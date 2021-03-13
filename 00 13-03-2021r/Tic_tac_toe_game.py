def screen_out(array):
    rows = ['A','B','C']
    columns = ['1','2','3']
    for column in columns:
        print(f'\t{column} ',end='')
    print()
    for r in range(len(rows)):
        print(f'{rows[r]}\t', end='')
        for n in range(3):
            print(f'{array[r][n]}\t', end="")
        print()
    return()
def splitter(coordinate):
    coordinates = []
    for i in range(len(coordinate)):
        coordinates.append(coordinate[i])
    return(coordinates)
def translator(list):
    cord_dict = {'A':0,
                 'B':1,
                 'C':2}
    coordinates_numeric = [cord_dict[list[0]],int(list[1])]
    return coordinates_numeric
def win_checkout(array,player):
    for i in range(3):
        if array[i][0] == array[i][1] == array[i][2] == player: #szukanie w poziomie
            return f'The winner is player {player}!'
        elif array[0][i] == array[1][i] == array[2][i] == player: #szukanie w poziomie
            return f'The winner is player {player}!'
    if array[0][0] == array[1][1] == array[2][2] == player or array[0][2] == array[1][1] == array[2][0] == player: #szukanie po skosach
        return f'The winner is player {player}!'
    array_1 = array[0] + array[1] + array[2]
    if array_1.count('-') == 0:
        return f'Draw!'
    else:
        return('game on!')


###################################main program###########################################

tictactoe = [['-','-','-'],
              ['-','-','-'],
              ['-','-','-']]

player_1 = input("Give your coordinate for X: ").capitalize()
p1_choice = translator(splitter(player_1))
tictactoe[p1_choice[0]][p1_choice[1] - 1] = 'X'
screen_out(tictactoe)

player_2 = input("Give your coordinate for O: ").capitalize()
p2_choice = translator(splitter(player_2))
tictactoe[p2_choice[0]][p2_choice[1] - 1] = 'O'
screen_out(tictactoe)


while win_checkout(tictactoe,'X') == 'game on!':
    player_1 = input("Give your coordinate for X: ").capitalize()
    p1_choice = translator(splitter(player_1))
    tictactoe[p1_choice[0]][p1_choice[1]-1] = 'X'
    screen_out(tictactoe)
    status = win_checkout(tictactoe,'X')
    if status == 'game on!':
        player_2 = input("Give your coordinate for O: ").capitalize()
        p2_choice = translator(splitter(player_2))
        tictactoe[p2_choice[0]][p2_choice[1] - 1] = 'O'
        screen_out(tictactoe)
        status = win_checkout(tictactoe,'O')
    else:
        print(f'\n{status}')