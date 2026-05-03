from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict


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

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data left to output")

        data = self._storage.pop(0)
        rank = self._output_count
        self._output_count += 1
        return rank, data

    def get_stats(self):
        return self._total_count, len(self._storage)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and\
                all(isinstance(x, (int, float)) for x in data):
            return True
        return False

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
        if isinstance(data, list) and all(isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(item)
            self._total_count += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_log_dict(d: Any) -> bool:
            return isinstance(d, dict) and \
                "log_level" in d and "log_message" in d

        if is_log_dict(data):
            return True
        if isinstance(data, list) and all(is_log_dict(x) for x in data):
            return True
        return False

    def ingest(self, data: Union[Dict[str, str], List[Dict[str, str]]])\
            -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            formatted_log = f"{item['log_level']}: {item['log_message']}"
            self._storage.append(formatted_log)
            self._total_count += 1


class DataStream:
    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor):
        self.processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            found = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    found = True
                    break
            if not found:
                print(f"DataStream error - Can't process element in stream: \
{element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            total, remaining = proc.get_stats()
            print(
                f"{name}: total {total} items processed, remaining \
{remaining} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...\n")
    ds = DataStream()
    ds.print_processors_stats()

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("\nRegistering Numeric Processor")
    num_p = NumericProcessor()
    ds.register_processor(num_p)

    print(f"\nSend first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    text_p = TextProcessor()
    log_p = LogProcessor()
    ds.register_processor(text_p)
    ds.register_processor(log_p)

    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nConsume some elements from the data "
          "processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_p.output()
    for _ in range(2):
        text_p.output()
    for _ in range(1):
        log_p.output()

    ds.print_processors_stats()
