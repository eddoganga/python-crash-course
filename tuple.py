tuple
dimensions = (200, 50)
print('Original Dimensions: ')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified Dimensions: ')
for dimension in dimensions:
    print(dimension)

foods = ('rice', 'ugali', 'beef', 'chicken', 'beans')
print('Here are the food available in Kafe Restaurant: ')
for food in foods:
    print(food.title())

cars = ['audi', 'toyota', 'subaru', 'bentley']
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())


alien_color = 'green'  # Assigning the color of the alien

# Checking if the alien's color is green
if alien_color == 'green':
    print("Congratulations! You just earned 5 points!")

alien_color = 'yellow'  # Assigning the color of the alien

# Checking if the alien's color is green
if alien_color == 'green':
    # There is no code inside this block, so no output will be produced.
    pass

alien_color = 'yellow'
if alien_color == 'yellow':
    print('The player just earned 5 points for shooting the alien')
else:
    print('The player just earned 10 points')

alien_color = 'green'
if alien_color == 'green':
    print('The player just earned 5 points!')
elif alien_color == 'yellow':
    print('The player just earned 10 points!')
elif alien_color == 'red':
    print('The player just earned 15 points!')
else:
    print('You lost!')

person_age = 50
if person_age < 2:
    print('The person is a baby')
elif person_age < 4:
    print("The person is a toddler.")
elif person_age < 13:
    print("The person is a kid.")
elif person_age < 20:
    print("The person is a teenager.")
elif person_age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

usernames = ['admin', 'john', 'sara', 'brad']
for username in usernames:
    if username.title() == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {username.title()}, thank you for logging in again.')
        

# Empty list of usernames
usernames = []  
if usernames:  # Check if the list is not empty
    for username in usernames:
        if username.lower() == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

#checking new usernames
current_users = ['edd', 'bruce', 'olaf', 'tim', 'bob', 'erik']
new_users = ['scott', 'bruce', 'bob', 'rhea', 'kim']

for new_user in new_users:
    if new_user.lower() in (user.lower() for user in current_users):
        print(f'{new_user} is not available. Enter a new username!')
    else:
        print(f'{new_user} is available.')

#ordinal numbers
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        ordinal = "1st"
    elif number == 2:
        ordinal = "2nd"
    elif number == 3:
        ordinal = "3rd"
    else:
        ordinal = str(number) + "th"
    
    print(ordinal)