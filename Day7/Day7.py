from DayBase import DayBase, DayBaseSmall
from Objects.Directory import Directory
from typing import Optional, List


class Day7(DayBase):
    FILE_SYSTEM_SIZE = 70000000
    SPACE_FOR_UPDATE = 30000000

    def __init__(self):
        DayBase.__init__(self, 7, to_int=False)

        self.directory: Directory = Directory(None, "/")

        current_directory: Optional[Directory] = None
        for line in self.data:
            line = line.strip("$ ")

            if line.strip() == "cd /":
                current_directory = self.directory
                continue

            line_data: List[str] = line.split()

            command = line_data[0]
            if command == "ls":
                continue
            elif command == "dir":
                # make new directory
                current_directory.add_directory(line_data[1])
            elif command == "cd":
                # change directory
                current_directory = current_directory.get_directory(line_data[1])
            else:
                # make new file
                current_directory.add_file(line_data[1], int(line_data[0]))

        self.directory.get_size()

    def part1(self):
        return self.directory.find_directories_with_size_n(100000)  # 1443806

    def part2(self):
        used_space = self.directory.size
        need_to_free = Day7.SPACE_FOR_UPDATE - (Day7.FILE_SYSTEM_SIZE - used_space)

        return self.directory.find_smallest_larger_than_n(need_to_free)  # 942298


day = Day7()
day.run()
