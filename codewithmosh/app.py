""" name = "Ibou KANE"
print("hello", name)

 """
""" 
for number in range(1, 4):
    print("Iteration", number, number * ".")

 """

""" 
def increment(number, by=1):
    return number + by


print(increment(2, 5))
 """

# xargs

""" 
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4))
 """

# xxargs


def save_user(**user):
    print(user["name"])


# save_user(id=1, name="John", age=22)

def fizz_buzz(input):
    result = input
    if input % 3 == 0:
        result = "fizz"

    if input % 5 == 0:
        result = "buzz"

    if (input % 3 == 0) and (input % 5 == 0):
        result = "fizzBuzz"

    return result


print(fizz_buzz(15))
