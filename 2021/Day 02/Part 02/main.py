f = open("data.txt", "r")
lines = f.readlines()
f.close()
horizontal = 0
depth = 0
aim = 0
for l in lines:
    lSplit = l.split()
    direction = lSplit[0]
    amount = int(lSplit[1])
    if direction == "forward":
        horizontal += amount
        depth += (amount * aim)
    elif direction == "up":
        aim -= amount
    elif direction == "down":
        aim += amount
    else:  
        print("This ain't it chief")
print("Horizontal: " + str(horizontal))
print("Depth: " + str(depth))
print("Total: " + str(horizontal * depth))