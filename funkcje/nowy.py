from typing import Union, Any, Optional, Callable
from dataclasses import dataclass
def multiply_string(factor: int, text: str) -> str:
    """
    :type factor: int
    :type text: str
    :rtype: str
    """
    return factor * text



multiply_string(5, 'text')


x : str = "Lorem ipsum"
x: int = 1_000_000
x: float = 0.5
x: bool = True

l1: list[int] = [1, 2, 3]
l2: list[Union[int, str]] = ['text', 1, 2]
l3: list[tuple[Any, Any]] = [('1', 2), (3, 3.40), ('tt', True)]


def multiply(a: int, b: int , c: Optional[int] = None):
    return a * b * c if c else a * b


print(multiply(1, 2, 3))
print(multiply(1, 5))

def do_something(): pass


fun: Callable = do_something

@dataclass
class Point:
    x: int = 0
    y: int = 0


p: Point = Point()




