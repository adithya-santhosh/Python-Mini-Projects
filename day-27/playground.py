def add(*args):
    s = 0
    for i in args:
        s += i
    return s


print(add(3, 4, 5, 6, 7))

print(add(9, 6, 5, 7, 8, 4, 3, 2, 1))


def calculate(n, **kwargs):

    n += kwargs["add"]
    n -= kwargs["subtract"]
    n *= kwargs["multiply"]
    return n

print(calculate(5, multiply=10,subtract=5,add=10))

class Car:
    def __init__(self, **kw ):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.model = kw.get("colour")
        self.model = kw.get("Seats")