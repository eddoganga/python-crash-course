bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)


name = ['IG', 'Sergio', 'Yobra', 'Edd']
print(name[0])
print(name[1])
print(name[2])
print(name[3])

message = 'Happy name day ' + name[0] + '.'
print(message)
message = 'Happy name day ' + name[1] + '.'
print(message)
message = 'Happy name day ' + name[2] + '.'
print(message)

cars = ['Audi', 'Toyota', 'Mercedes']
message = 'I would love to own an ' + cars[0]
print(message)

motorcylces = ['Honda', 'Suzuki', 'Yamaha']
print(motorcylces)

#appending elements into the end of a list
motorcylces.append('Ducati')
print(motorcylces)

motorcylces = ['Honda', 'Suzuki', 'Yamaha']
#inserting elements into a list
motorcylces.insert(0, 'Ducati')
print(motorcylces)
#removing an item using del statement
del motorcylces[1]
print(motorcylces)
#removing an item using pop method
pooped_motorcycle = motorcylces.pop()
print(pooped_motorcycle)

guest_list = ['Bruce', 'joker', 'bane']
message = 'Hello ' + guest_list[0].title() + ', welcome to dinner.'
print(message)
message = 'Hello ' + guest_list[1].title() + ', welcome to dinner.'
print(message)
message = 'Hello ' + guest_list[2].title() + ', welcome to dinner.'
print(message)
message = guest_list[1].title() + ' sends his apology for missing dinner.'
print(message)
guest_list[1] = 'Selina'
message = 'Hello ' + guest_list[1].title() + ', welcome to dinner.'
print(message)

#length of a list
cars = ['audi', 'subaru', 'toyota']
print(len(cars))

locations = ['zanzibar', 'london', 'new york', 'ethiopia', 'spain']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
#reverse function
locations.reverse()
print(locations)

magicians = ['carolina', 'david', 'alice']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print('I cant wait to see your next trick, ' + magician.title() + '.\n')
print("Thank you, everyone. That was a great magic show!")

cars = ['audi', 'subaru', 'toyota', 'honda']
for car in cars:
    print('I like ' + car.title() + '.')
print('I really love cars!')

#making numerical list
#range () function
for value in range(1,5):
    print(value)

#using range() to make alist of numbers
numbers = list(range(1,6))
print(numbers)

#even numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

#square of no btwn 1 to 10
squares = []
for value in range(1,11):
    squares.append(value**2) #add a new element at the end of the list
print(squares)

#simple statistics with alist of numbers
digits = [1,2,3,4,5,6,7,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)


for value in range(1,21):
    print(value)

numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))

#odd number
odd_numbers = list(range(1,20,2))
print(odd_numbers)

#cubes btwn 1 to 10

cubes = [value**3 for value in range(1,11)]
print(cubes)

#working with part of a list
#slicing a list
player = ['Jon', 'dan', 'hanna', 'mike']
print(player[0:3])

#looping through a list
players = ['scott', 'stiles', 'lydia', 'derek', 'allison']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

#copying a list
my_foods = ['rice', 'beans', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print('\nMy friends favorite foods are:')
print(friend_foods)
