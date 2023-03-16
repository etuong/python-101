# This is a comment in Python
# Proper use of commenting can make code maintenance much easier and help make finding bugs faster

def print_hello(name):
    print(f'Hello, {name}!')

# This is where top-level code is run
if __name__ == '__main__':
    name = input('What is your name? ')
    print_hello(name)
