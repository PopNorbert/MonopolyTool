from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

from entities.player import Player


@dataclass
class Field(ABC):
    name: str


@dataclass
class ColorProperty(Field):
    type: str
    price: int
    mortgage: int
    housePrice: int
    rent: List[int]
    level: int = 0
    owner: Player = None
    def getRent(self):
        return self.rent[self.level]

    def execute(self, player):


@dataclass
class Railroad(Field):
    price: int
    mortgage: int
    rent: List[int]
    level: int = 0
    owner: Player = None
    def getRent(self):
        return self.rent[self.level]

    def execute(self, player):


@dataclass
class Utility(Field):
    price: int
    mortgage: int
    rent: List[int]
    level: int = 0
    owner: Player = None
    def getRent(self):
        pass

    def execute(self, player):

@dataclass
class DummyField(Field):

    def execute(self, player):
        pass


@dataclass
class PayField(Field):
    amount: int

    def execute(self, player):
        player.balance -= self.amount


# TODO
@dataclass
class ChooseField(Field):

    def execute(self, player):
        pass
