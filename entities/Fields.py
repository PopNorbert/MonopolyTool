from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List


@dataclass
class Field(ABC):
    name: str

    @abstractmethod
    def execute(self, player):
        pass


@dataclass
class Property(Field):
    type: str
    rent: List[int]
    level: int = 0

    @abstractmethod
    def getRent(self):
        pass

@dataclass
class ColorProperty(Property):
    def getRent(self):
        pass

@dataclass
class Railroad(Property):
    def getRent(self):
        pass

@dataclass
class Utility(Property):
    def getRent(self):
        pass

@dataclass
class Start(Field):
    pass

@dataclass
class PayField(Field):
    pass
@dataclass
class ChooseField(Field):
    pass

