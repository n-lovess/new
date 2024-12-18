class VirtualPet:
    def __init__(self, name: str):
        self.__name = name
        self.__hunger = 0
        self.__happiness = 50
        self.__energy = 10

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self.__name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def hunger(self):
        return self.__hunger

    def feed(self, amount: int):
        if amount > 0:
            self.__hunger = max(0, self.__hunger - amount)

    @property
    def happiness(self):
        return self.__happiness

    def play(self):
        self.__happiness = min(100, self.__happiness + 10)
        self.__hunger = min(100, self.__hunger + 2)
        self.__energy = max(0, self.__energy - 2)

    def sleep(self):
        self.__energy = min(100, self.__energy + 10)

    @property
    def energy(self):
        return self.__energy

    def __str__(self):
        return f"{self.__name} with {self.__energy} energy points and {self.__hunger} hunger level"