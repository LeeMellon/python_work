"""
write a function that prints the numbers from 1 to n.
but for multiples of three print "Fizz" instead of the number
and ofr the multiples of five print "buzz".
For numbers which are multiples of both print "FizzBuzz"
"""


def fizzbuzz():
    x = int(input("Give me the begining of a range of numbers: "))
    y = int(input("Give me the end of your range: "))
    for i in range(x,y):
        if i % 3 == 0 and i % 5 == 0:                           #have to work backwards
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizzbuzz()





