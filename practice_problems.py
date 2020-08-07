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


def equal_nums(x, y):
    nums_sum = x + y
    diff = x - y
    diff_two = y - x

    if x == y or nums_sum == 5 or abs(diff == 5) or abs(diff_two == 5):
        return print(True)
    else:
        return print(False)


equal_nums(5, 5)
equal_nums(1, 6)
equal_nums(2, 3)
equal_nums(6, 1)
equal_nums(4, 6)