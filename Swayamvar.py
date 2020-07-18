length = int(input("Enter Length: "))
brides = input("Enter Brides: ")
grooms = input("Enter Grooms: ")

groom_rum = 0
groom_mojito = 0
match = 0

for groom in grooms:
    if groom == "r":
        groom_rum += 1
    else:
        groom_mojito += 1

for bride in brides:
    if bride == "r":
        if groom_rum > 0:
            groom_rum -= 1
            match += 1
        else:
            break
    else:
        if groom_mojito > 0:
            groom_mojito -= 1
            match += 1
        else:
            break

unmatch = length - match
print(unmatch)