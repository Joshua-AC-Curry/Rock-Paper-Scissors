from random import randint

def get_players_choice(liz_spoc = False):
    selecting_choice = True
    player_choice = ""
    if(liz_spoc):
        while(selecting_choice):
            player_choice = input("Enter rock, paper, scissors, lizard, spock ")
            if player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors' or player_choice == 'lizard' or player_choice == 'spock':
                selecting_choice = False
            else:
                print("You muust enter either rock, paper or scissors")
    else:   
        while(selecting_choice):
            player_choice = input("Enter rock, paper, scissors ")
            if player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors':
                selecting_choice = False
            else:
                print("You muust enter either rock, paper or scissors")
    
    return player_choice

def get_computer_choice(liz_spoc = False):

    if(liz_spoc):
        choice_num = randint(1, 5)
        if choice_num == 1:
            return 'rock'
        elif choice_num == 2:
            return 'paper'
        elif choice_num == 3:
            return 'scissors'
        elif choice_num == 4:
            return 'lizard'
        elif choice_num == 5:
            return 'spock'
        else:
            print("get_computer_choice failed")
    else:
        choice_num = randint(1,3)
        if choice_num == 1:
            return 'rock'
        elif choice_num == 2:
            return 'paper'
        elif choice_num == 3:
            return 'scissors'
        else:
            print("get_computer_choice failed")

def compare_hands(player_choice, computer_choice, liz_spoc=False):
    # cw = computer win, pw = player win
    if(liz_spoc):
        if player_choice == 'rock' and computer_choice == 'paper':

            return 'cw'
        elif player_choice == 'rock' and computer_choice == 'scissors':

            return 'pw'
        elif player_choice == 'paper' and computer_choice == 'scissors':

            return 'cw'
        elif player_choice == 'paper' and computer_choice == 'rock':

            return 'pw'
        elif player_choice == 'scissors' and computer_choice == 'rock':
    
            return 'cw'
        elif player_choice == 'scissors' and computer_choice == 'paper':

            return 'pw'
        elif player_choice == 'rock' and computer_choice == 'spock':

            return 'cw'
        elif player_choice == 'rock' and computer_choice == 'lizard':

            return 'pw'
        elif player_choice == 'paper' and computer_choice == 'lizard':

            return 'cw'
        elif player_choice == 'paper' and computer_choice == 'spock':

            return 'pw'
        elif player_choice == 'scissors' and computer_choice == 'spock':

            return 'cw'
        elif player_choice == 'scissors' and computer_choice == 'lizard':

            return 'pw'
        elif player_choice == 'spock' and computer_choice == 'paper':

            return 'cw'
        elif player_choice == 'spock' and computer_choice == 'rock':

            return 'pw'
        elif player_choice == 'spock' and computer_choice == 'lizard':

            return 'cw'
        elif player_choice == 'spock' and computer_choice == 'scissors':

            return 'pw'
        elif player_choice == 'lizard' and computer_choice == 'rock':

            return 'cw'
        elif player_choice == 'lizard' and computer_choice == 'paper':

            return 'pw'
        elif player_choice == 'lizard' and computer_choice == 'scissors':

            return 'cw'
        elif player_choice == 'lizard' and computer_choice == 'spock':

            return 'pw'
        elif player_choice == computer_choice:

            return 'draw'
        
    else:
        if player_choice == 'rock' and computer_choice == 'paper':

            return 'cw'
        elif player_choice == 'rock' and computer_choice == 'scissors':

            return 'pw'
        elif player_choice == 'paper' and computer_choice == 'scissors':

            return 'cw'
        elif player_choice == 'paper' and computer_choice == 'rock':

            return 'pw'
        elif player_choice == 'scissors' and computer_choice == 'rock':
    
            return 'cw'
        elif player_choice == 'scissors' and computer_choice == 'paper':

            return 'pw'
        elif player_choice == computer_choice:

            return 'draw'

def output_result(player_choice, computer_choice, result):
    if(result == 'cw'):
        print(player_choice + " loses to " + computer_choice)
    elif(result == 'pw'):
        print(player_choice + " defeats " + computer_choice)
    else:
        print(player_choice + " draws with " + computer_choice)

def final_result_screen_multi(player, score):
    if (score == 2):
        print(player + " won")
    elif(score == 1):
        print(player + " tied") 
    elif(score == 0):
        print(player + " lost") 
    else:
        print("error inccorect score")

def output_result_multi(player_choice, first_computer_choice, second_computer_choice, liz_spoc=False):
    player_score = 0
    first_score = 0
    second_score = 0
    
    result = compare_hands(player_choice, first_computer_choice, liz_spoc=liz_spoc)
    if(result == 'pw'):
        player_score += 1
    elif(result == 'cw'):
        first_score += 1
    elif(result == 'draw'):
        player_score += 0
        first_score += 0
    else:
        print("Error: result unknown")
    output_result(player_choice, first_computer_choice, result)

    result = compare_hands(player_choice, second_computer_choice, liz_spoc=liz_spoc)
    if(result == 'pw'):
        player_score += 1
    elif(result == 'cw'):
        second_score += 1
    elif(result == 'draw'):
        player_score += 0
        second_score += 0
    else:
        print("Error: result unknown")
    output_result(player_choice, second_computer_choice, result)

    result = compare_hands(first_computer_choice, second_computer_choice, liz_spoc=liz_spoc)
    if(result == 'pw'):
        first_score += 1
    elif(result == 'cw'):
        second_score += 1
    elif(result == 'draw'):
        first_score += 0
        second_score += 0
    else:
        print("Error: result unknown")
    output_result(first_computer_choice, second_computer_choice, result)

    final_result_screen_multi("player", player_score)
    final_result_screen_multi("first computer", first_score)
    final_result_screen_multi("second computer", second_score)

def play_game():

    playing = True
    again =  False
    second_comp = False
    liz_spoc = False
    prev_choice = ""
    while(playing):
        if(again == 'yes'):
            add_comp_check = False
            while(not add_comp_check):
                add_comp = input("do you want to add an additional player, yes or no ")
                if add_comp == 'yes':
                    add_comp_check = True
                    second_comp = True
                elif add_comp == 'no':
                    add_comp_check = True
                else:
                    print("Please enter yes or no")
        
        spoc_check = True
        while(spoc_check):
            liz = input("do you want to play the lizard spock rules, yes or no ")
            if(liz == 'yes'):
                liz_spoc = True
                spoc_check = False
            elif(liz == 'no'):
                liz_spoc = False
                spoc_check = False

                if(prev_choice == 'lizard' or prev_choice =='spock'):
                    print("You must play with lizard spock if you chose lizard or spock in your previous game")
                    liz_spoc = False
                    spoc_check = True
            else:
                print("please enter yes or no ")
        

        if(second_comp):
            print(" ")
            print("adding second player")
            player_choice = get_players_choice(liz_spoc=liz_spoc)
            first_computer_choice = get_computer_choice(liz_spoc=liz_spoc)
            second_computer_choice = prev_choice

            print(" ")

            print("you picked " + player_choice)
            print("first computer picked " + first_computer_choice)
            print("second computer picked " + second_computer_choice)

            print(" ")

            output_result_multi(player_choice, first_computer_choice, second_computer_choice, liz_spoc)

        else:
            player_choice = get_players_choice(liz_spoc=liz_spoc)
            computer_choice = get_computer_choice(liz_spoc=liz_spoc)

            print("you picked " + player_choice)
            print("computer picked " + computer_choice)

            result = compare_hands(player_choice, computer_choice, liz_spoc)

            output_result(player_choice, computer_choice, result)

        valid_choice = False
        while(not valid_choice):
            print(" ")
            again = input("Do you want to play again, yes or no ")
            if again == 'yes':
                playing = True
                valid_choice = True
                prev_choice = player_choice
            elif again == 'no':
                playing = False
                valid_choice = True
            else:
                print("Please enter either yes or no")

play_game()