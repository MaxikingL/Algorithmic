def greet(name):
    print("Hello, "+name+"!")
    greet2(name)
    print("Preparing for say good bye...")
    bye()

def greet2(name):
    print("How are you, "+name+"?")

def bye():
    print("OK, Hi Hello")


greet('Milej')
