from random import randint

def get_players_choice():
    selecting_choice = True
    player_choice = ""
    while(selecting_choice):
        player_choice = input("Enter rock, paper, scissors ")
        if player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors':
            selecting_choice = False
        else:
            print("You muust enter either rock, paper or scissors")
    
    return player_choice

def get_computer_choice():
    choice_num = randint(1,3)
    if choice_num == 1:
        return 'rock'
    elif choice_num == 2:
        return 'paper'
    elif choice_num == 3:
        return 'scissors'
    else:
        print("get_computer_choice failed")

def compare_hands(player_choice, computer_choice):
    # cw = computer win, pw = player win
    if player_choice == 'rock' and computer_choice == 'paper':
        print(player_choice + " loses to " + computer_choice)
        return 'cw'
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print(player_choice + " defeats " + computer_choice)
        return 'pw'
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print(player_choice + " loses to " + computer_choice)
        return 'cw'
    elif player_choice == 'paper' and computer_choice == 'rock':
        print(player_choice + " defeats " + computer_choice)
        return 'pw'
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print(player_choice + " loses to " + computer_choice)
        return 'cw'
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print(player_choice + " defeats " + computer_choice)
        return 'pw'
    elif player_choice == computer_choice:
        print(player_choice + " draws with " + computer_choice)
        return 'draw'
 
def play_game():

    playing = True
    while(playing):
        player_choice = get_players_choice()
        computer_choice = get_computer_choice()

        print("you picked " + player_choice)
        print("computer picked " + computer_choice)

        result = compare_hands(player_choice, computer_choice)

        valid_choice = False
        while(not valid_choice):
            again = input("Do you want to play again, yes or no ")
            if again == 'yes':
                playing = True
                valid_choice = True
            elif again == 'no':
                playing = False
                valid_choice = True
            else:
                print("Please enter either yes or no")

play_game()