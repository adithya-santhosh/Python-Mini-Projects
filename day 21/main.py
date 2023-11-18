class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe (self):
        print("Breathing")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing inside water")

    def swim(self):
        print("Swimming in Water")

nemo = Fish()
nemo.breathe()
print(nemo.eyes)