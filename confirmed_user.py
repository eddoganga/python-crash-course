# start with users that need to be verified,
#  and an empty list to hold confirmed users

unconfirmed_users = ['derek', 'edwin', 'brian']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print('Verifying_users: ' + current_users.title())
    confirmed_users.append(current_users)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())