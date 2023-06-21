line = "* * * * * * * * * *"

enemyGrid = ["* A * * * * * * * *",
             "* A * * * * * E * *",
             "* A * * * * * * * *",
             "* A * * * * D D * *",
             "* A * * * * * * * *",
             "* * * * * * * * * *",
             "* * B B B B * C * *",
             "* * * * * * * C * *",
             "* * * * * * * C * *",
             "* * * * * * * * * *"]
enemyGridShow = [line for i in range(10)]
myGrid = [line for i in range(10)]


def printGrid(grid1, grid2):
    letter = 'A'
    print(' ', end='  ')
    for i in range(10):
        print(chr(ord(letter)+i), end=' ')
    print()

    for j in range(10):
        print(f"{j+1:>2} {grid1[j]:>3}")

    for _ in range(24):
        print('-', end='')
    print()

    for k in range(10):
        print(f"{k+1:>2} {grid2[k]:>3}")


def coord2Index(coord: str) -> int:
    y = (ord(coord[0])-65)*2
    x = int(coord[1])-1
    return x, y


def replaceStr(s: str, char: str, i: int) -> str:
    return s[:i] + char + s[i + 1:]


def isValid(x: int, y: int, direction: str, ship: str, grid) -> bool:

    valid = True
    shipLength = 70-ord(ship)

    if direction == 'up':
        if (x+1) < shipLength:
            valid = False
        else:
            counter = 0
            while counter < shipLength:
                if grid[x-counter][y] != '*':
                    return False
                counter += 1

            for counter in range(shipLength):
                grid[x-counter] = replaceStr(grid[x-counter], ship, y)

    elif direction == 'down':
        if (10-x) < shipLength:
            valid = False
        else:
            counter = 0
            while counter < shipLength:
                if grid[x+counter][y] != '*':
                    return False

                counter += 1

            for counter in range(shipLength):
                grid[x+counter] = replaceStr(grid[x+counter], ship, y)

    elif direction == 'left':
        if (y+1) < shipLength:
            valid = False
        else:
            counter = 0
            while counter < shipLength:
                if grid[x][y-counter] != '*':
                    return False

                counter += 2

            for counter in range(0, shipLength*2, 2):
                grid[x] = replaceStr(grid[x], ship, y-counter)

    elif direction == 'right':
        if (10-y) < shipLength:
            valid = False
        else:
            counter = 0
            while counter < shipLength:
                if grid[x][y+counter] != '*':
                    return False

                counter += 2

            for counter in range(0, shipLength*2, 2):
                grid[x] = replaceStr(grid[x], ship, y+counter)

    else:
        valid = False

    return valid


def setMyShips():

    global myGrid

    ships = ['A', 'B', 'C', 'D', 'E']   # A = 5, E = 1
    for ship in ships:
        valid = False
        while valid == False:
            coord = input(f"Enter ship {ship} starting coordinate: ")
            [x, y] = coord2Index(coord)

            while x > 20 or y > 10:
                print("***Coordinate invalid!***")
                target = input(f"Enter ship {ship} starting coordinate: ")
                [x, y] = coord2Index(target)

            if ship == 'E':
                direction = 'up'
            else:
                direction = input(
                    f"Enter ship {ship} direction (up/down/left/right): ")
            valid = isValid(x, y, direction, ship, myGrid)
            printGrid(enemyGridShow, myGrid)
            if valid == False:
                print("***Ship position invalid!***")


def shipCount(grid, ship: str) -> int:
    count = 0
    for i in range(10):
        for j in grid[i]:
            if j == ship:
                count += 1
    return count


printGrid(enemyGridShow, myGrid)
setMyShips()
gameOver = False
enemyShips = ['A', 'B', 'C', 'D', 'E']
myShips = ['A', 'B', 'C', 'D', 'E']
while gameOver == False:
    printGrid(enemyGridShow, myGrid)

    target = input("Enter target coordinate: ")
    [x, y] = coord2Index(target)

    while x > 20 or y > 10:
        print("Invalid coordinate")
        target = input("Enter target coordinate: ")
        [x, y] = coord2Index(target)

    if enemyGrid[x][y] == '*' or enemyGridShow[x][y] == 'X':
        print("Shot missed!")
        enemyGridShow[x] = replaceStr(enemyGridShow[x], 'X', y)
    elif enemyGrid[x][y] == 'A':
        print("Hit enemy ship A")
        enemyGrid[x] = replaceStr(enemyGrid[x], 'X', y)
        enemyGridShow[x] = replaceStr(enemyGridShow[x], 'X', y)
    elif enemyGrid[x][y] == 'B':
        print("Hit enemy ship B")
        enemyGrid[x] = replaceStr(enemyGrid[x], 'X', y)
        enemyGridShow[x] = replaceStr(enemyGridShow[x], 'X', y)
    elif enemyGrid[x][y] == 'C':
        print("Hit enemy ship C")
        enemyGrid[x] = replaceStr(enemyGrid[x], 'X', y)
        enemyGridShow[x] = replaceStr(enemyGridShow[x], 'X', y)
    elif enemyGrid[x][y] == 'D':
        print("Hit enemy ship D")
        enemyGrid[x] = replaceStr(enemyGrid[x], 'X', y)
        enemyGridShow[x] = replaceStr(enemyGridShow[x], 'X', y)
    elif enemyGrid[x][y] == 'E':
        print("Hit enemy ship E")
        enemyGrid[x] = replaceStr(enemyGrid[x], 'X', y)
        enemyGridShow[x] = replaceStr(enemyGridShow[x], 'X', y)
    else:
        print("Target invalid!")

    enemyShipsAlt = []
    for i in enemyShips:
        if shipCount(enemyGrid, i) != 0:
            enemyShipsAlt.append(i)
        else:
            print(f'Enemy ship {i} destroyed!')

    enemyShips = []
    enemyShips = enemyShipsAlt

    print(f'Enemy ships left: {len(enemyShips)}')

    if len(enemyShips) == 0:
        gameOver = True
        break

print('Game over!')
