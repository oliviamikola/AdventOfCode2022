from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def add(self, value: str) -> None:
        self.data.append(value)

    def add_group(self, group: List[str]) -> None:
        self.data.extend(group)

    def remove(self) -> str:
        return self.data.pop()

    def remove_many(self, remove_count: int) -> List[str]:
        to_remove: List[str] = self.data[-remove_count:]
        self.data = self.data[:-remove_count]
        return to_remove

    def reverse(self) -> None:
        self.data = self.data[::-1]

    def get_top(self) -> str:
        return self.data[-1]
