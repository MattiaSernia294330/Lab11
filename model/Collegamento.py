from dataclasses import dataclass
from datetime import date
@dataclass
class Collegamento:
    p1:int
    p2:int
    data:date

    def __hash__(self):
        return hash(f"{self.p1}{self.p2}{self.data}")