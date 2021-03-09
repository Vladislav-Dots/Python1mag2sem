import numpy

days             = int(input("Количество дней = "))
while(True):
    skidka_percent   = int(input("Скидка в % = ")) # от 0 до 100
    if(skidka_percent < 100 and skidka_percent >= 0):
        break
summa_start      = float(input("Сумма в $ = "))
summa_end = summa_start
for day in range(1,days):
    summa_end += 3
summa_end *= (1 - skidka_percent / 100)

print("Прибыль = %.2f", %(summa_end - summa_start))