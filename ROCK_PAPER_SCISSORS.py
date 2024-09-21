import random

print("Welcome to Rock, Paper and Scissors")
print("Type 0 for Rock, 1 for Paper and 2 for Scissors")

rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user=int(input("Enter your choice: "))
comp=random.randint(0,2)
print(f"Computer chose {comp}")

if(user==0 and comp==0):
    print("Draw")
elif(user==0 and comp==1):
    print("You Lose!!")
elif(user==0 and comp==2):
    print("You Win!!")
elif(user==1 and comp==0):
    print("You win!!")
elif(user==2 and comp==1):
    print("You Win!!")
elif(user==1 and comp==1):
    print("Draw")
else:
    print("Invalid input")