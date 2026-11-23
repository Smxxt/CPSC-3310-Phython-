class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} area:"

    def area(self):
        return 0.0