import random


print("welcome to the game")
print("choose a method to toss the coin")


print("1.uuu random.random()")
print("2.uuu random.randint()")


choice = input("enter rhe (1 or 2)\n")



if choice == "1":
	random_n = random.random()
	if random_n >= 0.5:
		computer_r = "heads"
	else:
		computer_r = "tails"

		








elif choice == "2":
	if random.randint(0,1) == 0:
		computer_r = "heads"
	else:
		computer_r = "tails"
		
		
	




else:
	print("nooo")

user_choice = input("enter the (heads or tails):")
if user_choice == computer_r:
	print("you won yee")
else:
	print("iam sorry")
print(f"the coputer {computer_r}")