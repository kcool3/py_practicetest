#33.7 LAB: Smallest number/Ch5 Branching
num1 = int(input())
num2 = int(input())
num3 = int(input())

#Find the smallest number using conditional statements
if num1 <= num2 and num1 <= num3:
    smallest_num = num1
elif num2 <= num1 and num2 <= num3:
    smallest_num = num2
else:
    smallest_num = num3

#Print the smallest number here
print(smallest_num)