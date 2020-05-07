"""
Задача D. Игра в пьяницу

В игре в пьяницу карточная колода раздается поровну двум игрокам.
Далее они вскрывают по одной верхней карте, и тот, чья карта старше,
забирает себе обе вскрытые карты, которые кладутся под низ его колоды.
Тот, кто остается без карт – проигрывает.
Для простоты будем считать, что все карты различны по номиналу,
а также, что самая младшая карта побеждает самую старшую карту ("шестерка берет туза").
Игрок, который забирает себе карты,
сначала кладет под низ своей колоды карту первого игрока,
затем карту второго игрока (то есть карта второго игрока оказывается внизу колоды).
Напишите программу, которая моделирует игру в пьяницу и определяет, кто выигрывает.
В игре участвует 10 карт, имеющих значения от 0 до 9,
большая карта побеждает меньшую, карта со значением 0 побеждает карту 9.
"""
from data_structure.queue import Queue


class Game:
    def __init__(self, player_1: Queue, player_2: Queue):
        self.player_1 = player_1
        self.player_2 = player_2
        self.steps = 0

    def cards_on_table(self):
        cart_player_1 = self.player_1.pop()
        cart_player_2 = self.player_2.pop()

        return cart_player_1, cart_player_2

    def calc_winner(self, cart_player_1, cart_player_2):

        cur_winner = self._get_winner(cart_player_1, cart_player_2)

        if cur_winner == self.player_1:
            self.player_1.push(cart_player_1)
            self.player_1.push(cart_player_2)
        else:
            self.player_2.push(cart_player_1)
            self.player_2.push(cart_player_2)

        self.steps += 1

    def _get_winner(self, cart_player_1, cart_player_2):
        special_cards = [0, 9]

        # случай когда 0 побеждает 9
        if (cart_player_1 in special_cards and
                cart_player_2 in special_cards):

            if cart_player_1 < cart_player_2:
                winner = self.player_1
            else:
                winner = self.player_2

        # все остальные случаи (кто больше тот и победил)
        elif cart_player_1 > cart_player_2:
            winner = self.player_1
        else:
            winner = self.player_2

        return winner

    def is_game_of(self):
        if (self.player_1.size == 0 or
            self.player_2.size == 0 or
            self.steps == 10**6):
            return True
        else:
            return False


if __name__== "__main__":
    player_1 = Queue()
    player_2 = Queue()

    # Раздача карт 1 игроку
    inp_player_1 = input()[:9]
    for cart in inp_player_1.split(" "):
        cart = int(cart)
        player_1.push(cart)
    # Раздача карт 2 игроку
    inp_player_2 = input()[:9]
    for cart in inp_player_2.split(" "):
        cart = int(cart)
        player_2.push(cart)

    game = Game(player_1, player_2)
    # процесс игры
    while not game.is_game_of():
        cart_player_1, cart_player_2 = game.cards_on_table()
        game.calc_winner(cart_player_1, cart_player_2)

    # определение того, кто выиграл
    if player_1.size == 0:
        print(f"second {game.steps}")
    elif player_2.size == 0:
        print(f"first {game.steps}")
    else:
        print("botva")


