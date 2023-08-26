# A function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

# function with a parameter
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

# fucntion with multiple parameters
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# Using Keyword arguments
greet_with(location="Nakuru", name="Tom")