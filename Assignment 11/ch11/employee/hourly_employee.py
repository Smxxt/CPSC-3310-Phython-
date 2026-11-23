from employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_per_week=40, weeks=52):
        annual_pay = hourly_rate * hours_per_week * weeks
        super().__init__(name, annual_pay, "Hourly Employee")
        self.hourly_rate = hourly_rate
        self.hours_per_week = hours_per_week
        self.weeks = weeks

    def earnings(self):
        return self.hourly_rate * self.hours_per_week * self.weeks