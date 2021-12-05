f = open("data.txt", "r")
data = f.readlines();
f.close()
charCount = 12
gamma = ""
epsilon = ""
for i in range(0, charCount):
    ones = 0
    zeros = 0
    for line in data:
        if line[i] == '0':
            zeros += 1
        elif line[i] == '1':
            ones += 1
        else:
            print("This ain't it chief")
    if ones > zeros:
        gamma += "1"
        epsilon += "0"
    elif zeros > ones:
        gamma += "0"
        epsilon += "1"
    else:
        print("Equal numbers do what now?")
gamma10 = int(gamma, 2)
epsilon10 = int(epsilon, 2)
print("Gamma in binary is: " + gamma)
print("Gamma in base 10 is: " + str(gamma10))
print("Epsilon in binary is: " + epsilon)
print("Epsilon in base 10 is: ", str(epsilon10))
print("The product is: " + str(gamma10 * epsilon10))