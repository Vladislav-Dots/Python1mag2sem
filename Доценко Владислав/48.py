a = float (input ("Первое число = "))
b = float (input ("Второе число = "))
c = float (input ("Третье число = "))

if (b < c):
    if (a < b):
        print ("Второе и третье число.",b,c, end = " ")
    else:
        print ("Первое и третье число.",a,c, end = " ")
else:
    print ("Первое и второе число.",a,b, end = " ")