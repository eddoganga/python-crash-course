#restaurant seating
diner_group = input('How many people are in your diner group? ')
if int(diner_group) > 8:
    print('Apologies, you will have to wait for a table.')
else:
    print('Your table is ready.')