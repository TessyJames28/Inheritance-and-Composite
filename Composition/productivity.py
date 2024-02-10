class ProductivitySystem:
    def track(self, employees, hours):
        print(f"Tracking Employee Productivity")
        print("===============================")
        for employee in employees:
            result = employee.work(hours)
            print(f"{employee.name}: {result}")
            print("")
        print("")
        
        

class ManagerRole:
    def work(self, hours):
        return f"screams and yells for {hours} hourrs."
    

class SecretaryRole:
    def work(self, hours):
        return f"expends {hours} hours doing office paperwork."
    
    
class SalesRole:
    def work(Self, hours):
        return f"expends {hours} hours on the phone."
    
    
class FactoryRole:
    def work(self, hours):
        return f"manufactures gadgets for {hours} hours."