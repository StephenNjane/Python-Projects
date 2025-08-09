class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    

class SalaryEmployee(Employee):
    def __init__(self, fname, lname,salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary / 52
    
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hourly_rate, hours_worked):
        super().__init__(fname, lname)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_paycheck(self):
        return self.hourly_rate * self.hours_worked
    
class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_amount, commission_rate):
        super().__init__(fname, lname, salary)
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    def calculate_paycheck(self):
        regular_pay = super().calculate_paycheck()
        commission_pay = self.sales_amount * self.commission_rate
        return regular_pay + commission_pay
    