import random

def dice_roll(dieCount):
    sumOfRolls = 0
    for x in range(dieCount):
        sumOfRolls = sumOfRolls + random.randint(1,6)
    return sumOfRolls

roll = dice_roll(4)

print(roll)