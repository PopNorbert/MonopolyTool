from dataclasses import dataclass
from typing import List, Match
import random

from entities.board import Board
from entities.fields import *
from entities.player import Player


def roll():
    v1, v2 = random.randint(1, 6), random.randint(1, 6)
    return v1 + v2

def log(message):
    print("\nmessage")


@dataclass
class Game:
    players: List[Player]
    board: Board
    roll: int=0
    player: Player=None

    def start(_):
        while True:
            for p in _.players:
                _.player = p
                _.roll = roll()
                _.moveBy()

    def moveBy(_):
        _.player.position = _.player.position + _.roll
        if _.player.position > 39:
            _.player.position = _.player.position - 40
            _.player.balance += 200
        _.board[_.player.position].execute()


    def execute(_):
        field = _.board[_.player.position]
        match field.:
            case ColorProperty(rent):
            case Railroad():
            case Utility():
            case ChooseField():
            case JailField():
            case PayField():



