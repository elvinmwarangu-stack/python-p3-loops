#!/usr/bin/env python3

def happy_new_year():
    # Print numbers 10 down to 1
    for i in range(10, 0, -1):
        print(i)
    # Final message
    print("Happy New Year!")


def square_integers(int_list):
    # Return a list of squares
    return [i * i for i in int_list]


def fizzbuzz():
    # Loop from 1 to 100
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
