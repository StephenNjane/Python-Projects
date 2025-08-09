money_owed = float(input("How much money do you owe in dollars?\n"))
interest_rate = float(input("What is the interest rate in percent?\n")) / 100
years = int(input("How many years will it take to pay off the loan?\n"))

monthly_payment = money_owed * (interest_rate / 12) / (1 - (1 + interest_rate / 12) ** (-years * 12))

interest_paid = monthly_payment * years * 12 - money_owed
print(f"You will pay a total of ${interest_paid:.2f} in interest over the life of the loan.")

loan_amount = money_owed + interest_paid
print(f"The total amount to be paid back is ${loan_amount:.2f}.")

remaining_balance = loan_amount
for month in range(years * 12):
    remaining_balance -= monthly_payment
    if remaining_balance < 0:
        remaining_balance = 0
    print(f"After month {month + 1}, the remaining balance is ${remaining_balance:.2f}.")

print(f"Your monthly payment will be ${monthly_payment:.2f}.")

