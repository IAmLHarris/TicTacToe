def display_board(p1,p2,p3,p4,p5,p6,p7,p8,p9):
    '''Prints p1 through p9 arguments in order to console'''
    print(f"{p1}|{p2}|{p3}\n-=-=-\n{p4}|{p5}|{p6}\n-=-=-\n{p7}|{p8}|{p9}")

def main():

    d1="1"
    d2="2"
    d3="3"
    d4="4"
    d5="5"
    d6="6"
    d7="7"
    d8="8"
    d9="9"

    display_board(d1,d2,d3,d4,d5,d6,d7,d8,d9)

    user_input("x")

def user_input(player_turn):
    '''Takes first argument and '''

    if player_turn == "x":
        player_choice = input(f"{player_turn}'s turn to choose a square (1-9): ")

    elif player_turn == "o":
        player_choice = input(f"{player_turn}'s turn to choose a square (1-9): ")

    return player_choice

main()