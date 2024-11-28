import datetime
import random
import matplotlib.pyplot as plt

arrayRandom = [10000, 20000, 30000, 40000, 50000]
result = []
for m in range(len(arrayRandom)):
    array = [random.randint(0, arrayRandom[m]) for i in range(arrayRandom[m])]
    start = datetime.datetime.now()
    i = 0
    while i < len(array) - 1:
        if array[i] == array[i + 1]:
            array.pop(i + 1)
        else:
            i += 1
    finish = datetime.datetime.now()
    result.append(int(finish.microsecond))
print(result)

plt.plot(arrayRandom, result)
plt.show()
