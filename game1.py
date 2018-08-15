import random
import sys
import time
store=random.randint(1,100)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def Start_Game():
	print("")
	print("")
	print_slow("What is your name: ")
	name=input("");
	print("")
	print("")
	print_slow("OK Lets play!! ")
	print_slow(name)
	print("");
	
	guess="";
	while not(guess==store):
		print("")
		print("")
		guess=int(input("Enter your guess "));
		print("")
		print("")
		if(guess<store):
			
			print_slow("You are.......")
			time.sleep(1.0);
			print("Wrong");
			print("");
			print("Hint: ")
			print_slow("Guess Higher buddy");
			print("")
			print("");
			
		elif(guess>store):
			
			print_slow("You are.......")
			time.sleep(1.0);
			print("Wrong");
			print("");
			print("Hint: ")
			print_slow("Guess Lower buddy");
			print("");
			print("")
			
		else:
			print("")
			print("")
			print("")
			print("               ********************")
			print_slow("           Congo!! You got it ");
			print_slow(name)
			print("")
			print("                *******************")

print("")
print("")
print_slow("HI!! I AM PROCESSOR.")
print("");
print("")
print("")

print_slow("DO YOU WANT TO PLAY THE GAME: ")
ans = input("").strip();
while not(ans=='yes' or ans=='no'):
	print_slow("DO YOU WANT TO PLAY THE GAME: ")

	ans=input(" ").strip();

if(ans=='yes'):
	Start_Game();
else:
	print("")
	print_slow("Dont waste my time. Fuck off!!");
	print("")