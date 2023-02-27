# get the 9-digit integer input
num = int(input())

# extract the first, middle, and last parts of the number
first = str(num // 1000000)   # the first three digits
middle = str((num // 10000) % 100)   # the middle two digits
last = str(num % 10000)   # the last four digits

# format the parts with hyphens and concatenate them
id_num = first + '-' + middle + '-' + last

# output the result
print(id_num)