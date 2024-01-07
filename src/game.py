from dataclasses import dataclass
from typing import List
import random

from entities.fields import Field
from entities.player import Player


def roll():
    v1, v2 = random.randint(1, 6), random.randint(1, 6)
    return v1 + v2

def log(message):
    print("\nmessage")


@dataclass
class Game:
    players: List[Player]
    board: List[Field]

    def start(self):
        while True:
            for player in self.players:
                value = roll()
                self.move(player, value)

    def move(self, player, value):
        player.position = player.position + value
        if value > 39:
            player.position = player.position - 40
            player.balance += 200
        self.board[player.position].execute(player)

