import math


def special_math(a: int, b: int) -> int:
    c = math.fabs(a) + math.fabs(b)
    return int(c)


def greeting(name: str) -> str:
    return "Hello " + name
