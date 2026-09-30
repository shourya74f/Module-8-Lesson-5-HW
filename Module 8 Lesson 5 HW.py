from abc import ABC, abstractmethod
class i(ABC):
    def __init__(self, name):
        self.name = name
    def d(self):
        print(f"Instrument name: {self.name}")
    @abstractmethod 
    def p(self):
        pass
class Guitar(i):
    def __init__(self, name, strings):
        super().__init__(name)
        self.strings = strings
    def p(self):
        print(f"{self.name} has {self.strings} strings.")
class Piano(i):
    def __init__(self, name, keys):
        super().__init__(name)
        self.keys=keys
    def p(self):
        print(f"{self.name} has {self.keys} keys.")
n1 = Guitar("Guitar", 6)
n2 = Piano("Piano", 88)
print("Welcome to the Instrument Information Program!")
n1.d()
n1.p()
n2.d()
n2.p()
