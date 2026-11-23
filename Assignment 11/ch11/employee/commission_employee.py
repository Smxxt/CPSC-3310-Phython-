from employee import Employee


class CommissionEmployee(Employee):
    def __init__(self, name, base_pay, commission_earned):
        total_pay = base_pay + commission_earned
        super().__init__(name, total_pay, "Commission Employee")
        self.base_pay = base_pay
        self.commission_earned = commission_earned

    def earnings(self):
        return self.base_pay + self.commission_earned

    def commission_breakdown(self):
        total = self.earnings()
        pct = (self.commission_earned / total) * 100 if total > 0 else 0.0
        return (
            f"Base ${self.base_pay:.2f} + "
            f"Commission ${self.commission_earned:.2f} "
            f"({pct:.1f}% of earnings)"
        )