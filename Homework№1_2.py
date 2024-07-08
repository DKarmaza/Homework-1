"""Завдання №2"""

import random

def get_numbers_ticket(a, b, c):
    if a > b:
        print(f"Число мінімуму ({a}) не може бути більше ніж максимум ({b})")
        return []

    if c > (b - a + 1):
        print(f"Кількість потрібних результатів ({c}) перевищує можливий діапазон чисел")
        return []

    numbers = set()
    while len(numbers) < c:
        numbers.add(random.randint(a, b))
    
    return sorted(list(numbers))

a = int(input("Введіть число мінімум: "))
b = int(input("Введіть число максимум: "))
c = int(input("Введіть кількість потрібних результатів: "))

result = get_numbers_ticket(a, b, c)
print(f"Ваші числа: {result}")