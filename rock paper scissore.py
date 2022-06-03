from random import randint

player = input("rock(r), paper(p), scissors(s)?")
print(player, "vs", end='')
choosen = randint(1,3)

#print(choosen)

if choosen == 1:
    computer = "r"
elif choosen == 2:
    computer = "p"
else:
    computer = "s"
print(computer)
if player == computer:
    print('DRAW!')

elif player == "r" and computer =="s":
    print("PLAYER WINS")
elif player == "r" and computer == "p":
    print("COMPUTER WINS")

elif player == "p" and computer =="r":
    print("PLAYER WINS")
elif player == "p" and computer == "s":
    print("COMPUTER WINS")

elif player == "s" and computer =="p":
    print("PLAYER WINS")
elif player == "s" and computer == "r":
    print("COMPUTER WINS")

print("thank you for playing")