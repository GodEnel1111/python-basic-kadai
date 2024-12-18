import sys

args = sys.argv
var = int(args[1])

if var%3 == 0:
    if var%5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif var%5 == 0:
    print("Buzz")
else:
    print(var)