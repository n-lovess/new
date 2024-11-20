class VirtualPet:
    def __init__(self, name: str):
        self.__name = name  # Private attribute for pet's name
        self.__hunger = 50  # Hunger level (0-100)
        self.__happiness = 50  # Happiness level (0-100)

    # Getter for name
    @property
    def name(self):
        return self.__name

    # Setter for name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self.__name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    # Getter for hunger
    @property
    def hunger(self):
        return self.__hunger

    # Method to feed the pet (reduce hunger)
    def feed(self, amount: int):
        if amount > 0:
            self.__hunger = max(0, self.__hunger - amount)

    # Getter for happiness
    @property
    def happiness(self):
        return self.__happiness

    # Method to play with the pet (increase happiness)
    def play(self, amount: int):
        if amount > 0:
            self.__happiness = min(100, self.__happiness + amount)