def show_magicians(magicians):
    for name in magicians:
        print(name.title())

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]

# List of magician's names
magicians_names = ['sky bri', 'lucy hale', 'scarlet witch', 'adam strange']

# Displaying original list of magicians
print("Original List:")
show_magicians(magicians_names)

# Modifying the list using make_great()
make_great(magicians_names)

# Displaying the modified list of magicians
print("\nModified List:")
show_magicians(magicians_names)


