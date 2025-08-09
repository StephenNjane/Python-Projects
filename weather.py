#the program assigns 95 to a variable named temperature. 
# The if statement checks if the temperature is greater than 80 and prints the statements if the condition is true
temperature = int(input("What is the temparature at this time?\n"))
if temperature > 80:
    print("It is too hot!")
    print("Stay inside and hydrated!")

elif temperature < 50:
    print("it is too cold stay inside and be warm!")
else:
    print("enjoy the weather outside|!!")

#combining the if statement with "or"
if temperature > 80 or temperature < 50:
    print("You should stay inside!")
else:
    print("You can go outside and enjoy the weather!")

#using the "and" operator: where all conditions must be true
temparature = int(input("What is the temparature at this time?\n"))
forecast = input("What is the weather forecast for today?\n")
if temperature < 80 and forecast != "rainy":
    print("You can go outside and enjoy the weather!")
else:
    print("You should stay inside!")

    #using the "not" operator: where the condition must be false
if not forecast == "rainy":
    print("You can go outside and enjoy the weather!") 

#using the boolean operators with the "if" statement 
raining = "yes"
if not raining: 
    print("You can go outside and enjoy the weather!") 
else: 
    print("You should stay inside!")            