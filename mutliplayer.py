import random
import sys
import time

store=random.randint(1,100)

def names():
	print("")
	print("")
	print_slow("Enter the name of first player ")
	names.name1=input(" ")
	print("")
	print_slow("Enter the name of second player ")
	names.name2=input(" ")
	print("")
	print("")
	player1();

def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.1)

def player1():
	print_slow("Enter Your guess ")
	print(names.name1)
	guess1=int(input(" "))

	if(guess1==store):
		print("               ********************")
		print_slow("           Congo!! You got it ");
		print_slow(names.name1)
		print("")
		print("                *******************")
		
		
	else:
		if(guess1>store):
			print_slow("Guess Lower Buddy")
			print("")
			print("")
		else:
			print_slow("Guess Higher Buddy")
			print("")
			print("")
		player2();

def player2():
	print_slow("Enter Your guess ")
	print(names.name2)
	guess2=int(input("  "))

	if(guess2==store):
		print("               ********************")
		print_slow("           Congo!! You got it ");
		print_slow(names.name2)
		print("")
		print("                *******************")
	else:
		if(guess2>store):
			print_slow("Guess Lower Buddy")
			print("")
			print("")
		else:
			print_slow("Guess Higher Buddy")
			print("")
			print("")
		player1();

print("")
print("")
print_slow("Hi!! I am Anup");
print("")
print("")
print_slow("Rule: Two player is needed for this game. I will guess a number and both the player will get the chance to enter the number I guessed one by one. OK!! ")
print("");
print_slow("Do you want to play the game ");
ans=input("");
print("")

while not(ans=="yes" or ans=="no"):
	print_slow("Do you want to play the game ");
	ans=input("");

if(ans=="yes"):
	names();

else:
	print_slow("Are you sure want to exit: ")
	ans_no=input("");
	print("")
	while not(ans_no=="no" or ans_no=="yes"):
		print_slow("Are you sure want to exit: ")
		ans_no=input("");
		print("")

	if(ans_no=="yes"):
		print_slow("Ok bye!! Visit Again");
		print("");
	else:
		print_slow("Ok then lets start the game");
		print("");
		names();
