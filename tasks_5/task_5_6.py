a = [12, 324, 24, 24 ,235, 325, 43, 5,53, 2, 234, 43, 423, 3424, 4]
b = len(a)
i = 0
c = 0
while i < b-1:
    while a[i] > a[i +1 ]:
        c += 1
    i +=1
print(c)
