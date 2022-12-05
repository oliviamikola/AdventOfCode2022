from typing import List, Dict
from copy import deepcopy
from DayBase import DayBase, DayBaseSmall
from Objects.Stack import Stack


class Day5(DayBase):
    def __init__(self):
        DayBase.__init__(self, 5, to_int=False)

        self.stacks_part_one: Dict[int, Stack] = {}
        self.stacks_part_two: Dict[int, Stack] = {}
        self.moves: List[List[int]] = []

        start_moves: bool = False
        for line in self.data:
            if line.strip() == "":
                start_moves = True
                for column in self.stacks_part_one:
                    self.stacks_part_one[column].remove()
                    self.stacks_part_one[column].reverse()
                    self.stacks_part_two[column] = deepcopy(self.stacks_part_one[column])
                continue

            if not start_moves:
                current_index = 1
                while current_index < len(line):
                    current_column: int = (current_index - 1) // 4
                    if self.stacks_part_one.get(current_column) is None:
                        self.stacks_part_one[current_column] = Stack()

                    value: str = line[current_index]
                    if value.strip() != "":
                        self.stacks_part_one[current_column].add(value)

                    current_index += 4

            else:
                part_one: str = line.strip("move ")
                part_two: List[str] = part_one.split(" from ")
                part_three: List[int] = list(map(int, part_two[-1].split(" to ")))

                count: int = int(part_two[0])
                original_index = int(part_three[0]) - 1
                new_index = int(part_three[1]) - 1

                self.moves.append([count, original_index, new_index])

    def __get_top_string(self, stacks: Dict[int, Stack]) -> str:
        top_values: str = ""
        for column in sorted(stacks.keys()):
            top_values += stacks[column].get_top()
        return top_values

    def part1(self):
        for move in self.moves:
            for _ in range(move[0]):
                to_move: str = self.stacks_part_one[move[1]].remove()
                self.stacks_part_one[move[2]].add(to_move)

        return self.__get_top_string(self.stacks_part_one)

    def part2(self):
        for move in self.moves:
            to_move: List[str] = self.stacks_part_two[move[1]].remove_many(move[0])
            self.stacks_part_two[move[2]].add_group(to_move)

        return self.__get_top_string(self.stacks_part_two)


day = Day5()
day.run()
