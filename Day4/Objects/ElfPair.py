from Objects.Elf import Elf


class ElfPair:
    def __init__(self, first_elf_range: str, second_elf_range: str):
        self.first_elf: Elf = Elf(first_elf_range)
        self.second_elf: Elf = Elf(second_elf_range)

    def check_if_fully_contained(self) -> bool:
        # if second elf is fully contained in the first elf
        if self.second_elf.start >= self.first_elf.start and self.second_elf.end <= self.first_elf.end:
            return True

        # if first elf is fully contained in the second elf
        if self.first_elf.start >= self.second_elf.start and self.first_elf.end <= self.second_elf.end:
            return True

        return False

    def check_for_overlap(self) -> bool:
        if (self.first_elf.start <= self.second_elf.start <= self.first_elf.end or
                self.first_elf.start <= self.second_elf.end <= self.first_elf.end):
            return True

        if (self.second_elf.start <= self.first_elf.start <= self.second_elf.end or
                self.second_elf.start <= self.first_elf.end <= self.second_elf.end):
            return True

        return False
