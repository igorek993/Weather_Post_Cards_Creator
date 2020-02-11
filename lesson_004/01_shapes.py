# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# - треугольник

point = sd.get_point(150, 150)


def triangle(point, angle, length):
    for _ in range(3):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw()
        point = v1.end_point
        angle = angle + 120


# - квадрат

def square(point, angle, length):
    for _ in range(4):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw()
        point = v1.end_point
        angle = angle + 90


# - пятиугольник

def pentagon(point, angle, length):
    for _ in range(5):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw()
        point = v1.end_point
        angle = angle + 72


# - шестиугольник

def hexagon(point, angle, length):
    for _ in range(6):
        v1 = sd.get_vector(point, angle, length, 3)
        v1.draw()
        point = v1.end_point
        angle = angle + 60


# зачет первой части

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

def general(point, angle, length):
    v1 = sd.get_vector(point, angle, length, 3)
    v1.draw()
    point = v1.end_point
    angle = angle + ???

# I cant understand how I can make the general function recognise what angle it should add to the primary one(60?72?90??)
# Should I use 'if' somehow or there is another way of doing this? Or maybe I took too many lines of the code?

def triangle_2(point, angle, length):
    for _ in range(3):
        general(point, angle, length)
        angle = angle + 120


triangle_2(sd.get_point(300, 100), 0, 200)



sd.pause()
