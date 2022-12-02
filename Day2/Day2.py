from DayBase import DayBase, DayBaseSmall
from typing import List, Tuple


class Day2(DayBase):
    def __init__(self):
        DayBase.__init__(self, 2, to_int=False)

        # A for Rock, B for Paper, and C for Scissors
        # X for Rock, Y for Paper, and Z for Scissors
        # 1 for Rock, 2 for Paper, and 3 for Scissors

        self.rounds: List[Tuple[int, int]] = [self.__translate_moves(round.split()) for round in self.data]

    def __translate_moves(self, moves: List[str]) -> Tuple[int, int]:
        return (self.__translate_opponent_move(moves[0]), self.__translate_my_move(moves[1]))

    def __translate_opponent_move(self, move: str) -> int:
        if move == "A":
            return 1
        elif move == "B":
            return 2
        elif move == "C":
            return 3

        return 0

    def __translate_my_move(self, move: str) -> int:
        if move == "X":
            return 1
        elif move == "Y":
            return 2
        elif move == "Z":
            return 3

        return 0

    def __calculate_winnings(self, opponent_move: int, my_move: int) -> int:
        # 0 if you lost, 3 if the round was a draw, and 6 if you won
        # 1 for Rock, 2 for Paper, and 3 for Scissors

        if opponent_move == my_move:
            return 3
        elif ((my_move == 1 and opponent_move == 3) or
              (my_move == 2 and opponent_move == 1) or
              (my_move == 3 and opponent_move == 2)):
            return 6
        else:
            return 0

    def calculate_round_score(self, opponent_move: int, my_move: int) -> int:
        return my_move + self.__calculate_winnings(opponent_move, my_move)

    def find_my_move(self, opponent_move: int, outcome: int) -> int:
        # 1 for Rock, 2 for Paper, and 3 for Scissors
        # X/1 means you need to lose
        # Y/2 means you need to end the round in a draw
        # Z/3 means you need to win
        if outcome == 1:  # lose
            if opponent_move == 1:
                return 3
            elif opponent_move == 2:
                return 1
            elif opponent_move == 3:
                return 2
        elif outcome == 2:  # draw
            return opponent_move
        elif outcome == 3:  # win
            if opponent_move == 1:
                return 2
            elif opponent_move == 2:
                return 3
            elif opponent_move == 3:
                return 1

    def part1(self):
        total_score: int = 0
        for round in self.rounds:
            total_score += self.calculate_round_score(*round)
        return total_score  # 8890

    def part2(self):
        total_score = 0
        for round in self.rounds:
            my_move = self.find_my_move(*round)
            total_score += self.calculate_round_score(round[0], my_move)
        return total_score  # 10238


day = Day2()
day.run()
