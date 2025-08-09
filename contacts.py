contacts = { 
    'number': 4,
    'students': 
               [
                 {'name': 'Alice Wick', 'email': 'alicewick@example.com' , 'grade': 'A'},
                 {'name': 'Bob Smith', 'email': 'bob@example.com', 'grade': 'B'},
                 {'name': 'Charlie Brown', 'email': 'cbrown@example.com', 'grade': 'C'},
                 {'name': 'Diana Prince', 'email': 'princediana@example.com', 'grade': 'A+'}
              ] 
}

print('students emails in the contacts:')
for student in contacts['students']:
    #print(student)
    print(student['email'])