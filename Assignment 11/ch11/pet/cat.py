from pet import Pet


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def speak(self):
        return "Meow!"