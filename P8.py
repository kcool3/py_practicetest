#33.8 LAB: Exact change

#input values
total_change_amount = int(input())

#Coin values given here 
dollars = 100 
quarters = 25
dimes = 10 
nickels = 5
pennies = 1

#Check for negative or zero inputs
if total_change_amount <= 0:
    print('No change')
else:
    #calculate the number of each coin type needed
    num_dollars = total_change_amount // dollars 
    total_change_amount = total_change_amount % dollars

    num_quarters = total_change_amount // quarters
    total_change_amount = total_change_amount % quarters 

    num_dimes = total_change_amount // dimes
    total_change_amount = total_change_amount % dimes

    num_nickels = total_change_amount // nickels
    total_change_amount = total_change_amount % nickels

    num_pennies = total_change_amount // pennies
    total_change_amount = total_change_amount % pennies

    #Print the results here 
if num_dollars > 0:
    if num_dollars == 1:
        print("1 Dollar")
    else:
        print(num_dollars, "Dollars")
if num_quarters > 0:
    if num_quarters == 1:
        print("1 Quarter")
    else:
        print(num_quarters, "Quarters")
if num_dimes > 0:
    if num_dimes == 1:
         print("1 Dime")
    else:
        print(num_dimes, "Dimes")
if num_nickels > 0:
    if num_nickels == 1:
        print("1 Nickel")
    else:
        print(num_nickels, "Nickels")
if num_pennies > 0:
    if num_pennies == 1:
        print("1 Penny")
    else:
        print(num_pennies, "Pennies")