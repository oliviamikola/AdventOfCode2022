from DayBase import DayBase, DayBaseSmall
from Objects.Rucksack import Rucksack
from typing import List


class Day3(DayBase):
    def __init__(self):
        DayBase.__init__(self, 3, to_int=False)

        self.rucksacks: List[Rucksack] = []
        for line in self.data:
            self.rucksacks.append(Rucksack(line))

    def part1(self):
        total_sum = 0
        for rucksack in self.rucksacks:
            common_items = rucksack.find_common_in_current()
            for item in common_items:
                total_sum += Rucksack.convert(item)

        return total_sum  # 8088

    def part2(self):
        total_sum = 0
        for index in range(0, len(self.rucksacks), 3):
            common_items = self.rucksacks[index].find_common_in_multiple(self.rucksacks[index + 1: index + 3])

            for item in common_items:
                total_sum += Rucksack.convert(item)

        return total_sum  # 2522


day = Day3()
day.run()
