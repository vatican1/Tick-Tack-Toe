class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1
        self.fieldArray = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.endGame = False
        print("Вводите координаты клетки(левая верхняя 1 1)")
        self.draw()
        self.get_turn()

    def get_turn(self):
        if self.turn == 1:
            print(self.player1 + " ходит крестиками")
        else:
            print(self.player2 + " ходит ноликами")

    def cheat_move(self, x_or_zero, cord_x, cord_y):  # 1 - крестики, 2 - нолики
        self.fieldArray[cord_x][cord_y] = x_or_zero

    def move(self, cord_x, cord_y):
        if 0 > cord_x or 0 > cord_y or cord_x > 3 or cord_y > 3:
            print("Сюда нельзя ходить")
            return
        if self.endGame:
            print("Игра окончена")
            return
        if self.fieldArray[cord_x][cord_y] == 0:
            self.fieldArray[cord_x][cord_y] = self.turn

            if self.turn == 1:
                self.turn = 2
            else:
                self.turn = 1
            self.draw()
            self.get_turn()
            self.check_win()

        else:
            print("Сюда ходить нельзя")
            self.get_turn()

    def draw(self):
        for line in self.fieldArray:
            for element in line:
                if element == 0:
                    print(" _ ", end="")
                if element == 1:
                    print(" X ", end="")
                if element == 2:
                    print(" O ", end="")
            print()

    def check_win(self):
        win_coord = (([0, 0], [0, 1], [0, 2]),
                     ([1, 0], [1, 1], [1, 2]),
                     ([2, 0], [2, 1], [2, 2]),
                     ([0, 0], [1, 0], [2, 0]),
                     ([0, 1], [1, 1], [2, 1]),
                     ([0, 2], [1, 2], [2, 2]),
                     ([0, 0], [1, 1], [2, 2]),
                     ([0, 2], [1, 1], [2, 0]))
        for each in win_coord:
            if self.fieldArray[each[0][0]][each[0][1]] == self.fieldArray[each[1][0]][each[1][1]] == \
                    self.fieldArray[each[2][0]][each[2][1]] & self.fieldArray[each[0][0]][each[0][1]] != 0:
                print("ПОБЕДА!")
                self.endGame = True


game = Game('Лупа', 'Пупа')
while not game.endGame:
    x, y = input().split(' ')
    game.move(int(x) - 1, int(y) - 1)
