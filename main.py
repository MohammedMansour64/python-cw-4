def my_name():
    print("My name is fatima")

def my_meal(food , drink):
    print(f"I like to eat {food} and while drinking {drink}")


def cube(number):
    return number ** 3

def byThree(number):
    if number % 3 == 0:
        return cube(3)
    else:
        return "False"




my_name()

my_meal("Pizza" , "Pepsi")

print(byThree(3))
