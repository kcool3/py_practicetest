#solution accepts three integer values representing base and height measurements of a trapezoid
#first and second integers represent base 1 and base 2; third integer represents height 
#solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h

b1 = int(input())
b2 = int(input())
height = int(input())

area = (b1 + b2) / 2 * height

print("Trapezoid area: {:.1f} square meters".format (area))