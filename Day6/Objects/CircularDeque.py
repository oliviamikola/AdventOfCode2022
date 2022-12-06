from typing import List


class CircularDeque:
    def __init__(self, starting_size: int = 4):
        self.start_index: int = 0
        self.end_index: int = 0
        self.data: List[str] = [""] * starting_size

    def size(self) -> int:
        if self.end_index == self.start_index:
            return 0
        elif self.end_index > self.start_index:
            return self.end_index - self.start_index
        else:
            return len(self.data) - self.start_index + self.end_index

    def __str__(self) -> str:
        value: str = ""
        current_location: int = self.start_index
        while current_location != self.end_index:
            value += self.data[current_location]
            current_location = (current_location + 1) % len(self.data)
        return value

    def add_to_end(self, value: str) -> None:
        if self.size() >= len(self.data) // 2:
            self.grow()

        self.data[self.end_index] = value
        self.end_index = (self.end_index + 1) % len(self.data)

    def grow(self):
        new_data = [""] * (2 * len(self.data))
        self.start_index = 0
        self.end_index = 0
        for item in self.data:
            if item.strip() == "":
                break
            new_data[self.end_index] = item
            self.end_index += 1
        self.data = new_data

    def remove_from_front(self) -> str:
        value = self.data[self.start_index]
        self.start_index = (self.start_index + 1) % len(self.data)
        return value
