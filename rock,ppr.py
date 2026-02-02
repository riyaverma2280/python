import random
print("In this game, we have following Choices available:")
print("Choose one of the following:")
print("1. Rock")
print("2. Paper")
print("3. scissors")

user=input("Enter your choice (1/2/3):")   
if user=="1":
    a= "rock"
    print("Your choice: rock")
elif user=="2":
    b= "paper"
    print("Your choice: paper")
elif user=="3":
    c= "scissors"
    print("Your choice: scissors")
else:
    print('none')


computer = random.choice(["rock","paper","scissors"])
print("Computer Choice:", computer)


if user==computer:
    print("We have a tie")
    
elif (user=="rock" and computer=="scissors") or (user=="paper" and computer=="rock" ) or (user=="scissors" and computer=="paper"):
    print("user wins")

else:
    print("computer wins")
