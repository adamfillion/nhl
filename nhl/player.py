"""
Module containing NHL player objects
"""
from dataclasses import dataclass, field, InitVar
import datetime

from .flyweight import Flyweight

@dataclass(frozen=True)
class Player(Flyweight):
    """
    NHL player object.

    This is the detailed docstring.
    """
    __slots__ = ["id", "name", "number", "position", "height", "weight",
        "shoots_catches", "birth_date", "birth_city", "birth_country"]
    _instances = {}

    id: int
    """int: The NHL statsapi universal player ID"""

    name: str
    """str: Player's full name"""

    number: int
    """int: Player's primary number"""

    position: str
    """str: Player's primary position ("LW", "C", "RW", "D", "G")"""

    height: int
    """int: Player's height in total inches"""

    weight: int
    """int: Player's weight in lbs"""

    shoots_catches: str
    """str: Indication of whether the player shoots (skater)/catches (goalie) "L" or "R" """

    birth_date: InitVar[str]
    """:class:`datetime.date`: Player's birth date"""

    birth_city: str
    """str: Player's birth city"""

    birth_country: str
    """str: Player's birth country"""

    def _key(cls, id, *args, **kwargs):
        return id

    @classmethod
    def has_key(cls, id):
        """
        Check whether flyweight object with specified key has already been created.

        Returns:
            bool: True if already created, False if not
        """
        return super().has_key(id)

    @classmethod
    def from_key(cls, id):
        """
        Return flyweight object with specified key, if it has already been created.

        Returns:
            nhl.Player or None: Previously constructed flyweight object with given
            key or `None` if key not found
        """
        return super().from_key(id)

    def __post_init__(self, birth_date):
        year = int(birth_date.split("-")[0])
        month = int(birth_date.split("-")[1])
        day = int(birth_date.split("-")[2])
        object.__setattr__(self, "birth_date", datetime.date(year, month, day))

    @property
    def first_name(self):
        """str: Player's first name"""
        return self.name.split(" ", 1)[0]

    @property
    def last_name(self):
        """str: Player's last name"""
        return self.name.split(" ", 1)[1]

    @property
    def height_ft(self):
        """int: Height in feet (:py:attr:`height` // 12)"""
        return self.height // 12 if self.height else None

    @property
    def height_in(self):
        """int: Height in inches (:py:attr:`height` % 12)"""
        return self.height % 12 if self.height else None

    @property
    def age(self):
        """int: Current age in years"""
        return (datetime.date.today() - self.birth_date).days // 365
