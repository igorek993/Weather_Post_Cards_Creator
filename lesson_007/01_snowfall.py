# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, number):
        self.number = number  # TODO Нигде не используется, более того, при добавлении новых снежинок номера перестают
                              #  быть уникальными. Тогда вопрос - зачем этот атрибут нужен?
        self.x = [sd.random_number(0, sd.resolution[0])]
        self.y = [sd.random_number(sd.resolution[1], sd.resolution[1] * 2)]
        self.flake_length = [sd.random_number(20, 50)]  # TODO Повторяться в классе снежинка, что этот параметр
                                                        #  относится к снежинке, избыточно. Просто length достаточно
        # TODO Это класс снежинки. У снежинки какие параметры? Координаты и размер. Ей достаточно одного икс, одного
        #  игрек и одного размера. Тогда зачем же тут списки? Они вам мешают, и вы с ними "боретесь" используя
        #  индексацию, циклы с zip, но сохраняете списки :)

    def clear_previous_picture(self):
        sd.start_drawing()  # TODO Это должно быть до главного цикла по снежинками в основном коде

        for x, y, length in zip(self.x, self.y, self.flake_length):
            # TODO На деле всё значительно проще, цикл тут не нужен
            sd.snowflake(sd.get_point(x, y), length, color=sd.background_color)

    def move(self):
        self.x[0] += sd.random_number(-15, 15)
        self.y[0] -= sd.random_number(4, 30)

    def draw(self):
        for x, y, length in zip(self.x, self.y, self.flake_length):
            # TODO На деле всё значительно проще, цикл тут не нужен
            sd.snowflake(sd.get_point(x, y), length, color=sd.COLOR_WHITE)
        sd.finish_drawing()  # TODO Это должно быть после главного цикла по снежинками в основном коде

    def can_fall(self):
        if self.y[0] <= self.flake_length[0]:
            # TODO Просто поставьте условие в return
            return True


#
# flake = Snowflake(1)
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

def get_flakes(count):
    flakes = []
    for number in range(count):
        flakes.append(Snowflake(number=number))
    return flakes


def get_fallen_flakes():
    global flakes
    count = 0
    for flake in flakes:
        if flake.y[0] <= 0:  # TODO Примените готовый метод объекта снежинка can_fall
            count += 1
    return count


def append_flakes(count):
    global flakes
    for number in range(count):
        flakes.append(Snowflake(number=number))


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=20)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
