# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import os
import zipfile as zp
from pprint import pprint

file_name = 'voyna-i-mir.txt'


class StatisticCount:

    def count_letters(self, file_name):
        stat = {}
        letters_total = 0
        with open(file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for letter in line:
                    if letter.isalpha():
                        if letter in stat:
                            stat[letter] += 1
                        else:
                            stat[letter] = 1
        print('+---------+----------+\n'
              '|  буква  | частота  |\n'
              '+---------+----------+')
        for key, value in stat.items():
            print(f'|{key:^9}|{value:^10}|')
            letters_total += value
        print('+ --------+----------+\n'
              '|  итого  |{:^10}|\n'
              '+---------+----------+\n'.format(letters_total))


a = StatisticCount()

a.count_letters(file_name)

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
