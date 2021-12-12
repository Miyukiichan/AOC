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
    board[x1][y1] += 1
    while x1 != x2 or y1 != y2:
        if x2 < x1:
            x1 -= 1
        elif x2 > x1:
            x1 += 1
        if y2 < y1:
            y1 -= 1
        elif y2 > y1:
            y1 += 1
        board[x1][y1] += 1
count = 0
for row in board:
    for i in row:
        if i > 1:
            count += 1

print("The answer is: " + str(count))