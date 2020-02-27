import heapq
from dataclasses import dataclass, field
from functools import total_ordering
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
@total_ordering
class Ninja:
    """Ninja class object"""

    name: str
    bites: int

    def __eq__(self, other) -> bool:
        return (self.bites, self.name) == (other.bites, other.name)

    def __gt__(self, other) -> bool:
        return (self.bites, self.name) > (other.bites, other.name)

    def __lt__(self, other) -> bool:
        return (self.bites, self.name) < (other.bites, other.name)

    def __str__(self) -> str:
        return f"[{self.bites}] {self.name}"


@dataclass
class Rankings:
    """Rankings class object"""

    _ninjas: List[Ninja] = field(default_factory=list)

    def __post_init__(self):
        heapq.heapify(self._ninjas)

    def __len__(self) -> int:
        return len(self._ninjas)

    def add(self, ninja: Ninja):
        """Adds a new Ninja"""
        heapq.heappush(self._ninjas, ninja)

    def dump(self) -> Ninja:
        """Removes the lowest ranking Ninja"""
        return heapq.heappop(self._ninjas)

    def highest(self, count: int = 1) -> List[Ninja]:
        """Returns the highest ranking Ninja"""
        return heapq.nlargest(count, self._ninjas)

    def lowest(self, count: int = 1) -> List[Ninja]:
        """Returns the lowest ranking Ninja

        :param count: Integer that indicates how many Ninjas return
        :return: List of Ninjas
        """
        return heapq.nsmallest(count, self._ninjas)

    def pair_up(self, count: int = 3) -> List[Tuple[Ninja, Ninja]]:
        """Pairs up study partners

        :param count: Integer that indicates how many Ninjas to pair up
        :return: List containing tuples of the paired up Ninjas
        """
        return list(zip(self.highest(count), self.lowest(count)))

