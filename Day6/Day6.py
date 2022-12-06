from DayBase import DayBase, DayBaseSmall
from Objects.CircularDeque import CircularDeque


class Day6(DayBase):
    def __init__(self):
        DayBase.__init__(self, 6, to_int=False)

    def __find_n_consecutive_unique(self, n: int) -> int:
        deque: CircularDeque = CircularDeque()
        for index, character in enumerate(self.data[0], 1):
            deque.add_to_end(character)

            if deque.size() == n:
                if len(set(str(deque))) == n:
                    return index
                deque.remove_from_front()

    def part1(self):
        return self.__find_n_consecutive_unique(4)  # 1658

    def part2(self):
        return self.__find_n_consecutive_unique(14)  # 2260


day = Day6()
day.run()
