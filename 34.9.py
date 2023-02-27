temp = int(input())

if temp < 33:
    state = "Frozen"
    safety_comment = "Watch out for ice!"
elif temp <= 80:
    state = "Cold"
elif temp <= 115:
    state = "Warm"
elif temp <= 211:
    state = "Hot"
else:
    state = "Boiling"

if temp == 212:
    safety_comment = "Caution: Hot!"
else:
    safety_comment = ""

print(state)
if safety_comment:
    print(safety_comment)


    #4/5 
