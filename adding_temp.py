acronym = input("What acronym do you want to add?\n")
definition = input("What is the definition of the acronym?\n")
with open("acronym.txt", "a") as file:
    file.write(acronym + '  ' + definition + '\n')