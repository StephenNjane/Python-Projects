def find_acronym():
    # Prompt user for the acronym they want to look up
    look_up = input("What software are you looking for?\n ")

    found = False
    try: 
        with open("acronym.txt", "r") as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("Error: The file was not found.")
        return
    if not found:
        print("Software acronym not found in the list.")

def add_acronym():
    # Prompt user for the acronym and its definition
    acronym = input("What acronym do you want to add?\n")
    definition = input("What is the definition of the acronym?\n")
    with open("acronym.txt", "a") as file:
        file.write(acronym + '  ' + definition + '\n')

def main():
    """Main function to run the acronym management system."""
    while True:
        print("\nAcronym Management System")
        print("A. Find an acronym")
        print("B. Add a new acronym")
        print("C. Exit")
        
        choice = input("Please choose an option (A-C): ")
        
        if choice == 'A':
            find_acronym()
        elif choice == 'B':
            add_acronym()
        elif choice == 'C':
            print("Exiting the Acronym Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

main()  # Ensure the script runs when executed directly