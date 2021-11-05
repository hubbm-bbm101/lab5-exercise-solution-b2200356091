import random
number = random.randint(1,100)
print("the number is between 1 and 100.")
quess = 0
while quess != number:
    quess = int(input("enter your quess:"))
    if quess>number:
        print("decrease your number ")
    elif quess<number:
        print("increase your number")

print("Correct! ,the number was: " + str(number))
