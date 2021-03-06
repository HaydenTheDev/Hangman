from math import pi

"""This calculates the area of a circle."""
# r = float(input("Enter the radius for the circle here: "))
#
# print("The area of the circle with a radius of " + str(r) + " is " + str(pi * r**2))


"""Input name and print it reversed with a space in between"""
#
# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")
#
# print(last_name + " " + first_name)

"""Create an input with 5 comma separated number and make them into a list and
# a tuple."""
# values = input("Please input 4 values separated by commas: ")
#
# list = values.split(',')
# tuple = tuple(list)
#
# print('List : ', list)
# print('Tuple : ', tuple)

"""Write a Python program to accept a filename
from the user and print the extension of that"""
#
# filename = input("Please enter the filename that you want: ")
#
# file_ext = filename.split(".")
#
# print("The extension of the file is " + repr(file_ext[-1]))


"""Write a Python program to display the
first and last colors from the following list."""
#
# f_name = input("Please enter your first name: ")
# l_name = input("Please enter your last name: ")
#
# print(l_name + " " + f_name)


"""Write a Python program to
display the examination schedule.
(extract the date from exam_st_date)"""
#
# exam_st_date = (11, 12, 2014)
#
#
# print("The examination will start from: %i/%i/%i"%exam_st_date)


"""Write a Python program that accepts an integer (n) and
 computes the value of n+nn+nnn."""
#
# n = int(input("Enter a number: "))
#
# n1 = int("%s" % n)
# n2 = int("%s%s" % (n, n))
# n3 = int("%s%s%s" % (n, n, n))
#
# calculate = n1 + n2 + n3
# print(calculate)


"""Write a Python program to print the documents (syntax, description
 etc.) of Python built-in function(s)."""
#
# print(abs.__doc__)
# print(repr.__doc__)
# print(next.__doc__)

"""Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module."""
#
# import calendar
#
# y = int(input("Enter the year like ex. 1995: "))
# m = int(input("Enter the month like ex. 5: "))
#
# print(calendar.month(y, m))

"""Write a Python program to print the following here document."""

# its a doc string like above.

"""Write a Python program to calculate number of days between two dates."""
# import datetime
#
# date_one = datetime.date(1995, 5, 6)
# date_two = datetime.date(2020, 8, 4)
#
# difference = date_two - date_one
#
# print(difference)

"""Write a Python program to get the volume of a sphere with radius 6."""
# import math
#
# radius = float(input("Enter the radius of the sphere: "))
#
# cube = math.pow(radius, 3)
#
# volume = float(4/3)*pi*cube
# print("The volume of the this sphere is: {}".format(volume))

"""Write a Python program to get the difference between a given number and 17,
 if the number is greater than 17 return double the absolute difference. """
#
# number_one = int(input("Enter a number: "))
#
# difference = abs(number_one - 17)
#
# if number_one > 17:
#     print(difference * 2)
# else:
#     print("nevermind")

"""Write a Python program to test whether a number
 is within 100 of 1000 or 2000."""
#
# answer = int(input("enter an number close to 1000 or 2000: "))
#
#
# def near_thousand(n):
#     return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)
#
#
# print(near_thousand(answer))

"""Write a Python program to calculate the sum of three given numbers,
 if the values are equal then return three times of their sum. """

# number_1 = float(input("Please enter the first number: "))
# number_2 = float(input("Please enter the second number: "))
# number_3 = float(input("Please enter the third number: "))
#
# number_sum = number_1 + number_2 + number_3
#
# if number_1 == number_2 == number_3:
#     print("These numbers cubed is : {}".format(number_sum ** 3))
# else:
#     print("The sum of these numbers is: {}".format(number_sum))

"""Write a Python program to get a new string from a given string where 
"Is" has been added to the front. If the given string already begins with 
"Is" then return the string unchanged."""

# def new_string(str):
#     if len(str) >= 2 and str[:2] == "Is":
#         return str
#     return "Is" + str
#
#
# print(new_string("array"))
# print(new_string("Isarray"))

"""Write a Python program to get a string which
 is n (non-negative integer) copies of a given string."""

# def greater_string(str, n):
#     result = ""
#     for i in range(n):
#         result = result + str
#     return result
#
#
# print(greater_string("this is hayden\n", 10))
# print(greater_string("this is Bazor\n", 10))


"""Write a Python program to find whether a given number (accept from
 the user) is even or odd, print out an appropriate message to the user."""

# user_input = int(input("Please enter a even or odd number: "))
#
#
# def odd_even(number):
#     if number % 2 == 0:
#         print("The number you chose is even.")
#     else:
#         print("This number is odd.")
#
#
# odd_even(user_input)


"""Write a Python program to count the number 4 in a given list"""

# def list_count(n):
#     count = 0
#     for number in n:
#         if number == 4:
#             count += 1
#     return print(count)
#
#
# list_count([2, 3, 4, 4, 6, 4])
# list_count([2, 4, 4, 4, 4, 4])


"""Write a Python program to get the n (non-negative integer) 
copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2."""

# def substring_copy(str, n):
#     flen = 2
#     if flen > len(str):
#         flen = len(str)
#     substr = str[:flen]
#
#     result = ""
#     for i in range(n):
#         result = result + substr
#     return result
#
#
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3))

"""Write a Python program to test whether 
a passed letter is a vowel or not. """

# user_input = input("Please enter a letter: ")
#
#
# def vowel_or_not(letter):
#     vowel = "aeiou"
#     if letter in vowel:
#         print("This is a vowel")
#     else:
#         print("This is a consonant")
#
#
# vowel_or_not(user_input)


"""Write a Python program to check whether a 
specified value is contained in a group of values. """

# my_guess = int(input("Please check for a number: "))
#
#
# def numbers(n):
#     if my_guess in n:
#         return print(True)
#     else:
#         return print(False)


# numbers([6, 5, 4, 2, 1, 13, 3])


"""Write a Python program to create a histogram
 from a given list of integers."""

# def histogram(items):
#     for n in items:
#         output = ''
#         times = n
#         while times > 0:
#             output += '$'
#             times = times - 1
#         print(output)
#
#
# histogram([2, 4, 66, 3])


"""Write a Python program to concatenate all elements 
in a list into a string and return it."""

# def concatenate(s):
#     result = ""
#     for words in s:
#         result += str(words)
#     return result
#
#
# print(concatenate(["Hayden ", "Is ", "My ", "Name ", 1995]))


"""Write a Python program to print all even numbers from a given
 numbers list in the same order and stop the printing if any 
 numbers that come after 237 in the sequence."""

# def ordered_numbers(n):
#     for numbers in n:
#         if numbers % 2 == 0:
#             print(numbers)
#         elif numbers == 237:
#             print(numbers)
#             break
#     return
#
#
# print(ordered_numbers([386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#                        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#                        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#                        958, 743, 527]))


"""Write a Python program to print out a set containing all the
 colors from color_list_1 which are not present in color_list_2."""

# list_one = {"Halo", "Fallout", "RocketLeague", "OverWatch", "WarZone", "WoW"}
# list_two = {"Halo", "Fallout", "RocketLeague", "OverWatch"}
#
# print(list_one.difference(list_two))


"""Write a Python program that will accept the base and height of a
 triangle and compute the area."""

# def triangle(b, h):
#     area = (b*h) / 2
#
#     print("The area of the triangle is: {}".format(area))
#
#
# triangle(7, 4)


"""Write a Python program to compute the greatest common
 divisor (GCD) of two positive integers."""

# first_input = int(input("Please enter a positive number: "))
# second_input = int(input("Please enter a positive number: "))
#
#
# def gcd(x, y):
#     _gcd = 1
#
#     if x % y == 0:
#         return y
#
#     for i in range(int(y / 2), 0, -1):
#         if x % i == 0 and y % i == 0:
#             _gcd = i
#             break
#     return _gcd
#
#
# print(gcd(first_input, second_input))


"""Write a Python program to sum of three given integers. 
However, if two values are equal sum will be zero."""

# def sum_numbers(x, y, z):
#     my_sum = 0
#     if x == y or x == z or y == z:
#         print(my_sum)
#     else:
#         print(x + y + z)
#     return my_sum
#
#
# sum_numbers(13, 6, 8)


"""Write a Python program to sum of two given integers.
 However, if the sum is between 15 to 20 it will return 20."""

#
# def two_sum(x, y):
#     my_sum = x + y
#     if 15 <= my_sum <= 20:  # or if my_sum in range(15, 20):
#         return print(20)
#     else:
#         return print(my_sum)
#
#
# two_sum(124125324324235, 12312412412421)


"""Write a Python program that will return true if the two given
 integer values are equal or their sum or difference is 5."""

#
# def equal_nums(x, y):
#     nums_sum = x + y
#     diff = x - y
#     diff_two = y - x
#
#     if x == y or nums_sum == 5 or abs(diff == 5) or abs(diff_two == 5):
#         return print(True)
#     else:
#         return print(False)
#
#
# equal_nums(5, 5)
# equal_nums(1, 6)
# equal_nums(2, 3)
# equal_nums(6, 1)
# equal_nums(4, 6)


"""Write a Python program to add two objects
 if both objects are an integer type."""

#
# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#         raise TypeError("Inputs must be integers")
#     return a + b
#
#
# print(add_numbers(10, 20))


"""Write a Python program to display your details 
like name, age, address in three different lines."""

# name = input("Please enter your name: ")
# age = input("Please enter your age: ")
# address = input("Please enter your address: ")
#
#
# def info(n, a, ad):
#     print("Name: {}\nAge: {}\nAddress: {}".format(n, a, ad))
#     return
#
#
# info(name, age, address)


"""Write a Python program to solve (x + y) * (x + y). """

# def program(x, y):
#     function = ((x + y) * (x + y))
#     print(function)
#
#
# program(4, 3)


"""Write a Python program to compute the future value of a 
specified principal amount, rate of interest, and a number of years."""

# def future_amount(amount, interest, years):
#     rate = float(amount*((1+(0.01*interest)) ** years))
#     print(round(rate))
#
#
# future_amount(10000, 3.5, 7)


"""Write a Python program to check whether a file exists."""

# import os.path
#
# open('name.txt', 'w')
# print(os.path.isfile('name.txt'))


"""Write a Python program to determine whether a Python 
shell is executing in 32bit or 64bit mode on OS?"""

# import struct
# print(struct.calcsize("P") * 8)


"""Write a Python program to get OS name,
platform and release information"""

# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())


"""Write a Python program to locate Python site-packages."""
# import site
# print(site.getsitepackages())


"""Write a Python program to find out the number of CPUs using."""
# import multiprocessing
# print(multiprocessing.cpu_count())


"""Write a Python program to parse a string to Float or Integer."""

# n = "246.2458"
# print(float(n))
# print(int(float(n)))


"""Write a Python program to list all files in a directory in Python."""
# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/Users/power/Downloads') if isfile(join('/Users/power/Downloads', f))]
# print(files_list)


"""Write a Python program to determine profiling of Python programs."""

# import cProfile
# def sum():
#     print(1+2)
# cProfile.run('sum()')

"""Write a Python program to get the current username."""
# import getpass
# print(getpass.getuser())


"""Write a Python to find local IP addresses using Python's stdlib"""
# import socket
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
#     if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
#         s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
#             socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


"""Write a python program to find the sum of the first n positive integers."""
# n = int(input("Input a number: "))
# sum_num = (n * (n + 1)) / 2
# print(sum_num)


"""Write a Python program to convert height
 (in feet and inches) to centimeters."""

# feet_inches = float(input("Enter a number in feet and inches: "))
# original = feet_inches
#
# feet_inches = feet_inches * 30.48
#
# print("{} feet is equal to: {} centimeters.".format(original, feet_inches))


"""Write a Python program to calculate the 
hypotenuse of a right angled triangle."""

# import math
#
# a = float(input("Please enter value one: "))
# val_one = a
# b = float(input("Please enter value two: "))
# val_two = b
# c = math.sqrt((a ** 2) + (b ** 2))
# print("The Hypotenuse of the right angle with values {} and {} is: {}"
#       .format(val_one, val_two, c))


"""Write a Python program to convert the 
distance (in feet) to inches, yards, and miles."""


# feet_input = float(input("Please enter a value for feet: "))
# feet = feet_input
#
# inches = round(feet_input * 12, 2)
# yards = round(feet_input * 0.333333, 2)
# miles = round(feet_input * 0.000189394, 5)
#
#
# print("{} feet is equal to {} inches, {} yards and {} miles."
#       .format(feet, inches, yards, miles))


""""""
# second = 1

# minute = (second * 60)
#
# hour = (minute * 60)
#
# day = (hour * 24)
#
# month = (day * 30)
#
# year = (month * 12)
#
#
# print(" {} seconds in a year\n {}: seconds in a month"
#       "\n {}: seconds in a day\n {}: seconds in a hour\n {}: seconds in a minute\n"
#       .format(year, month, day, hour, minute))


"""Write a Python program to get file creation and modification date/times."""


# import os.path, time
# print("Last modified: %s" % time.ctime(os.path.getmtime("name.txt")))
# print("Created: %s" % time.ctime(os.path.getctime("name.txt")))


"""Write a Python program to convert seconds to day,
 hour, minutes and seconds."""


# time = float(input("Input time in seconds: "))
# day = time // (24 * 3600)
# time = time % (24 * 3600)
# hour = time // 3600
# time %= 3600
# minutes = time // 60
# time %= 60
# seconds = time
# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
# print(hour)


"""Write a Python program to calculate body mass index."""

# #  muscle isn't accounted for so BMI is inaccurate :)
# weight = float(input("Please enter your weight in pounds: "))
# height = float(input("Please enter your height: "))
#
# height_to_inches = (height * 12)
#
# calculate = ((weight / height_to_inches / height_to_inches) * 703)
#
# print("Your BMI is: {}".format(round(calculate, 2)))


"""Write a Python program to convert pressure in kilopascals to pounds
 per square inch, a millimeter of mercury (mmHg) and atmosphere pressure."""


# kilopascals = float(input("Enter a value for kilopascals: "))
#
# psi = round(kilopascals * 0.145, 3)
# mmhg = round(kilopascals * 7.501, 3)
# ap = round(kilopascals / 101, 4)
#
# print("{} KPA = {}: PSI, {}: mmHg, {}: AP".format(kilopascals, psi, mmhg, ap))


"""Write a Python program to calculate the sum of the digits in an integer"""

# num = int(input("Please enter a four digit number:  "))
#
# x = num // 1000
# x1 = (num - x*1000)//100
# x2 = (num - x*1000 - x1*100)//10
# x3 = num - x*1000 - x1*100 - x2*10
# print("The sum of digits in the number is", x+x1+x2+x3)


"""Write a Python program to sort three integers without
 using conditional statements and loops."""

#
# numbers = (input("Please enter digits: "))
#
# my_str = numbers + ""
#
# sorted_numbers = sorted(my_str)
#
# num_1 = sorted_numbers[0]
# num_2 = sorted_numbers[1]
# num_3 = sorted_numbers[2]
# num_4 = sorted_numbers[3]
#
# print(num_1)
# print(num_2)
# print(num_3)
# print(num_4)


"""Write a Python program to sort files by date."""
# import glob
# import os
#
# new_file = open("bobs_burger.txt", 'w')
# new_file.write("This show is alright.")
# new_file.close()
#
#
# files = glob.glob("*.txt")
# files.sort(key=os.path.getmtime)
# print("\n".join(files))


"""Write a Python program to get a directory listing,
 sorted by creation date."""
#
# from stat import S_ISREG, ST_CTIME, ST_MODE
# import os, sys, time
#
#
# dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
#
# data = (os.path.join(dir_path,fn) for fn in os.listdir(dir_path))
# data = ((os.stat(path), path) for path in data)
#
# data = ((stat[ST_CTIME], path) for stat, path in data if S_ISREG(stat[ST_MODE]))
#
# for cdate, path in sorted(data):
#     print(time.ctime(cdate), os.path.basename(path))


"""Write a Python program to get the details of math module."""

#
# import math
#
# math_details = dir(math)
# print(math_details)
#
# print(math.__doc__)


"""Write a Python program to calculate midpoints of a line."""

# x_start = float(input("The first point of the line: "))
# y_start = float(input("The first point of the line: "))
#
# x2_start = float(input("The endpoint of the line: "))
# y2_start = float(input("The endpoint of the line: "))
#
# midpoint = (x_start + x2_start) / 2
# midpoint_2 = (y_start + y2_start) / 2
#
#
# print("The midpoint for x is: {}".format(midpoint))
# print("The midpoint for y is: {}".format(midpoint_2))


"""Write a Python program to hash a word."""

# soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
#
# word=input("Input the word be hashed: ")
#
# word=word.upper()
#
# coded=word[0]
#
# for a in word[1:len(word)]:
#     i = 65-ord(a)
#     coded=coded+str(soundex[i])
# print()
# print("The coded word is: "+coded)
# print()

"""Write a Python program to get the copyright information."""
# import sys
# print("\nPython Copyright Information")
# print(sys.copyright)
# print()


"""Write a Python program to concatenate N strings."""

# colors_list = ["White", "Blue", "Red", "Green", "Grey"]
#
# con_list = '-'.join(colors_list)
# print(con_list)


"""Write a Python program to calculate the sum over a container."""

# container = sum([10, 20, 30])
# print("Sum of the container is:", container)

"""Write a Python program to test whether all numbers of a
 list is greater than a certain number."""
#
#
# numbers_list = [3, 4, 5, 6, 12, 15, 7]
#
# num1 = all(x > 16 for x in numbers_list)
# num2 = all(x > 2 for x in numbers_list)
# print(num1)
# print(num2)


"""Write a Python program to count the number
 occurrence of a specific character in a string."""

#
# my_string = "This is my string for now."
# value = 0
# for char in my_string:
#     if char == 'o':
#         value += 1
#
# print(value)
#
# # other way
#
# my_string = "This is my string for now."
#
# print()
# print(my_string.count("i"))
# print()


"""Write a Python program to get the ASCII value of a character."""

# print()
# print(ord('a'))
# print(ord('A'))
# print(ord('1'))
# print(ord('@'))
# print()


"""Write a Python program to get the size of a file."""

# import os
#
# file_size = os.path.getsize("bobs_burger.txt")
# print("The size of this file is: ", file_size, "Bytes")


"""Given variables x=30 and y=20,
 write a Python program to print t "30+20=50"""

# x = 30
# y = 20
#
# result = y + x
#
# print("{} + {} = {}".format(x, y, result))


"""Given a variable name, if the value is 1, display the string 
"First day of a Month!" and do nothing if the value is not equal."""

# value = 1
#
# if value == 1:
#     print("First day of the Month!")


"""Write a Python program to swap two variables."""

# x = 34
# y = 56
# print("x = {} and y = {}".format(x, y))
# x, y = y, x
# print("x = {} and y = {}".format(x, y))


"""Write a Python program to convert a byte string to a list of integers."""


# x = b'abcgsiodugosugs98w7598237520392ugowih(^&&*^%*&('
# print()
# print(list(x))
# print()


"""Write a Python program to check whether a string is numeric. """


# my_string = "It was very hot outside today."
# my_string_2 = "1995"
#
# is_string = my_string.isnumeric()
# is_string_2 = my_string_2.isnumeric()
#
# print(is_string)
# print(is_string_2)


"""Write a Python program to get the system time."""
# import time
#
# this_time = time.ctime()
# print(this_time)


"""Write a Python program to check if a number
 is positive, negative or zero."""
#
# user_input = int(input("Please enter a number: "))
#
# if user_input == 0:
#     print("This number is zero.")
# elif user_input > 0:
#     print("This number is positive.")
# elif user_input < 0:
#     print("This number is negative.")

"""Write a Python program to get numbers divisible
 by fifteen from a list using an anonymous function."""

#
# num_list = [45, 55, 37, 60, 100, 105, 220]
#
# result = list(filter(lambda x: (x % 15 == 0), num_list))
# print("Numbers divisible by 15 are", result)

"""Write a Python program to remove the first item from a specified list."""

# my_list = ["LoL", "Battlefield", "Halo", "WoW", "Rs"]
#
# del my_list[0]
# print(my_list)

"""Write a Python program to input a number,
 if it is not a number generate an error message."""

# while True:
#     try:
#         user_input = int(input("Please enter a number:  "))
#         break
#     except ValueError:
#         print("This is not a number...Try again.")


"""Write a Python program to filter the positive numbers from a list. """

# numbers_list = [3, 4, 6, -5, 8, -12, -11, 10]
# print("This is the first list of numbers: ", numbers_list)
# new_numbers = list(filter(lambda x: x > 0, numbers_list))
# print("Updated numbers list with only positives: ", new_numbers)


"""Write a Python program to compute the product
 of a list of integers (without using for loop)."""
# from functools import reduce
# numbers_list = [2, 4, 45, 2450]
# numbers_product = reduce((lambda x, y: x * y), numbers_list)
# print("Product of the numbers: ", numbers_product)


"""Write a Python program to display a floating number in specified numbers."""

# order_amount = 212.374
# print('\nThe total order amount comes to %f' % order_amount)
# print('\nThe total order amount comes to %.2f' % order_amount)


"""Write a Python program to format a specified string
 to limit the number of characters to 6."""


# string_amount = "This is a new string."
# print('%.6s' % string_amount) #string only prints 6 characters


"""Write a Python program to determine whether variable is defined or not."""
# success

# try:
#     x = 6
# except NameError:
#     print("This variable is not defined yet.")
# else:
#     print("x has been defined to: ", x)
#
# #  error
# try:
#     y
# except NameError:
#     print("This variable has not been defined yet.")
# else:
#     print("y has been defined.")


"""Write a Python program to empty a variable without destroying it"""


# n = 20
# d = {"x":200}
# l = [1,3,5]
# t= (5,7,8)
# print(type(n)())
# print(type(d)())
# print(type(l)())
# print(type(t)())


"""Write a Python program to determine the 
largest and smallest integers, longs, floats. """


# import sys
# print("Float value information: ", sys.float_info)
# print("\nInteger value information: ", sys.int_info)
# print("\nMaximum value information: ", sys.maxsize)


"""Write a Python program to check whether
 multiple variables have the same value. """


# x = 20
# y = 20
# z = 20
#
# if x == y == z == 20:
#     print("All the values are equal.")


"""Write a Python program to split a variable length string into variables."""


var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z)
var_list = [100, 20.25]
x, y = (var_list + [None] * 2)[:2]
print(x, y)