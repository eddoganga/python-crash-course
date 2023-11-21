name = 'bruce'
print('Hello ' + name.title() + ', would you like to learn some Python today? ')
print('Hello ' + name.lower() + ', would you like to learn some Python today? ')
print('Hello ' + name.upper() + ', would you like to learn some Python today? ')

print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJava")

favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())


#famous qoute
print('David Starr once said, "Wisdom is knowing what to do next, skill is knowing how to do it, and virtue is doing it." ')

#famous_quote2
famous_person = 'Albert Eisten'
message = '"A person who never made a mistake never tried anything new"'
print(famous_person + 'once said, ' + message)

#whitespace characters
name = "\t \n   Bruce Wayne   \t\n"

# Printing the name with whitespace around it
print("Name with whitespace around it:")
print(f"---{name}---")

# Using stripping functions
print("\nStripping whitespace:")
print(f"Left stripped: ---{name.lstrip()}---")
print(f"Right stripped: ---{name.rstrip()}---")
print(f"Stripped from both sides: ---{name.strip()}---")
