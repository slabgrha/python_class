import random
import sys

dice=[]

# set base set
dice.append(0)
dice.append(1)

# build out dice
# dice[7] = set((1,6), (2,5)...)
for pip_count in range(2,13):
    dice.append(set())
    for pip in range(1,pip_count):
        dice[pip_count].add((pip, pip_count-pip))

# Random number generator
r = random.Random()

# First roll
d1=r.randrange(1,6)
d2=r.randrange(1,6)

print("You rolled [%d][%d] = %d" % (d1, d2, d1+d2))

# Win if first roll is 7 or 11
if (d1, d2) in dice[7] | dice[11]:
    print("You won")
    sys.exit(0)

# Lose if first roll is 2, 3, 12
if (d1, d2) in dice[2] | dice[3] | dice[12]:
    print("You lost")
    sys.exit(0)

# You established the point
point = d1+d2
print("")
print("Your point is: [%d][%d] = %d" % (d1, d2, d1+d2))
print("")

# Loop until we win or lose
while True:
    d1=r.randrange(1,6)
    d2=r.randrange(1,6)

    print("You rolled [%d][%d] = %d" % (d1, d2, d1+d2))

    # Win if we make the point
    if (d1, d2) in dice[point]:
        print("You win!")
        sys.exit(0)
    if (d1, d2) in dice[7]:
        print("You lose!")
        sys.exit(1)
