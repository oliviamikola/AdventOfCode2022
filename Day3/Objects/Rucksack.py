from __future__ import annotations
from typing import Set, List


class Rucksack:
    def __init__(self, contents: str):
        halfway_index: int = len(contents) // 2

        self.total: Set[str] = set(contents)
        self.first_sack: Set[str] = set(contents[:halfway_index])
        self.second_sack: Set[str] = set(contents[halfway_index:])

    def find_common_in_current(self) -> Set[str]:
        return self.first_sack.intersection(self.second_sack)

    def find_common_in_multiple(self, rucksacks: List[Rucksack]) -> Set[str]:
        if rucksacks is None or len(rucksacks) == 0:
            return self.total

        common_items = self.total
        for rucksack in rucksacks:
            common_items = common_items.intersection(rucksack.total)
        return common_items

    @staticmethod
    def convert(letter: str) -> int:
        if letter.isupper():
            return ord(letter) - 38
        return ord(letter) - 96
