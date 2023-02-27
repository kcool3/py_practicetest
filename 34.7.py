# define the predefined list of integers
predef_list = [4, -27, 15, 33, -10]

# get the integer input to compare
num = int(input())

# find the maximum value in predef_list
max_num = max(predef_list)

# compare num with max_num and output the result
if num > max_num:
    print("Greater Than Max? True")
else:
    print("Greater Than Max? False")