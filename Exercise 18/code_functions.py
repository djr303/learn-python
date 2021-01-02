def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2 {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2 {arg2}")

def print_one(arg1):
    print(f"agr1: {arg1}")

def print_none():
    print("I got nothin'.")


print_two("Zebbidie", "Nackers"); print_two_again("David", "Sambana"); print_one('First!'); print_none()