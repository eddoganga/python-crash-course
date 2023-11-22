#user input and while loops


#how input() function works
message = input('Tell me something and I will repeat it back to you: ')
print(message)

height = input('How tall are you, in inches? ')
height = int(height)

if height >= 36:
    print('\nYou are tall enough to ride!')
else:
    print('\nyou will be able to ride when you are older!')

#rental cars
rental_cars = input('What kind of rental car would you like? ')

print(f'Lemme see if i can find you a {rental_cars.title()}')




#multiples of ten
number = input('Enter a number: ')
if int(number) % 10 == 0:
    print('The number is a mutiple of 10')
else:
    print('Not a multiple of 10')

#while loop
current_number = 1
while current_number < 6:
    print(current_number)
    current_number += 1

#letting users to quit when they want
prompt = '\nTell me something and I will repeat it back to you: '
prompt += "\nEnter 'quit' to end the program."

message = ''
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

#using the flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
 
active = True
while active:
    message = input(prompt)
 
    if message == 'quit':
        active = False
    else:
        print(message)

#using continue loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)





