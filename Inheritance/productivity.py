# The productivity interface to make use of the .work method and track hours worked

class ProductivitySystem:
    def track(self, employees, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            employee.work(hours)
        print("")