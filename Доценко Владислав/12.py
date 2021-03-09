# Вычислите значение выражения
import numpy as np

x = 3.6

print("Ответ: %3.4f" % (np.exp(x - 2) + abs(np.sin(x)) - x ** 4 * np.cos(1 / x)))
