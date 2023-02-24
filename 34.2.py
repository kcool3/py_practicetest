number_of_ounces = int(input())

#conversion to tons, pounds and remaining ounces
tons = number_of_ounces // (2000 * 16)
pounds = (number_of_ounces //16) % 2000
remaining_ounces = number_of_ounces % 16

#output printed results

print("Tons: {}\nPounds: {}\nOunces: {}".format(tons, pounds, remaining_ounces))