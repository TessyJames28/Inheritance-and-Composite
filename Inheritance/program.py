import hr_system

salary_employee = hr_system.SalaryEmployee(1, "John Smith", 1500)
hourly_employee = hr_system.HourlyEmployee(2, "Jane Doe", 40, 15)
commission_employee = hr_system.CommissionEmployee(3, "Kevin Bacon", 1000, 250)

payroll_system = hr_system.PayrollSystem()
payroll_system.calculate_payroll(
    [salary_employee, hourly_employee, commission_employee]
)