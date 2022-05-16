import random

print("#####\n \n A is the user inputted number \n B is the computer generated number \n \n#####\n\n");
print('Type "y" or "yes"  or "Y" to start the game')
a = input("Enter y or Y")
while a == "yes" or a == "Yes" or a == "YES" or a == "y" or a == "Y":
    print("1. stone\n 2. paper\n 3. scissors")
    a = int(input("Enter your choice: "))
    b = random.randint(1,3)
if a == b:
    print("Draw")
elif a == 1 and b == 2:
    print("Computer wins")
elif a == 1 and b == 3:
    print("User wins")
elif a == 2 and b == 1:
    print("Computer wins")
elif a == 2 and b == 3:
    print("Computer wins")      
elif a == 3 and b == 1:
    print("Computer wins")
elif a == 3 and b == 2:
    print("User wins")
elif a > 3 or a < 1:
    print("Invalid input");
else :
    print("Invalid input");
print("game over")            

