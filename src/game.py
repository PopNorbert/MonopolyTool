from dataclasses import dataclass
from typing import List

from entities.Board import Board
from entities.Player import Player


@dataclass
class Game:
    players:List[Player]
    board:Board

    def start(self):
        while True:
            for player in self.players:


