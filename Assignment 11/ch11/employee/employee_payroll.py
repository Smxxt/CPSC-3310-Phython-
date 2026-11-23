from commission_employee import CommissionEmployee
from employee import Employee
from hourly_employee import HourlyEmployee
from salary_employee import SalaryEmployee


def main():
    # Dictionary mapping department names to lists of employee objects
    departments = {
        "Sales": [
            HourlyEmployee("Nick DeFalco", 25.00),
            SalaryEmployee("Applejack Johnson", 44000.00),
            SalaryEmployee("Mario Dubois", 77200.00),
        ],
        "Engineering": [
            SalaryEmployee("Anthony Jo", 98000.00),
            Employee("Stephanie Johnson", 31200.00),
        ],
        "Maintenance": [
            CommissionEmployee("Dominic Togo", 20000.00, 45000.00),
            HourlyEmployee("Christina Gonzalez", 19.80),
        ],
        "HR": [
            HourlyEmployee("Geoffrey Dav", 65.00),
        ],
    }

    for dept, employees in departments.items():
        print(f"Department: {dept}")
        total_payroll = 0.0

        for emp in employees:
            # Polymorphic __str__() and earnings() calls
            print(emp)
            total_payroll += emp.earnings()

            # Check type before calling CommissionEmployee-specific breakdown
            if isinstance(emp, CommissionEmployee):
                print(emp.commission_breakdown())

        print(f"Total Payroll: ${total_payroll:.2f}")


if __name__ == "__main__":
    main()