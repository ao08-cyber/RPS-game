import random
player_score=0
computer_score=0
ties=0
choices=["rock","paper","scissors"]
while True:
    player=input("Rock, Paper, Scissors (or quit): ").lower()
    if player=="quit":
        break
    if player not in choices:
        print("Invalid choice!")
        continue
    computer=random.choice(choices)
    print("You:",player)
    print("Computer:",computer)
    if player==computer:
        print("Tie!")
        ties+=1
    elif (player=="rock" and computer=="scissors") or (player=="paper" and computer=="rock") or (player=="scissors" and computer=="paper"):
        print("You win!")
        player_score+=1
    else:
        print("Computer wins!")
        computer_score+=1
    print("Player:",player_score)
    print("Computer:",computer_score)
    print("Ties:",ties)
print("Final Score")
print("Player:",player_score)
print("Computer:",computer_score)
print("Ties:",ties)