''' CSE 210, W2 Ponder and Prove, "TicTacToe", Liam Harris '''

def display_board(p1,p2,p3,p4,p5,p6,p7,p8,p9):
    '''Prints p1 through p9 arguments in order to console as game board.'''
    print(f"{p1}|{p2}|{p3}\n-=-=-\n{p4}|{p5}|{p6}\n-=-=-\n{p7}|{p8}|{p9}")

def main():
    '''main'''
    player_turn = "x"
    game_state = "playing"


    d1="1"
    d2="2"
    d3="3"
    d4="4"
    d5="5"
    d6="6"
    d7="7"
    d8="8"
    d9="9"

    agree=False
    print()
    print("A game of TicTacToe. If you need to reset the board, both players must type 'reset'.\n")
    while game_state == "playing":

        display_board(d1,d2,d3,d4,d5,d6,d7,d8,d9)
        user_choice = user_input(player_turn)
        if user_choice =="1" and d1 == "1":
            d1=player_turn
        elif user_choice =="2" and d2 == "2":
            d2 =player_turn
        elif user_choice =="3" and d3 == "3":
            d3 =player_turn
        elif user_choice =="4" and d4 == "4":
            d4 =player_turn
        elif user_choice =="5" and d5 == "5":
            d5 =player_turn
        elif user_choice =="6" and d6 == "6":
            d6 =player_turn
        elif user_choice =="7" and d7 == "7":
            d7 =player_turn
        elif user_choice =="8" and d8 == "8":
            d8 =player_turn
        elif user_choice =="9" and d9 == "9":
            d9 =player_turn
        elif user_choice =="reset" and agree==False:
            agree=True
        elif user_choice =="reset" and agree==True:
            d1="1"
            d2="2"
            d3="3"
            d4="4"
            d5="5"
            d6="6"
            d7="7"
            d8="8"
            d9="9"
        else:
            print("Please input a valid number on the board.")
            if player_turn == "x":
                player_turn = "o"
            else:
                player_turn = "x"
        
        board_checked = board_check(d1,d2,d3,d4,d5,d6,d7,d8,d9,player_turn)
        if board_checked == "TicTacToe Found":
            game_state = "winner found"
        else:
            print()
        
        if player_turn == "x":
            player_turn = "o"
        else:
            player_turn = "x"
    if game_state == "winner found":
        if player_turn == "x":
            player_turn = "o"
        else:
            player_turn = "x"
        print(f"Congratulations {player_turn}! You may now gloat.")

        


def user_input(player_turn):
    '''Takes first argument, prints it to console as an input. Asks for a number 1-9. '''
    player_choice = input(f"{player_turn}'s turn to choose a square (1-9): ")

    # if player_turn == "x":
        
    # elif player_turn == "o":
    #     player_choice = input(f"{player_turn}'s turn to choose a square (1-9): ")

    return player_choice

def board_check(c1,c2,c3,c4,c5,c6,c7,c8,c9,player_turn):
    '''Takes 10 arguments, and checks for a line in TicTacToe.'''
    c=None
    check_end=False
    
    

    while check_end == False:
        if player_turn=="x":
            c="xxx"
        elif player_turn=="o":
            c="ooo"

        if c1+c2+c3==c or c4+c5+c6==c or c7+c8+c9==c or c1+c4+c7==c or c2+c5+c8==c or c3+c6+c9==c or c1+c5+c9==c or c7+c5+c3==c:
            check_end = True
            return "TicTacToe Found"
        else:
            check_end = True
            return None
            
        

    

main()