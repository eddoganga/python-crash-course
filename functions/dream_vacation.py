responses = {}

polling_active = True

while polling_active:
    name = input('What is your name? ')
    response = input('If you could visit one place in the world, where would you go? ')

    # store the response in a dictionary
    responses[name] = response

    repeat = input('Would you like another person to respond? (yes or no) ')
    if repeat == 'no':
        polling_active = False

#polling is complete
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name.title() + ' would like to visit ' + response.title() + '.')