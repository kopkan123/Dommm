# Напишите программу,
# которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def Vozvod(a, b):
    if b == 0:
        return 1
    return a * Vozvod(a, b - 1)

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(Vozvod(a, b))