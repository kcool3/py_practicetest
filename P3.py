#33.3 LAB: Convert to dollars
#This is the input for the four values.
quarters = int(input())
dimes = int(input())
nickels = int(input())
pennies = int(input())

#Calculate the total amount in dollars and cents
total_cents = quarters *25 + dimes * 10 + nickels * 5 + pennies
dollars = total_cents // 100
cents = total_cents % 100

#Output total amount
print(f'Amount: ${dollars}.{cents:02d}')

#prints out dollars and cents to two decimal places.