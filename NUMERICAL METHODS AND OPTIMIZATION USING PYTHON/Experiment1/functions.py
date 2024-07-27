# Function Definition
def greet(name):
    print("Hello,", name)
# Function Call
greet("Annjan")
# Return Statement
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)
# Default Parameters
def greet(welcome="How are you?"):
    print("Hello,", welcome)

greet()  # Uses default parameter
greet("Annjan")  # Uses passed argument
