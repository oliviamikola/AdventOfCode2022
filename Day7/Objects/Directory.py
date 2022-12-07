from __future__ import annotations
import sys
from typing import Optional, Dict
from Objects.File import File


class Directory:
    def __init__(self, parent: Optional[Directory], name: str):
        self.name = name
        self.files: Dict[str, File] = {}
        self.directories: Dict[str, Directory] = {}
        self.parent: Directory = parent
        self.size: int = 0

    def add_file(self, name: str, size: int) -> None:
        self.files[name] = File(name, size)
        self.size += size

    def add_directory(self, name: str) -> None:
        self.directories[name] = Directory(self, name)

    def get_directory(self, name: str) -> Directory:
        if name == "..":
            return self.parent
        return self.directories[name]

    def get_size(self) -> int:
        total_size: int = 0
        for directory in self.directories.values():
            total_size += directory.get_size()
        for file in self.files.values():
            total_size += file.size
        self.size = total_size
        return total_size

    def find_directories_with_size_n(self, n: int) -> int:
        total_sizes: int = 0
        if self.size <= n:
            total_sizes += self.size

        for directory in self.directories.values():
            total_sizes += directory.find_directories_with_size_n(n)

        return total_sizes

    def find_smallest_larger_than_n(self, n: int) -> int:
        directory_size: int = sys.maxsize
        if n < self.size < directory_size:
            directory_size = self.size

        for directory in self.directories.values():
            directory_smallest_n = directory.find_smallest_larger_than_n(n)
            if n < directory_smallest_n < directory_size:
                directory_size = directory_smallest_n

        return directory_size
