# a bass class Employee that handles the common interface for every employee type

class Employee():
    def __init__(self, id, name):
        self.id = id
        self. name = name
        
        
        
# the system requires that every employee procesed must provide a .calculate_payroll() interface
# that returns the weekly salary for the employee.

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
        
    def calculate_payroll(self):
        return self.weekly_salary
    
    
# for employees paid hourly

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        
    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate
    
# for sales associate who are paid fixed salary plus commission based on their sales

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
        
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
        
    
    