f = open("data.txt", "r")
lines = f.readlines()
f.close()
horizontal = 0
depth = 0
for l in lines:
    lSplit = l.split()
    direction = lSplit[0]
    amount = int(lSplit[1])
    if direction == "forward":
        horizontal += amount
    elif direction == "up":
        depth -= amount
    elif direction == "down":
        depth += amount
    else:  
        print("This ain't it chief")
print("Horizontal: " + str(horizontal))
print("Depth: " + str(depth))
print("Total: " + str(horizontal * depth))