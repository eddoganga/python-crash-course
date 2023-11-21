#dictionries
#simple dictionary
alien_0 = {'color':'green', 'points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['point'] = 5
print(alien_0)

#modifying values in dictionary
alien_0 = {'color':'green'}
print('The alien is ' + alien_0['color'] + '.')

alien_0 = {'color':'yellow'}
print('The alien is ' + alien_0['color'] + '.')

person = {
    'first_name':'bruce',
    'last_name':'wayne',
    'age': 25,
    'city': 'gotham'
}
print(person)

#looping through all value key pair
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("\nValue: " + value)


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python'
    }
for name, languages in favorite_languages.items():
    print(name.title() + ' favorite language is ' + languages.title() + '.')

rivers = {
    'nile':'egypt',
    'tanganyika':'tanzania',
    'niger':'nigeria'
}
for river, country in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title() + '.' )

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

#a list of dictionaries
alien_0 = {'color':'green', 'point':5}
alien_1 = {'color':'red', 'point':25}
alien_2 = {'color':'yellow', 'point':15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#a list in adictionary
#store info about a pizza being ordered
pizza = {
    'crust':'thick',
    'toppings': ['mushrooms', 'extra cheese']
            }
#summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
 print("\t" + topping)

#a dictionary in a dictionary
users = {
    'aeistein': {
        'first':'albert',
        'last': 'eistein',
        'location': 'princeton'
    },
    'mcuire':{
        'first': 'marie',
        'last': 'cuire',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print('\nUsername: ' + username)

pet1 = {
    "kind": "Dog",
    "owner_name": "Alice"
}

pet2 = {
    "kind": "Cat",
    "owner_name": "Bob"
}

pet3 = {
    "kind": "Bird",
    "owner_name": "Charlie"
}

pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"Pet kind: {pet['kind']}")
    print(f"Owner's name: {pet['owner_name']}")



favorite_places = {
    'scott': ['zanzibar', 'st.lucia', 'jamaica'],
    'bruce': ['gotham', 'arkham', 'central city'],
    'mark': ['malindi', 'nakuru', 'busia']
}
for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are: {', '.join(places)}")
