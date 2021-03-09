while(True):
    a = int (input ("Трехзначное число = "))
    if (a > 99 and a < 1000):
        break

a_1 = int (a / 100)
a_2 = int (a / 10) % 10
a_3 = a % 10
print("Новое трехзначеное число = ", (a_3 * 100 + a_2 * 10 + a_1))