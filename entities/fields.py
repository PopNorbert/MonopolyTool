from dataclasses import dataclass
from abc import ABC
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


@dataclass
class Railroad(Field):
    price: int
    mortgage: int
    rent: List[int]
    level: int = 0
    owner: Player = None
    def getRent(self):
        return self.rent[self.level]

@dataclass
class Utility(Field):
    price: int
    mortgage: int
    rent: List[int]
    level: int = 0
    owner: Player = None
    def getRent(self):
        pass

@dataclass
class DummyField(Field):
    pass


@dataclass
class PayField(Field):
    amount: int


@dataclass
class ChooseField(Field):
    pass
