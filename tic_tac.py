from random import shuffle
from colorama import Fore
from colorama import init


game_rows = []
game_over = False
first_user=True
game_users=['','']
game_actions = ['','']
for item in range(1,10):
    game_rows.append(' ')
init()
#print(Fore.RED + "Some red text")

#code starts here

def who_goes_first():
    print("Enter player 1 name")
    game_users[0] = input()
    print("Enter Player 2 name")
    game_users[1] = input()
    guess_list = [' ','O',' ',' ']
    print(guess_list)
    shuffle(guess_list)
    print("Guess the new postion of 'O'")
    guess_input = int(input())-1
    if guess_list[guess_input] == 'O':
        print(guess_list)
        print(f"Correct Guess.{game_users[0]}, you are 'X' and you get the first turn.")
        game_actions[0]='X'
        game_actions[1]='O'
        return True
    else:
        print(guess_list)
        game_actions[0]='O'
        game_actions[1]='X'
        print(f"Incorrect Guess. {game_users[0]}, you are 'O' and you get the second turn.")
        return False

def display_board():
    def color_select(value):
        if value == 'X':
            return Fore.RED+value
        elif value == 'O':
            return Fore.GREEN+value
        else:
            return Fore.WHITE+value


    print(f'\n{color_select(game_rows[0])}|{color_select(game_rows[1])}|{color_select(game_rows[2])}')
    print('-----')
    print(f'{color_select(game_rows[3])}|{color_select(game_rows[4])}|{color_select(game_rows[5])}')
    print('-----')
    print(f'{color_select(game_rows[6])}|{color_select(game_rows[7])}|{color_select(game_rows[8])}')


def check_for_win(user1,username):
            is_winner = False 
            if user1 == 0:
                if (game_rows[4] == game_rows[8] == game_rows[user1]) or (game_rows[user1] == game_rows[3] == game_rows[6]) or (game_rows[user1] == game_rows[1] == game_rows[2]):
                    is_winner = True
                    print(f'\nYipeeeeeeee..... {username} you are the winner .....')
            elif user1 == 2:
                if (game_rows[0] == game_rows[1] == game_rows[user1]) or (game_rows[user1] == game_rows[4] == game_rows[6]) or (game_rows[user1] == game_rows[5] == game_rows[8]):
                    is_winner = True
                    print(f'\nYipeeeeeeee..... {username} you are the winner .....')
            elif user1 == 6:
                if (game_rows[0] == game_rows[3] == game_rows[user1]) or (game_rows[user1] == game_rows[7] == game_rows[8]) or (game_rows[user1] == game_rows[4] == game_rows[2]):
                    is_winner = True
                    print(f'\nYipeeeeeeee..... {username} you are the winner .....')
            elif user1 == 8:
                if (game_rows[0] == game_rows[4] == game_rows[user1]) or (game_rows[user1] == game_rows[7] == game_rows[6]) or (game_rows[user1] == game_rows[5] == game_rows[2]):
                    is_winner = True
                    print(f'\nYipeeeeeeee..... {username} you are the winner .....')
            elif user1 == 1:
                if (game_rows[0] == game_rows[2] == game_rows[user1]) or (game_rows[user1] == game_rows[4] == game_rows[7]):
                    is_winner = True
                    print(f'\nYipeeeeeeee..... {username} you are the winner .....')
            elif user1 == 3:
                if (game_rows[4] == game_rows[5] == game_rows[user1]) or (game_rows[user1] == game_rows[0] == game_rows[6]):
                    is_winner = True
                    print(f'\nYipeeeeeeee..... {username} you are the winner .....')
            elif user1 == 5:
                if (game_rows[3] == game_rows[4] == game_rows[user1]) or (game_rows[user1] == game_rows[4] == game_rows[8]):
                    is_winner = True
                    print(f'\nYipeeeeeeee..... {username} you are the winner .....')
            elif user1 == 7:
                if (game_rows[1] == game_rows[4] == game_rows[user1]) or (game_rows[user1] == game_rows[6] == game_rows[8]):
                    is_winner = True
                    print(f'\nYipeeeeeeee..... {username} you are the winner .....')
            else:
                if (game_rows[0] == game_rows[8] == game_rows[user1]) or (game_rows[user1] == game_rows[2] == game_rows[6]) or (game_rows[user1] == game_rows[1] == game_rows[7]) or (game_rows[user1] == game_rows[3] == game_rows[5]):
                    is_winner = True
                    print(f'\nYipeeeeeeee..... {username} you are the winner .....')      

            return is_winner


def player_action():
    # ask for user1  to try
    global first_user, game_over, game_rows, game_actions
    username=''
    if ' ' in game_rows and game_rows.count(' ')>1:
        if first_user:
            print(f'\n{game_users[0]} is your turn')
            username = game_users[0]
        else:
            print(f'\n{game_users[1]} is your turn')  
            username = game_users[1] 
        
        user1 = (int(input()))-1
        #update the board if the move is possible
        if game_rows[user1] == ' ':
            if first_user:
                game_rows[user1] = game_actions[0]                
            else:
                game_rows[user1] = game_actions[1]                        
            #check if there is win 
            is_winner = check_for_win(user1,username)                              
            first_user = not first_user 
            if is_winner:
                game_over = True    
        else:
            print("Block is already filled, try again with a different block")
            player_action()     
    else:
         print("\nIt is a draw !!")
         game_over=True

    return game_over
    

while game_over == False:
    #ask user for the choice between X and O
    first_user=who_goes_first()
    print("\nLet the game begin ........")
    #display current board
    display_board() 
    while game_over == False:
        # ask for user1  to try
        game_over = player_action()
        display_board()

    # check for continue of board
    print("\n Press 'Y' to play again and other button to exit.")
    play_again = input()
    if play_again == 'Y':
        game_over=False
        game_rows = []
        game_over = False
        first_user=True
        game_users=['','']
        game_actions = ['','']
        for item in range(1,10):
            game_rows.append(' ')
    else:
        game_over=True 

print("\n***** Thank you for playing the game *****")
exit(1)

