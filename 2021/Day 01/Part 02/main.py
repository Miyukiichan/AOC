f = open('data.txt', 'r')
data = f.readlines()
f.close()
count = 0
for i in range(0, len(data) - 3):
    #First 3 values
    a1 = int(data[i])
    a2 = int(data[i + 1])
    a3 = int(data[i + 2])
    #First 3 values shifted by +1
    b1 = int(data[i + 1])
    b2 = int(data[i + 2])
    b3 = int(data[i + 3])
    #Sums
    a = a1 + a2 + a3
    b = b1 + b2 + b3
    if a < b:
        count+=1
print(count)