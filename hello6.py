# Ask user for their name
name = input("what's your name? ")

# Remove whitespace from str and capitalize user's name
name = name.strip().title()

# Say hello to user
print(f"hello, {name}")