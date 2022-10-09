
my_name = 'Satoshi'

print(f'Hello my name is {my_name}')

print("Its fleece was white as {}.".format('snow'))

print("HOLLA " * 10)

formatter = '{} {} {} {}'

print(formatter.format(1,2,3,4))

print("Hello \tGood \tSir")

yoyo = """
Hey
Baby
Whats
Going On
"""

print(yoyo)

age = input("How old are you?")

print(f'So youre {age}')

from sys import argv

script, first, second, third = argv

print('This script is called', script)
print('Your first variable is', first)
print('Your second variable is', second)
print('Your third variable is', third)

script, user_name = argv
prompt = '>'

print(f'This {script} is the script, this is username {user_name}')
print(f'Do you like me {user_name}?')
likes = input(prompt)

print(f'So you do like me? {likes}')

from sys import argv
from os.path import exists

script, from_file, to_file = argv

target = open(from_file, 'r')
target2 = open(to_file, 'w')

in_data = target.read()

target2.write(in_data)

target2 = open(to_file, 'r')

readME = target2.read()

print(f'This is your #2 file \n{readME}')

from sys import argv

script, input_file = argv

def read_me(f):
    print(f.read())

def reverse(f):
    f.seek(0)

def print_single_line(line_count, f):
    print(f'This is your line count: {line_count}')
    print(f.readline())

current_file = open(input_file)

read_me(current_file)

reverse(current_file)


current_num = 1
print_single_line(current_num, current_file)

current_num += current_num
print_single_line(current_num, current_file)

current_num += current_num
print_single_line(current_num, current_file)

from re import X


square = lambda num : num ** 2

print(square(2))

mynums = [1,2,3,4,5,6,7,8,9,10]

# Use lambda functions when an anonymous function is required for a short period of time.
print(list(map(lambda num : num ** 2, mynums)))
# The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number.
print(list(filter(lambda num : num%2 == 0, mynums)))

names = ['Sarah', 'Brandon', 'Alyssa']

print(list(map(lambda names:names[0],names)))
# ::-1 prints names backwards
print(list(map(lambda names:names[::-1],names)))

x = 50

def changeGlobal():
    # v Changing global value for X
    global x

    print(x)

    x = 'THIS IS YOUR NEW GLOBAL VALUE for X'

    print(x)

changeGlobal()

print(x)

#Determine the number of upper case letters in a sentence
statement = 'Hey Dude How are YOU doing TODAY?'
letters = []

for letter in statement:
    letters.append(letter)
    
    uppercase = 0
    lowercase = 0
    for upper in letters:
        if upper.isupper() == True:
            uppercase += 1
        else:
            lowercase += 1

print(f'This is the # of upper case letters: {uppercase}')
print(f'This is the # of lower case letters: {lowercase}')

numbers = [1,2,3,-7]

#multiply all numbers in a list
def multiplyList(a):
    result = 1
    for nums in a:
        result *= nums
    print(result)
    
multiplyList(numbers)

#see if a word is spelled the same backwards
def palindrome(word):
    if word == word[::-1]:
        print('TRUE')
    else:
        print('FALSE')

palindrome('TOOTS')

#OBJECT ORIENTED PROGRAMMING OOP


#camel case for classes
class Boardsports():

    def __init__(self):
        print('I Like to Ride Things')

    def goofy_or_regular(self):
        print('I can ride Goofy or Regular stance')



class Surfboard(Boardsports):

    #CLASS OBJECT ATTRIBUTE > Can reference it by using the class name instead of self.purpose like Surfboard.purpose
    purpose = 'To Catch Waves'

    def __init__(self,type,brand):
        #INHERITANCE. I am inheriting the Boardsports class by passing it in as an argument
        Boardsports.__init__(self)

        self.type = type
        self.brand = brand

    #method
    def whappa(self):
        print('WHAAAPPPPPPPAAAAAAA')

#CREATING INSTANCE of SURFBOARD
surfboard_type = Surfboard('Fish', 'Pyzel')

type(surfboard_type)

surfboard_type.whappa()

class Book():
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    #can define len
    def __len__(self):
        return self.pages

    #can define str
    def __str__(self):
        return f'{self.title} by {self.author}'

import math

class Line():
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        a = ((self.coor2[1] - self.coor1[1]**2) + (self.coor2[0] - self.coor1[0]**2))**0.5
        return math.sqrt(a)


class Account():
    
    def __init__(self, owner, balance):
        
        self.owner = owner
        self.balance = balance
    
    def deposit(self,number=0):
        
        self.balance += number
        print(f'Here is your new balance: {self.balance}')
    
    def withdraw(self,number=0):
        
        if self.balance - number < 0:
            print('Not Enough Funds!!!!')
        
        else:
            self.balance -= number
            print(f'Here is your new balance: {self.balance}')

#unittesting

import unittest
#cap.py is another sheet where my code is written that I am wanting to test
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'satoshi nakamoto'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Satoshi Nakamoto')


if __name__ =='__main__':
    unittest.main()
