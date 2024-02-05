class ProductivitySystem:
    def ___init__(self):
        self._roles = {
            "manager": ManagerRole,
            "secretary": SecretaryRole,
            "sales": SalesRole,
            "factory": FactoryRole,
        }
        
        
    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
    
    
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