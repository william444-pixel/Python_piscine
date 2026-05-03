from typing import Protocol, List, Tuple, Any, Union, Dict
from abc import ABC, abstractmethod


class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        ...


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[str] = []
        self._total_count: int = 0
        self._output_count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Union[Tuple[int, str], None]:
        if not self._storage:
            return None

        data = self._storage.pop(0)
        rank = self._output_count
        self._output_count += 1
        return rank, data

    def get_stats(self) -> Tuple[int, int]:
        return self._total_count, len(self._storage)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        return isinstance(data, list) and \
            all(isinstance(x, (int, float)) for x in data)

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(str(item))
            self._total_count += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return isinstance(data, list) and all(isinstance(x, str) for x in data)

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(item)
            self._total_count += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_log(d: Any) -> bool:
            return isinstance(d, dict) and "log_level" \
                in d and "log_message" in d

        if is_log(data):
            return True
        return isinstance(data, list) and all(is_log(x) for x in data)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            formatted = f"{item['log_level']}: {item['log_message']}"
            self._storage.append(formatted)
            self._total_count += 1


class DataStream:
    def __init__(self) -> None:
        self.processors: Dict[str, DataProcessor] = {}

    def register_processor(self, name: str, proc: DataProcessor) -> None:
        self.processors[name] = proc

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            found = False
            for proc in self.processors.values():
                if proc.validate(element):
                    proc.ingest(element)
                    found = True
                    break
            if not found:
                print(f"DataStream error - Can't process element: {element}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors.values():
            extracted: List[Tuple[int, str]] = []
            for _ in range(nb):
                val = proc.output()
                if val is not None:
                    extracted.append(val)

            if extracted:
                plugin.process_output(extracted)

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for name, proc in self.processors.items():
            total, remaining = proc.get_stats()
            print(f"{name}: total {total} items processed, remaining \
{remaining} on processor")


class CSVExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join([item[1] for item in data]))


class JSONExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        print("JSON Output:")
        items = [f'"item_{item[0]}": "{item[1]}"' for item in data]
        print("{" + ", ".join(items) + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")

    print("\nInitialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors\n")
    ds.register_processor("Numeric Processor", NumericProcessor())
    ds.register_processor("Text Processor", TextProcessor())
    ds.register_processor("Log Processor", LogProcessor())

    batch1 = ['Hello world', [3.14, -1, 2.71],
              [{'log_level': 'WARNING', 'log_message':
                  'Telnet access! Use ssh instead'},
               {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
              42, ['Hi', 'five']]

    print(f"\nSend first batch of data on stream: {batch1}")
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVExportPlugin())
    ds.print_processors_stats()

    batch2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR', 'log_message': '500 server crash'},
               {'log_level': 'NOTICE', 'log_message':
                   'Certificate expires in 10 days'}],
              [32, 42, 64, 84, 128, 168], 'World hello']

    print(f"Send another batch of data: {batch2}")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONExportPlugin())
    ds.print_processors_stats()
