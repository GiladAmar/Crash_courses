nothing: str
pi: float = 3.142


def headline(text: str, align: bool = True) -> str:
    return "stringy"


# Basic Types:
    # str
    # float
    # bool
    # int
    # list
    # tuple
    # dict


from typing import Dict, List, Tuple, Sequence

names: List[str] = ["Guido", "Jukka", "Ivan"]
version: Tuple[int, int, int] = (3, 7, 1)
options: Dict[str, bool] = {"centered": False, "capitalize": True}


# A sequence is either a list or a tuple
def square(elems: Sequence[float]) -> List[float]:
    return [x ** 2 for x in elems]


# Create aliases for commonly used types:
Card = Tuple[str, str]
Deck = List[Card]


def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


# For a function that should never return
from typing import NoReturn


def black_hole() -> NoReturn:
    raise Exception("There is no going back ...")


# Optional is type specified or None
from typing import Sequence, Optional


def player_order(names: Sequence[str], start: Optional[str] = None) -> Sequence[str]:
    pass


# Can type as an object
class Deck:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards


# Can use string literals to evaluate later if class not defined yet:
class Deck:
    # * No need to annotate self or cls

    @classmethod
    def create(cls, shuffle: bool = False) -> "Deck":
        import random

        """Create a new deck of 52 cards"""
        cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]
        if shuffle:
            random.shuffle(cards)
        return cls(cards)


# For unpacked arguments:
def __init__(self, *names: str) -> None:
    pass


# What type of function as a parameter?
from typing import Callable


def do_twice(func: Callable[[str], str], argument: str) -> None:
    print(func(argument))
    print(func(argument))

    # Callable[..., str] to not specify the input args


def create_greeting(name: str) -> str:
    return f"Hello {name}"


do_twice(create_greeting, "Jekyll")

# Common types
import numpy as np

np.NDArrayOperatorsMixin

from typing import TypeVar, Iterable, Tuple

T = TypeVar("T", int, float, complex)

AnyStr = TypeVar("AnyStr", Text, bytes)

# Union
from typing import Union


def handle_employees(e: Union[Employee, Sequence[Employee]]) -> None:
    if isinstance(e, Employee):
        e = [e]
    ...


# Union[Employee, None] same as Optional[Employee]


# for a class, not an instance of the class:
U = TypeVar("U", bound=User)


def new_user(user_class: Type[U]) -> U:
    ...


# also like this:
x, y, z = [], [], []  # type: List[int], List[int], List[str]

with frobnicate() as foo:  # type: int
    # Here foo is an int
    ...

for x, y in points:  # type: float, float
    # Here x and y are floats
    ...

# TODO
from Typing import date
