"""
Задача E. Капитан Флинт

Капитан Флинт зарыл клад на Острове сокровищ.
Он оставил описание, как найти клад.
Описание состоит из строк вида: "North 5",
где  слово – одно из
"North", "South", "East", "West", – задает направление движения,
а  число – количество шагов, которое необходимо пройти в этом направлении.
Напишите программу, которая по описанию пути к кладу определяет
точные координаты клада, считая, что начало координат находится в начале пути,
ось OX направлена на восток, ось OY – на север.

На вход подается последовательность строк указанного формата. Гарантируется, что числа не превосходят 108.

"""


class Navigator:
    def __init__(self):
        # стартовая позиция
        self.x = 0
        self.y = 0

    def to_north(self, steps):
        self.y += steps

    def to_south(self, steps):
        self.y -= steps

    def to_west(self, steps):
        self.x -= steps

    def to_east(self, steps):
        self.x += steps


navigator = Navigator()

with open("input.txt") as inp:
    for cur_line in inp.readlines():

        direction, steps = cur_line.split(" ")
        steps = int(steps)

        if direction == "North":
            navigator.to_north(steps)

        elif direction == "South":
            navigator.to_south(steps)

        elif direction == "West":
            navigator.to_west(steps)

        elif direction == "East":
            navigator.to_east(steps)

print(f"{navigator.x} {navigator.y}")
