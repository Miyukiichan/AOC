def goWest(a):
    x -= amount

f = open("data.txt", "r")
data = f.readlines()
f.close()

x = 0
y = 0
direction = 90 #East by default
for line in data:
    command = line[0]
    amount = int(line[1:])
    if command == "L":
        direction = (direction - amount) % 360
    elif command == "R":
        direction = (direction + amount) % 360
    elif command == "N":
        y += amount
    elif command == "S":
        y -= amount
    elif command == "E":
        x += amount
    elif command == "W":
        x -= amount
    elif command == "F":
        if direction == 90:
            x += amount
        elif direction == 180:
            y -= amount
        elif direction == 270:
            x -= amount
        elif direction == 0:
            y += amount

print("X is: " + str(x))
print("Y is: " + str(y))
print("Manhattan is: " + str(abs(x) + abs(y)))