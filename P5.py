#33.5 LAB: Input and formatted output: Right-facing arrow
#Input character
base_char = input()
head_char = input()

row1 = '      ' + head_char
row2 = base_char * 6 + head_char + head_char
row3 = base_char * 6 + head_char + head_char + head_char

#print output
print(row1)
print(row2)
print(row3)
print(row2)
print(row1)
