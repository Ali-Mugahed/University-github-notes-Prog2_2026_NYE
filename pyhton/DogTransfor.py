print("welcome to iiiiii\n")
print("this is a game to move the dog to the bone\n")
print("you can move the dog by entering the row and column number\n")

kert=[['🦴','🦴','🦴'],['🦴','🦴','🦴'],['🦴','🦴','🦴']]

print(f"{kert[0]}\n{kert[1]}\n{kert[2]}")

print("\n wwwwww 🐶")

position=(input("puiuzh "))

row=int(position[0])
coo=int(position[1])

kert[row-1][coo-1]="🐶"

print("\n susssse \n ")

print(f"{kert[0]}\n{kert[1]}\n{kert[2]}")


