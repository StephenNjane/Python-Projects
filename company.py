from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__ (self):
        self.employees =[]
        
    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('------------------')

    def pay_employees(self):
        print('Paying Employees:')
        for i in self.employees:
            print(f'Payment for {i.fname} {i.lname}')
            print(f'The salary is Amount${i.calculate_paycheck():,.2f}')
            print('------------------')

def main():
    my_company = Company()

    employee1 = SalaryEmployee("John", "Doe", 52000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee("Jane", "Smith", 60, 40)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee("Alice", "Johnson", 35000, 48, 350)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()


main()  # Ensure the script runs when executed directly