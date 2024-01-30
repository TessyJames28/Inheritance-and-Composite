import hr_system
import employees
import productivity

manager = employees.Manager(1, "John MacLean", 3000)
secretary = employees.Secretary(2, "John Smith", 1500)
sales_lady = employees.SalesPerson(3, "Jane Doe", 1000, 250)
factory_worker = employees.FactoryWorker(4, "Kevin Bacon", 40, 15)

employees = [
    manager,
    secretary,
    sales_lady,
    factory_worker
]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = hr_system.PayrollSystem()
payroll_system.calculate_payroll(employees)