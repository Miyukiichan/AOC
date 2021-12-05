def filter_list(l, i, lookForMost = True):
    if len(l) < 2: return l
    ones = 0
    zeros = 0
    for line in l:
        if line[i] == '0':
            zeros += 1
        elif line[i] == '1':
            ones += 1
        else:
            print("This ain't it chief")
    # Default value of zero for ease of not checking the opposite condition
    filterNum = "0"
    if ones == zeros:
        if lookForMost:
            filterNum = "1"
    else:
        onesWin = ones > zeros
        if lookForMost == onesWin:
            filterNum = "1"
    l = list(filter(lambda x: x[i] == filterNum, l))
    return l


f = open("data.txt", "r")
oxygen = f.readlines();
f.close()
co2 = oxygen
for i in range(0, 12):
    if len(oxygen) < 2 and len(co2) < 2: break
    oxygen = filter_list(oxygen, i, True)
    co2 = filter_list(co2, i, False)
if len(oxygen) == 0 or len(co2) == 0:
    print("OH NOS")
else:
    oxygen_10 = int(oxygen[0], 2)
    co2_10 = int(co2[0], 2)
    print("Oxygen in binary is: " + oxygen[0])
    print("Oxygen in base 10 is: " + str(oxygen_10))
    print("CO2 in binary is: " + co2[0])
    print("CO2 in base 10 is: ", str(co2_10))
    print("The product is: " + str(oxygen_10 * co2_10))