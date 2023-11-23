class User:

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0  # New attribute for login attempts

    def describe_user(self):
        print(f"User Information for {self.first_name} {self.last_name}:")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Creating instances for different users
user1 = User("Bruce", "Wayne", "batman", "brucewayne@mail.com")
user2 = User("Tony", "Stark", "ironman", "ironman@mail.com")
user3 = User("Emma", "Stone", "emmastone", "emmastone@mail.com")

# Calling methods for each user
user1.describe_user()
user1.greet_user()
print()

user2.describe_user()
user2.greet_user()
print()

user3.describe_user()
user3.greet_user()

# Incrementing login attempts for user1
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Login Attempts for user1: {user1.login_attempts}")

# Resetting login attempts for user1
user1.reset_login_attempts()
print(f"Login Attempts after reset for user1: {user1.login_attempts}")

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            # Add more privileges as needed
        ]

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(privilege)