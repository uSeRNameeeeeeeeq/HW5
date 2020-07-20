import random
v = 0
a = []
for i in range(5):
    b = []
    for j in range(5):
        b.append(random.randint(0, 99))
    a.append(b)
print(a)
e = 1
for i in a:
    for j in i:

        if e < j:
            e = j
            v += 1
            if v > j:
                e = 0

    print(e)