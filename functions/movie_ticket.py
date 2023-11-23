#A movie theater charges different ticket prices depending on a person’s age.movie ticket
age = input("Enter your age (or 'quit' to exit): ")

while  True:
    if age == 'quit':
        break

age = int(age)

if age < 3: 
    print('Your ticket is free!')
elif 3 <= age <= 12:
        print("The cost of your ticket is $10.")
else:
        print("The cost of your ticket is $15.")  
