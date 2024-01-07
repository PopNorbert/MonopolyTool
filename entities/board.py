from dataclasses import dataclass
from typing import List

from entities.fields import *


@dataclass
class Board:
    fields: List[Field]

    def __getitem__(self, item):
        return self.fields[item]
