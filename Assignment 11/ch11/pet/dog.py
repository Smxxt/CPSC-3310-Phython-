from pet import Pet


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def speak(self):
        return "Woof!"
    