def print_intro():
    print('Welcome to Tic Tac Toe Game')
    name = input('Please Enter name of Player 1: ')
    player_1 = {'name': name, 'moves': []}
    name = name = input('Please Enter name of Player 2: ')
    player_2 = {'name': name, 'moves': []}
    print('Here are the rules for this game: \n')
    print("Player 1 plays with 'o' and player 2 plays with 'x'")
    print("First player to get either 3 'o' or 3 'x' in a row, column or diagonal wins")
    print("When Prompted, enter the position you want to place the element (numbers on the num pad describe the location)")
    print("Let's start\n\n")
    return [player_1, player_2]


def print_board(board, player_list):
    for pos in range(1,10):
        if pos % 3 == 0:
            print('\n')

        if pos in board:
            if pos in player_list[0]['moves']:
                print('o ')
            else:
                print('x ')
        else:
            print('  ')

def check_win(player_moves):
    win_condition = {
        'row': [('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9')],
        'column': [('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9')],
        'diagonal': [('1', '5', '9'), ('3', '5', '7')]
    }
    win = False
    for key in win_condition:
        condition = win_condition[key]
        for tup in condition:
            for item in tup:
                if item not in player_moves:
                    win = False
                    break
                win = True
    return win


def tic_tac_toe():
    player_list = print_intro()
    win = False
    board = []
    while not win or len(board) != 9:
        for player in player_list:
            player_name = player['name']
            move = input(f'{player_name}, Enter your Move: ')
            board.append(move)
            player['moves'].append(move)
            print_board(board, player_list)
            win = check_win(player['moves'])
            print(player_list)

tic_tac_toe()