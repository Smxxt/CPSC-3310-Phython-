from employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name, annual_salary, "Salaried Employee")
        self.annual_salary = annual_salary

    def earnings(self):
        return self.annual_salary