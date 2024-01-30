# This improves the application by making use of the multiple inheritance without having the diamond problem that comes from two deriving from 2 classes that has common base class

import hr_system
import productivity
import employee

manager = employee.Manager(1, "Robert MacCoy", 3000)
secretary = employee.Secretary(2, "Janet Jack", 1800)
sales_lady = employee.SalesPerson(3, "Ginny Philip", 1500, 350)
factory_worker = employee.FactoryWorker(4, "Nathan Gate", 40, 20)
temporary_secretary = employee.TemporarySecretary(5, "Anne Smith", 40, 15)

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