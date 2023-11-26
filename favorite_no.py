import json

# favorite_number = int(input('Enter your favorite number: '))

# with open('favorite_number.json', 'w') as file:
#     json.dump(favorite_number, file)

# print("Favorite number has been stored in favorite_number.json.")


def get_favorite_number():
    try:
        with open('favorite_number.json', 'r') as file:
            stored_number = json.load(file)
            return stored_number
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def store_favorite_number(favorite_number):
    with open('favorite_number.json', 'w') as file:
        json.dump(favorite_number, file)

def main():
    stored_number = get_favorite_number()

    if stored_number:
        print(f"I know your favorite number! It's {stored_number}.")
    else:
        favorite_number = int(input("Please enter your favorite number: "))
        store_favorite_number(favorite_number)
        print("Favorite number has been stored.")

if __name__ == "__main__":
    main()