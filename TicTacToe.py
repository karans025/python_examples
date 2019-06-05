def print_intro():
    print('Welcome to Tic Tac Toe Game\n')
    name = input('\nPlease Enter name of Player 1: ')
    player_1 = {'name': name, 'moves': []}
    name = name = input('\nPlease Enter name of Player 2: ')
    player_2 = {'name': name, 'moves': []}
    print('\n\nHere are the rules for this game: \n')
    print("1. Player 1 plays with 'o' and player 2 plays with 'x'")
    print("2. First player to get either 3 'o' or 3 'x' in a row, column or diagonal wins")
    print("3. When Prompted, enter the position you want to place the element (numbers on the num pad describe the location)")
    #print("4. Enter in 'q' or 'quit' at any time to exit")
    print("\n\nLet's start\n\n")
    return [player_1, player_2]


def print_board(board, player_list):
    for pos in range(0,9):
        if pos % 3 == 0 and pos != 0:
            print('')

        board_pos = (9 - (pos // 3) * 3) - (2 - pos % 3)

        if board_pos in board:
            if board_pos in player_list[0]['moves']:
                print('o ', end = '')
            else:
                print('x ', end = '')
        else:
            print('  ', end = '')
    print('')

def check_win(player_moves):
    win_condition = {
        'row': [(1, 2, 3), (4, 5, 6), (7, 8, 9)],
        'column': [(1, 4, 7), (2, 5, 8), (3, 6, 9)],
        'diagonal': [(1, 5, 9), (3, 5, 7)]
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
            if win:
                return True
    return False


def tic_tac_toe(player_list):
    win = False
    board = []
    while not win and len(board) < 9:
        for player in player_list:
            player_name = player['name']
            if player_name == player_list[0]['name'] and len(player['moves']) > len(player_list[1]['moves']):
                continue
            try:
                move = int(input(f'{player_name}, Enter your Move: '))
                if move < 1 or move > 9:
                    print('Please Enter a value between 1 and 9')
                    break
                if move in board:
                    print('A marker already exists at the position, please Enter another position')
                    break
                board.append(move)
                player['moves'].append(move)
            except:
                print('Please enter a valid numeric value')
                break
            print_board(board, player_list)
            win = check_win(player['moves'])
            if win:
                print(f"Winner: {player['name']}")
                break
            if len(board) >= 9:
                print("This Match was a Draw.")
                break

player_list = print_intro()
while True:
    tic_tac_toe(player_list)
    new_game = input("Want another game? ")
    if(new_game.lower() == 'n' or new_game.lower() == 'no'):
        break
    for player in player_list:
        player['moves'] = []
