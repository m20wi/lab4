#lab4_Q3
import random
secret =random.randint(1,20)
total=0
while True:
    guess=int(input("Guess the number between 1 and 20:"))
    if guess <1 or guess > 20:
        print('Invalid number')
        continue
    total+=1
    if guess==secret:
        print('Correct')
        print('Number of guesses',total)
        break
    elif guess < secret:
        print('Too low')
    else:
        print('Too high')






