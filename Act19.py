import numpy as np

die_sides = int(input("Enter Number Of Sides For Dice (6/12) : "))
die = range(1,die_sides)

num_rolls = int(input("Enter Number of Times you want to roll the dice : "))

results = np.random.choice(die,size = num_rolls,replace = True)
print(results)