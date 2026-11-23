from pet import Pet


class Bird(Pet):
    def __init__(self, name):
        super().__init__(name, "Bird")

    def speak(self):
        return "Tweet!"
