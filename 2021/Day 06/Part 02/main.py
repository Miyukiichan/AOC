from collections import Counter
f = open("data.txt", "r")
population = [0] * 9
data = Counter(f.readline().split(",")).items()
for k, v in data:
    population[int(k)] = v
#Just change the range limit
for i in range(256):
    population = population[1:] + population[:1]
    population[6] += population[-1]
print(f"The answer is: {sum(population)}")