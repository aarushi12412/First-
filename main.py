#Challenge: FizzBuzz Write a Python program that prints the numbers from 1 to 50.
# But for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz".
# For numbers that are multiples of both 3 and 5, print "FizzBuzz".

for i in range (1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)


#Write a Python program that asks the user for a word or phrase and checks if it is a palindrome.
# A palindrome is a word, phrase, or sequence that reads the same forward and backward
# (ignoring spaces, punctuation, and capitalization).

user_input= input("Give me a word ")
#[::-1] reverses strings
if user_input==user_input[::-1]:
    print('this is a palindrome')
else:
    print("this is not a palindrome")

"""Write a Python program that generates a random number between 1 and 100 and lets the user guess it. 
The program should provide hints like "Too high!" or "Too low!" until the user guesses correctly"""

import random
random_number=random.randint(1,101)
print(random_number)
while 1==1:
    guess = input("what is your guess ")
    if int(guess) > random_number:
        print("Too high")
    elif int(guess)<random_number:
        print("Two low")
    elif int(guess)==random_number:
        print("you got it")
        break