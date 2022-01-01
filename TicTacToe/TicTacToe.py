gridDict = {7: (0, 0), 8: (0, 1), 9: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            1: (2, 0), 2: (2, 1), 3: (2, 2)}
def menu():
    global grid, turn
    with open('menu.txt') as menuGrid:
        print(menuGrid.read())
    if firstTime:
        ask_play()
    if isRunning:
        grid = [' '*3]*3
        turn = 0
        ask_character()

def ask_play():
    global isRunning, firstTime, gameState, grid
    answer = input('Yes or No to play: ')
    if not answer in 'YesNo':
        ask_play()
    if answer == 'No':
        isRunning = False
    else:
        firstTime, gameState = 0, 1
        grid = [' ' * 3] * 3


def ask_character():
    global p1,p2
    print('Select Key to Choose Character')
    print('Character Cannot be Number')
    p1 = input('Player 1: ')
    p2 = input('Player 2: ')
    if p1.isdigit() or p2.isdigit() or len(p1)+len(p2) > 2:
        ask_character()


def play():
    gridPrint()
    keyInput()
    update()
    print('\n' * 5)

def gridPrint():
    print(' '+grid[0][0]+' | '+grid[0][1]+' | '+grid[0][2])
    print('-'*3+'|'+'-'*3+'|'+'-'*3)
    print(' '+grid[1][0]+' | '+grid[1][1]+' | '+grid[1][2])
    print('-'*3+'|'+'-'*3+'|'+'-'*3)
    print(' '+grid[2][0]+' | '+grid[2][1]+' | '+grid[2][2])


def keyInput():
    global pos, x, y
    pos = input(f'Move Player {turn+1}: ')
    if pos.isdigit() and len(pos)==1:
        if pos != 0:
            y, x = gridDict[int(pos)]
            if grid[y][x] != ' ':
                keyInput()
        else:
            keyInput()
    else:
        keyInput()


def update():
    global grid, gameState, turn
    grid[y] = grid[y][:x] + (not turn) * p1 + turn * p2 + grid[y][x + 1:]
    if wincheck() or tie_check():
        gameState = 2
    else:
        turn = not turn

def wincheck():
    string = ((not turn) * p1 + turn * p2)*3
    for i in range(3):
        if grid[i] == string:
            return True
        if grid[0][i]+grid[1][i]+grid[2][i] == string:
            return True
    if grid[0][0]+grid[1][1]+grid[2][2] == string or grid[2][0]+grid[1][1]+grid[0][2] == string:
        return True
    return False


def tie_check():
    for i in grid:
        for f in i:
            if f ==' ':
                return False
    return True


def congrats():
    gridPrint()
    if wincheck():
        print(f'Congo Rats Player {turn + 1}')
    else:
        print(f'Congo Rats, its A Tie >_<')
    ask_play()


def main():
    global isRunning, gameState, firstTime
    isRunning, gameState, firstTime = True, 0,1
    while isRunning:
        if gameState == 0:
            menu()
        elif gameState == 1:
            play()
        elif gameState == 2:
            congrats()

if __name__ == '__main__':
    main()