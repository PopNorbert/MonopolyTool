from dataclasses import dataclass


@dataclass
class Player:
    name: str
    position: int
    balance: int
