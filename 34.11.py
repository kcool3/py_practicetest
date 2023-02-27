purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

item = input()
quantity = int(input())

if quantity < 10:
    total_cost = purchase[item] * quantity
elif quantity <= 20:
    total_cost = 0.95 * purchase[item] * quantity
else:
    total_cost = 0.9 * purchase[item] * quantity

print(f"{item} ${total_cost:.2f}")
