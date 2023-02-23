#33.4 LAB: Driving costs

#Input values for miles/gallon and dollars/gallon.
miles_gallon = float(input())
dollars_gallon = float(input())

#Calculate gas cost for 20 miles, 75 miles, and 500 miles.
gas_cost_20_miles = (20 / miles_gallon) * dollars_gallon
gas_cost_75_miles = (75 / miles_gallon) * dollars_gallon
gas_cost_500_miles = (500 / miles_gallon) * dollars_gallon

#Output gas cost
print('{:.2f} {:.2f} {:.2f}'.format(gas_cost_20_miles, gas_cost_75_miles, gas_cost_500_miles))