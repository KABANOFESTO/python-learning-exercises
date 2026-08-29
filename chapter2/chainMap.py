from collections import ChainMap

user_account = {'name': 'Alice', 'age': 30}

user_settings = {'theme': 'dark', 'language': 'en'}

user_preferences = ChainMap(user_account, user_settings)

print(user_preferences['name'])  # Output: Alice
print(user_preferences['theme'])  # Output: dark