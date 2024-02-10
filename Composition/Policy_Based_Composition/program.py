from hr_system import PayrollSystem, HourlyPolicy
from employees import EmployeeDatabase
from productivity import ProductivitySystem


productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()

employees = employee_database.employees
# manager = employees[0]
# manager.payroll = HourlyPolicy(55)

productivity_system.track_work(employees, 40)
payroll_system.calculate_payroll(employees)