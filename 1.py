'''Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8'''

def step_1(a,b):
    if b==1:
        return a
    else:
        return a * step_1(a, b-1)

a= int(input('Введите число: '))
b = int(input('Введите его степень: '))

print(f'Число {a} в степени {b} будет равна {step_1(a,b)}')

