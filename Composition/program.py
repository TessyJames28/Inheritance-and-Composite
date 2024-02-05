import hr_system
import employees
import productivity
import contacts

manager = employees.Manager(1, "Robert MacCoy", 3000)
manager.address = contacts.Address("121 Admin Rd.", "Concord", "NH", "03301")
secretary = employees.Secretary(2, "Janet Jack", 1800)
secretary.address = contacts.Address("67 Paperwork Ave.", "Manchester", "NH", "03101")
sales_lady = employees.SalesPerson(3, "Ginny Philip", 1500, 350)
factory_worker = employees.FactoryWorker(4, "Nathan Gate", 40, 20)
temporary_secretary = employees.TemporarySecretary(5, "Anne Smith", 40, 15)

employees = [
    manager,
    secretary,
    sales_lady,
    factory_worker,
    temporary_secretary
]

productivity = productivity.ProductivitySystem()
productivity.track(employees, 40)

hr_system = hr_system.PayrollSystem()
hr_system.calculate_payroll(employees)