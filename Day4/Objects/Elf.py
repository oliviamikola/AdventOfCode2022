class Elf:
    def __init__(self, cleaning_range: str):
        self.start: int = int(cleaning_range.split("-")[0])
        self.end: int = int(cleaning_range.split("-")[1])
