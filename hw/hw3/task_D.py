"""
Задача D. Древний баскетбольный матч\

за заброшенный со штрафного броска мяч команда получает 1 очко;
за заброшенный с близкой дистанции мяч команда получает 2 очка;
за заброшенный с дальней дистанции мяч команда получает 3 очка.
Известно, что если расстояние до корзины во время броска было не более L,
то дистанция считалась близкой, иначе дальней.

По данным о заброшенных мячах нужно восстановить результат матча.

В первой строке ввода записаны два целых числа
n — количество записей на табличках о заброшенных мячах
L и граница, разделяющая двух и трёхочковые броски.

В следующих n строках содержатся сведения о заброшенных мячах.
Каждая строка содержит два целых числа ti и di
Если di ≥ 0, это означает, что игрок из команды ti забросил мяч с расстояния di.
Если di = -1, это означает, что игрок из команды ti забросил мяч со штрафного броска.

В единственной строке выведите результат матча:
количество очков, набранных первой и второй командой соответственно, через двоеточие.
"""
from algoritms.binary_search import upper_bound


class Team:
    def __init__(self, near_end_distance):
        self._PENALTY_MARKER = -1

        self._PENALTY_POINTS = 1
        self._NEAR_POINTS = 2
        self._FAR_POINTS = 3

        self._near_end = near_end_distance
        self._history = []

    def write_to_history(self, distance) -> None:
        self._history.append(distance)

    def calculate_points_per_game(self) -> int:
        if len(self._history) == 0:
            return 0

        self._history.sort()

        points_for_penalty_bolls = (self._PENALTY_POINTS *
                                    self._get_number_penalty_bolls())
        points_for_far_bolls = (self._FAR_POINTS *
                                self._get_number_far_bolls())
        points_for_near_bolls = (self._NEAR_POINTS *
                                 self._get_number_near_bolls())

        point_per_game = (points_for_penalty_bolls +
                          points_for_far_bolls +
                          points_for_near_bolls)
        return point_per_game

    def _get_number_penalty_bolls(self) -> int:
        """кол-во мячей заброшенных со штрафной"""
        upper = upper_bound(self._history, self._PENALTY_MARKER)

        if self._history[upper] == self._PENALTY_MARKER:
            return upper + 1
        else:
            return upper

    def _get_number_near_bolls(self) -> int:
        """кол-во мячей заброшенный в 2-ух очковой зоне"""
        lower = upper_bound(self._history, self._PENALTY_MARKER)
        if self._history[lower] == self._PENALTY_MARKER:
            return 0

        upper = upper_bound(self._history, self._near_end)
        if self._history[upper] <= self._near_end:
            return upper - lower + 1
        else:
            return upper - lower

    def _get_number_far_bolls(self) -> int:
        """кол-во мячей заброшенный в 3-ех очковой зоне"""
        lower = upper_bound(self._history, self._near_end)

        if self._history[lower] <= self._near_end:
            return 0
        else:
            upper = len(self._history) - 1
            return upper - lower + 1


if __name__ == "__main__":
    n, L = [int(i) for i in input().strip().split()]

    team_1 = Team(L)
    team_2 = Team(L)

    for _ in range(n):
        ti, di = [int(i) for i in input().strip().split()]

        if ti == 1:
            team_1.write_to_history(di)
        else:
            team_2.write_to_history(di)

    points_team_1 = team_1.calculate_points_per_game()
    points_team_2 = team_2.calculate_points_per_game()

    print(f"{points_team_1}:{points_team_2}")
