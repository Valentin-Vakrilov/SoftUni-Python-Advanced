number_of_usernames = int(input())

unique_usernames = set()

for username in range(number_of_usernames):
    unique_usernames.add(input())

for user in unique_usernames:
    print(user)
