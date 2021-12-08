class Cell:
    def __init__(self, number):
        self.number = number
        self.marked = False

f = open("data.txt", "r")
data = f.readlines()
f.close()

numbers = []
boards = []
board = []
for d in data:
    d = d.rstrip()
    if numbers == []:
        numbers = d.split(',')
        continue
    if d == "":
        if board != []:
            boards.append(board)
        board = []
        continue
    board.append(list(map(lambda x: Cell(x), d.split())))

winners = []
lastNum = 0
bingo = False
for number in numbers:
    for board in list(boards):
        found = False
        for y, row in enumerate(board):
            if found: break
            for x, cell in enumerate(row):
                if cell.number == number:
                    cell.marked = True
                    found = True
                    bingo = True
                    for i in range(5):
                        if not board[y][i].marked:
                            bingo = False
                            break
                    if not bingo:
                        bingo = True
                        for i in range(5):
                            if not board[i][x].marked:
                                bingo = False
                                break   
                    break
                if bingo:
                    break
            if bingo:
                break
        if bingo:
            winners.append(board)
            boards.remove(board)
            lastNum = number
            bingo = False

sum = 0
for row in winners[len(winners) - 1]:
    for cell in row:
        if not cell.marked:
            sum += int(cell.number)

answer = sum * int(lastNum)
print("The score of the winner is: " + str(answer))
