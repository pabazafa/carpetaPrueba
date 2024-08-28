# Ask user for their name, remove whitespace and capitalize user's name.
# name = input("What's your name? ").strip().title()

# Split user's name into first and last name
# first, last = name.split(" ")
# Say hello to user
# print(f"Hello {first}!")

def main():
    name = input("What's your name? ")
    hello(name)

def hello(name):
    print(f"Hello, {name}")

main()

