from dataclasses import dataclass
from datetime import datetime


@dataclass
class Entry:
    start:datetime
    end:datetime
    free:datetime
    energy:float

    @property
    def cost(self):
        parktime = max(int((self.free-self.end).seconds/60)-15,0)
        return round(self.energy*0.31+parktime*0.05,2)
