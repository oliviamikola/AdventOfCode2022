from DayBase import DayBase, DayBaseSmall
from typing import List
from Objects.ElfPair import ElfPair


class Day4(DayBase):
    def __init__(self):
        DayBase.__init__(self, 4, to_int=False)

        self.pairs: List[ElfPair] = []
        for line in self.data:
            regions: List[str] = line.split(",")
            self.pairs.append(ElfPair(regions[0], regions[1]))

    def part1(self):
        fully_contained_pairs: int = 0
        for pair in self.pairs:
            fully_contained_pairs += 1 if pair.check_if_fully_contained() else 0
        return fully_contained_pairs  # 513

    def part2(self):
        overlapping_pairs: int = 0
        for pair in self.pairs:
            overlapping_pairs += 1 if pair.check_for_overlap() else 0
        return overlapping_pairs  # 878


day = Day4()
day.run()
