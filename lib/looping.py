#!/usr/bin/env python3
def happy_new_year():
    # code goes here!
    n = 10
    while n > 0:
        print(n)
        n -= 1
    else: print('Happy New Year!')
def square_integers(int_list):
    # code goes here!
    return [n**2 for n in int_list]

def fizzbuzz():
    # code goes here!
    n = 1
    while n < 101:
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else: print(n)
        n += 1