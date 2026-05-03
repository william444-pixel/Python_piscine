from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[str] = []
        self._count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data left to output")

        # تجباد أقدم معلومة (Index 0)
        data = self._storage.pop(0)
        rank = self._count
        self._count += 1
        return rank, data


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list)\
                and all(isinstance(x, (int, float)) for x in data):
            return True
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(str(item))


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


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_log_dict(d: Any) -> bool:
            return isinstance(d, dict)\
                and "log_level" in d and "log_message" in d

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


# --- Testing the Architecture ---
if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    # 1. Testing Numeric
    print("Testing Numeric Processor...")
    num_p = NumericProcessor()
    print(f"Trying to validate input '42': {num_p.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_p.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_p.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")

    num_p.ingest([1, 2, 3, 4, 5])
    print("Processing data: [1, 2, 3, 4, 5]")
    print("Extracting 3 values...")
    for i in range(3):
        rank, val = num_p.output()
        print(f"Numeric value {rank}: {val}")

    # 2. Testing Text
    print("\nTesting Text Processor...")
    text_p = TextProcessor()
    print(f"Trying to validate input '42': {text_p.validate(42)}")
    text_p.ingest(["Hello", "Nexus", "World"])
    print("Processing data: ['Hello', 'Nexus', 'World']")
    print("Extracting 1 value...")
    rank, val = text_p.output()
    print(f"Text value {rank}: {val}")

    # 3. Testing Log
    print("\nTesting Log Processor...")
    log_p = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_p.validate('Hello')}")
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    log_p.ingest(log_data)
    print(f"Processing data: {log_data}")
    print("Extracting 2 values...")
    for i in range(2):
        rank, val = log_p.output()
        print(f"Log entry {rank}: {val}")
