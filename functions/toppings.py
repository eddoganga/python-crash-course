#pizza toppings
prompt  = '\nEnter a pizza topping: '
prompt += "\nEnter 'quit' to end the program."

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print('I will add ' + message + ' topping to the pizza.')