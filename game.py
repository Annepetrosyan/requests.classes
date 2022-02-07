from random import randint
player_score = 0
computer_score = 0

while True:
    player = input("1 for r, 2 for p, 3 for c: ")
    computer = str(randint(1,3))
    
    if player == computer:
        print("tie")
    elif player == "r" and computer == "s" or player == "p" and computer == "r" or player == "s" and computer == "p":
        print("user won")
        player_score += 1
    else:
        print("computer has won")
        computer_score += 1
        
    answer = input("Wanna continue the game? 1 for yes \n")
    if answer != 1:
        break 
        

print(f"User won {player_score} times, computer won {computer_score} times")
