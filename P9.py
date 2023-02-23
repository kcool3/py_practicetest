#33.9 LAB: Output range with increment of 5

#Get input from the user 
num1 = int(input())
num2 = int(input())

#check if num2 is less than num1 
if num2 < num1:
    print("Second integer can't be less than the first")
else:
    #print the first integer
    print(num1, end='')
    #print subsequent increments of 5.
    while num1 + 5 <= num2:
        num1 += 5
        print(num1, end='')

#whitespace/newline issues on this one- 6/10