e = 0
c = 0
d= 0
for chi in range(200, 300):
    for i in range(2, chi):
        if chi % i == 0:
            e += i

            c = e
            e -= i

        i += 1

    print(chi, c)

            


    chi += 1
# for chi in range(200, 300):
#     for i in range(2, chi):


