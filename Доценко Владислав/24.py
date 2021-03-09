import numpy

days             = int(input("Количество дней = "))
while(True):
    skidka_percent   = int(input("Скидка в % = ")) # от 0 до 100
    if(skidka_percent < 100 and skidka_percent >= 0):
        break
summa            = float(input("Сумма в $ = "))

for day in range(1,days):
    summa += 3
    summa *= (1 - skidka_percent / 100)

print("Итоговая сумма = %f ", summa)