#here we have a static list of expenses
#we will use the sum function to calculate the total expenses
total = 0
expenses = []
for i in range(7):
    expenses.append(float(input('Enter your expenses:')))
total = sum(expenses)
print('Your Total expenses is $', total, sep='')

#here we have a dynamic list of expenses
total = 0
expenses = []
number_of_expenses = int(input("How many expenses do you want to enter? "))
for i in range(number_of_expenses):
    expenses.append(float(input('Enter your expenses:')))
total = sum(expenses)
print('Your Total expenses is $', total, sep='')
