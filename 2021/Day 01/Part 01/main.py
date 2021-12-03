f = open('data.txt', 'r')
data = f.readlines()
f.close()
count = 0
for i in range(0, len(data) - 1):
    a = int(data[i])
    b = int(data[i + 1])
    if a < b:
        count+=1
print(count)