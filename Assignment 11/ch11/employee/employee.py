class Employee:
    def __init__(self, name, annual_earnings=0.0, role_label="Employee"):
        self.name = name
        self.annual_earnings = annual_earnings
        self.role_label = role_label

    def earnings(self):
        return self.annual_earnings

    def __str__(self):
        return f"{self.name} ({self.role_label}): ${self.earnings():.2f}"