##Number Guessing: Python beginners can start with number guessing projects that can be exciting and offer a good learning experience.
##The mini-game can include random numbers between 1 to 10, 1 to 100, etc. followed by a hint so that users can guess the right numbers.
##A simple game will include the major forms of numbers including divisible, multiples, and other combinations. 
##
## 


import random
import math
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
x = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")
count = 0
while count < math.log(upper - lower + 1, 2):
	count += 1
	guess = int(input("Guess a number:- "))
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")
if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

##import math
##print(round(math.log(100 - 10 + 1, 2)))

