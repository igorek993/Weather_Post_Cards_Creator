# -*- coding: utf-8 -*-

# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, limit):
        self.limit = limit
        self.prime_numbers = []
        self.start_point = 2

    def __iter__(self):
        self.prime_numbers = []
        return self

    def __next__(self):
        for number in range(self.start_point, self.limit + 1):
            for prime in self.prime_numbers:
                if number >= self.limit:
                    raise StopIteration()
                if number % prime == 0:
                    break
            else:
                self.prime_numbers.append(number)
                self.start_point = number + 1
                return number


# prime_number_iterator = PrimeNumbers(limit=10000)
# for number in prime_number_iterator:
#     print(number)

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    for number in PrimeNumbers(n):
        yield number


for number in prime_numbers_generator(n=10000):
    print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True

def lucky_number(number):
    amount_of_digits = len(str(number))
    left_even_numbers = [int(x) for x in (str(number)[:(amount_of_digits // 2)])]
    right_even_numbers = [int(x) for x in (str(number)[-(amount_of_digits // 2):])]
    return True if sum(left_even_numbers) == sum(right_even_numbers) else False


# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101

def palindromic_number(number):
    amount_of_digits = len(str(number))
    left_even_numbers = [int(x) for x in (str(number)[:(amount_of_digits // 2)])]
    if not amount_of_digits % 2:
        reversed_right_even_numbers = [int(x) for x in (str(number)[:((amount_of_digits // 2) - 1):-1])]
    else:
        reversed_right_even_numbers = [int(x) for x in (str(number)[:(amount_of_digits // 2):-1])]
    return True if reversed_right_even_numbers == left_even_numbers else False


# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


for number in prime_numbers_generator(n=10000):
    if lucky_number(number):
        print(number)

for number in prime_numbers_generator(n=10000):
    print(number) if palindromic_number(number) else None
