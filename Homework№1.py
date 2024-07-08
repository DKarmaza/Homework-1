"""Завдання №1"""

from datetime import datetime

def days_until_now(date_str):
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d")
        current_date = datetime.today()
        difference = current_date - input_date 
        return difference.days
    except ValueError:
        return "Некоректний запис дати, напишіть у форматі 'РРРР-ММ-ДД'."

date_input = input("Напишіть дату:")
print(days_until_now(date_input))


"""Завдання №2"""

#import random

#def get_numbers_ticket(a, b, c):
#    if a > b:
#        print(f"Число мінімуму ({a}) не може бути більше ніж максимум ({b})")
#        return []
#
#    if c > (b - a + 1):
#        print(f"Кількість потрібних результатів ({c}) перевищує можливий діапазон чисел")
#        return []

#    numbers = set()
#    while len(numbers) < c:
#        numbers.add(random.randint(a, b))
    
#    return sorted(list(numbers))

#a = int(input("Введіть число мінімум: "))
#b = int(input("Введіть число максимум: "))
#c = int(input("Введіть кількість потрібних результатів: "))

#result = get_numbers_ticket(a, b, c)
#print(f"Ваші числа: {result}")