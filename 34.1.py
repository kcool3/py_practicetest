# Miles per commute for employee a, b, c
a_miles = 15.62 
b_miles = 41.85
c_miles = 32.67
#Read the number of times employee a, b, c travels to the job site
a_travels = int(input())
b_travels = int(input())
c_travels = int(input())

total_miles = a_travels * a_miles + b_travels * b_miles + c_travels * c_miles

#output the result here 

print("Distance: {:.2f} miles".format(total_miles))
