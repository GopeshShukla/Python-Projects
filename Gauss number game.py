#  I am going to develop a game which will generate a number and player have to gauss it .

import random

target=random.randint(1,100)

while True:
  userChoice=input("\nGuess the value or type QUIT to quit the game.  ")
  if userChoice=="QUIT":
    break
  userChoice=int(userChoice)

  if userChoice==target:
    print("\nsuccess:-correct Guess")
    break

  elif userChoice<target:
    print("\nyour number is small. take a bigger guess.")

  elif userChoice>target:
    print("\nyour number is big. take a smaller guess.")


print("\nTarget Value Was :- ",target)

print("---------------Game Over----------------------")









