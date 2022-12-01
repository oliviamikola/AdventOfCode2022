from DayBase import DayBase, DayBaseSmall
from typing import List, Dict


class Day1(DayBase):
    def __init__(self):
        DayBase.__init__(self, 1, to_int=False)

        self.elf_calories: Dict[int, List] = {}

        elf: int = 1
        calories: List = []
        for calorie in self.data:
            if calorie == "":
                self.elf_calories[elf] = calories
                calories = []
                elf += 1
                continue
            calories.append(int(calorie))

        self.total_calories_per_elf: List = []
        self.sorted_calorie_amounts: List = []

    def part1(self):
        self.total_calories_per_elf = [sum(calories) for calories in self.elf_calories.values()]
        self.sorted_calorie_amounts = sorted(self.total_calories_per_elf, reverse=True)

        return self.sorted_calorie_amounts[0]  # 70613

    def part2(self):
        return sum(self.sorted_calorie_amounts[0: 3])  # 205805


day = Day1()
day.run()
