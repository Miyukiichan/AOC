f = open("data.txt", "r")
data = f.readlines()
f.close()

MAX_LEN = 1000
board = [0] * MAX_LEN
for i in range(MAX_LEN):
    board[i] = [0] * MAX_LEN
for d in data:
    points = d.split(" -> ")
    p1 = points[0].split(",")
    x1 = int(p1[0])
    y1 = int(p1[1])
    p2 = points[1].split(",")
    x2 = int(p2[0])
    y2 = int(p2[1])
    if x1 != x2 and y1 != y2: continue
    if x2 < x1 or y2 < y1:
        tmp = x1
        x1 = x2
        x2 = tmp
        tmp = y1
        y1 = y2
        y2 = tmp

    board[x1][y1] += 1
    for i in range(x1 + 1, x2 + 1):
        board[i][y1] += 1
    for i in range(y1 + 1, y2 + 1):
        board[x1][i] += 1
count = 0
for row in board:
    for i in row:
        if i > 1:
            count += 1

print("The answer is: " + str(count))