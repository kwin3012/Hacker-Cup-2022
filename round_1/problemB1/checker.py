from random import randint
a = []
a.append(str(1) + "\n")
a.append(str(3000000) + "\n")
for i in range(3000000):
    x = randint(0, 3000)
    y = randint(0, 3000)
    a.append(str(x) + " " + str(y) + "\n")
a.append(str(3000000) + "\n")
for i in range(3000000):
    x = randint(0, 3000)
    y = randint(0, 3000)
    a.append(str(x) + " " + str(y) + "\n")

file1 = open('checker2.txt', 'w')
file1.writelines(a)
file1.close()


