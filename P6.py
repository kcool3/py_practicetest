#33.6 LAB: Phone number breakdown
#Given an integer representing a 10-digit phone number, output the area code, prefix, and line number using the format (800) 555-1212.
# Ch4 Types

phone_number = int(input())
# Code goes below
#Get area code, prefix, and line number from the phone number.

area_code = phone_number // 10000000
prefix = (phone_number // 10000) % 1000
line_number = phone_number % 10000

#Output formatted as phone number
print('({}) {}-{}'.format(area_code, prefix, line_number))