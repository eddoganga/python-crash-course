sandwich_order = ['chicken sandwich', 'egg sandwich', 'ham sandwich', 'beef sandwich']
finished_sandwiches = []

while sandwich_order:
    current_order = sandwich_order.pop()
    print('I made you a ' + current_order + '.')
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
