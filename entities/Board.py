from dataclasses import dataclass
from typing import List

from Fields import *
@dataclass
class Board:
    fields: List[Field]
