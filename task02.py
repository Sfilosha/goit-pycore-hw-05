import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float]: 
    # Знаходить всі чила із тексту та повертає їх як генератор
    is_number_pattern = r"\d+\.\d+|\d+"
    numbers = re.findall(is_number_pattern, text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable[[str], Generator[float]]) -> float:
    # Рахує сумму знайдених чисел в text, використовуючи генератор
    total = 0
    for number in func(text):
        total += number

    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
