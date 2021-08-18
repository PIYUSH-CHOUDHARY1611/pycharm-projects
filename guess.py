import random
import sys
print("hello,What's ur name ")
name=input()

print('well,'+name+',I am thinking of a number between 1 and 20,will you guess it? ')
i=int(input("enter 1 to proceed else 0 to extit"))
if i==1:
    scnumber=random.randint(1,20)
    for guesstaken in range(1,7):
        print("Take a Guess")
        guess=int(input())

        if guess < scnumber:
            print("your guess is too low")
        elif guess > scnumber:
            print("your guess is too high")
        else:
            break
    if guess==scnumber:
        print('Good Job,'+name+'! you guesses my Number in'+str(guesstaken)+'\tguesses!')
    else:
        print('Nope,the number I was thinking of was'+str(guesstaken))
else:
    sys.exit(0)