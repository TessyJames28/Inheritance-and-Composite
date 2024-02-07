from hr_system import PayrollSystem
from employees import EmployeeDatabase
from productivity import ProductivitySystem


productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()

employees = employee_database.employees
productivity_system.track_work(employees, 40)
payroll_system.calculate_payroll(employees)