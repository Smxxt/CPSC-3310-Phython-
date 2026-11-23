class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} the {self.species}"

    def speak(self):
        return "..."