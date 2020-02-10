"""
игра в змейку
по экрану лазит змейка у которой есть голова и хвост
на игровое поле в случайное место падает еда
если голова сталкивается с едой, еда исчезает, а хвост увеличивается
если голова змеи врезается в стенку экрана или в свой хвост змея погибает
"""

# Импортируем элементы Kivy, которые будем использовать в классах
from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.vertex_instructions import Rectangle, Triangle, Ellipse
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, BooleanProperty, OptionProperty, \
    ReferenceListProperty


class Playground(Widget):
    # Привязываем переменным элементы из .kv
    fruit = ObjectProperty(None)
    snake = ObjectProperty(None)

    # Задаем размер сетки
    col_number = 16
    row_number = 9

    # Игровые переменные
    score = NumericProperty(0)
    turn_counter = NumericProperty(0)
    fruit_rythme = NumericProperty(0)

    # Одработка входных данных
    touch_start_pos = ListProperty()
    action_triggered = BooleanProperty(False)

    def start(self):
        # Добавляем змею на поле
        self.new_snake()

        # Начинаем основной цикл обновления игры
        self.update()

    def reset(self):
        # Сбрасываем игровые переменные
        self.turn_counter = 0
        self.score = 0

        # Удаляем образы змеи и фрукта с поля
        self.snake.remove()
        self.fruit.remove()

        Clock.unschedule(self.pop_fruit)
        Clock.unschedule(self.fruit.remove)
        Clock.unschedule(self.update)

    def new_snake(self):
        # Генерируем случайные координаты
        start_coord = (
            randint(2, self.col_number - 2), randint(2, self.row_number - 2))

        # Устанавливаем для змеи новые координаты
        self.snake.set_position(start_coord)

        # Генерируем случайное направление
        rand_index = randint(0, 3)
        start_direction = ["Up", "Down", "Left", "Right"][rand_index]

        # Задаем змее случайное направление
        self.snake.set_direction(start_direction)

    def pop_fruit(self, *args):
        # Генерируем случайные координаты для фрукта
        random_coord = [
            randint(1, self.col_number), randint(1, self.row_number)]

        # получаем координаты всех клеток занимаемых змеей
        snake_space = self.snake.get_full_position()

        # Если координаты фрукта совпадают с координатами клеток змеи - генерируем
        # новые координаты
        while random_coord in snake_space:
            random_coord = [
                randint(1, self.col_number), randint(1, self.row_number)]

        # Помещаем образ фрукта на поле
        self.fruit.pop(random_coord)

    def is_defeated(self):
        """
        Проверяем, является ли позиция змеи проигрышной.
        """
        snake_position = self.snake.get_position()

        # Если змея кусает свой хвост - поражение
        if snake_position in self.snake.tail.blocks_positions:
            return True

        # Если вышла за пределы поля - поражение
        if snake_position[0] > self.col_number \
                or snake_position[0] < 1 \
                or snake_position[1] > self.row_number \
                or snake_position[1] < 1:
            return True

        return False

    def update(self, *args):
        # Регистрация последовательности появления фруктов в планировщике событий
        if self.turn_counter == 0:
            self.fruit_rythme = self.fruit.interval + self.fruit.duration
            Clock.schedule_interval(
                self.fruit.remove, self.fruit_rythme)
        elif self.turn_counter == self.fruit.interval:
            self.pop_fruit()
            Clock.schedule_interval(
                self.pop_fruit, self.fruit_rythme)

        """
        Используется для смены игровых ходов.
        """
        # Перемещаем змею на следующую позицию
        self.snake.move()

        # Проверяем на поражение
        # Если поражение - сбрасываем игру
        if self.is_defeated():
            self.reset()
            self.start()
            return

        # Проверяем, находится ли фрукт на поле
        if self.fruit.is_on_board():
            # Если змея съела фрукт - увеличиваем счет и длину змеи
            if self.snake.get_position() == self.fruit.pos:
                self.fruit.remove()
                self.score += 1
                self.snake.tail.size += 1

        # Увеличиваем счетчик ходов
        self.turn_counter += 1

        # Каждое обновление будет происходить ежесекундно (1'')
        Clock.schedule_once(self.update, 1)

    def on_click_down(self, touch):
        self.touch_start_pos = touch.spos

    def on_click_move(self, touch):
        # Вычисляем изменение позиции пальца
        # Проверяем, изменение > 10% от размера экрана:
        # Здесь мы регистрируем, что действие закончено, для того, чтобы оно не
        # происходило более одного раза за ход


    def on_click_up(self, touch):
        # Указываем, что мы готовы принять новые инструкции
        self.action_triggered = False



class Fruit(Widget):
    # Эти значения будем использовать для определения частоты появления fruit_rythme
    duration = NumericProperty(10)  # Продолжительность существования
    interval = NumericProperty(3)  # Продолжительность отсутствия

    # Представление на поле
    object_on_board = ObjectProperty(None)
    state = BooleanProperty(False)

    def is_on_board(self):
        return self.state

    def remove(self, *args):
        # Удаляем объект с поля и указываем, что он сейчас стерт
        if self.is_on_board():
            self.canvas.remove(self.object_on_board)
            self.object_on_board = ObjectProperty(None)
            self.state = False

    def pop(self, pos):
        self.pos = pos  # объявляем, что фрукт находится на поле

        # Рисуем фрукт
        with self.canvas:
            x = (pos[0] - 1) * self.size[0]
            y = (pos[1] - 1) * self.size[1]
            coord = (x, y)

            # Сохраняем представление и обновляем состояние объекта
            self.object_on_board = Ellipse(pos=coord, size=self.size)
            self.state = True


class Snake(Widget):
    head = ObjectProperty(None)
    tail = ObjectProperty(None)

    def move(self):
        """
        Движение змеи будет происходить в 3 этапа:
            - сохранить текущее положение головы.
            - передвинуть голову на одну позицию вперед.
            - переместить последний блок хвоста на предыдущие координаты головы .
        """
        next_tail_pos = list(self.head.position)
        self.head.move()
        self.tail.add_block(next_tail_pos)

    def remove(self):
        """
        Здесь мы опишем, удаление элементов хвоста и головы
        """
        self.head.remove()
        self.tail.remove()

    def set_position(self, position):
        self.head.position = position

    def get_position(self):
        """
        Положение змеи равно положению ее головы на поле.
        """
        return self.head.position

    def get_full_position(self):
        """
        Но иногда нам нужно будет узнавать, какое пространство занимает змея.
        """
        return self.head.position + self.tail.blocks_positions

    def set_direction(self, direction):
        self.head.direction = direction

    def get_direction(self):
        return self.head.direction


class SnakeHead(Widget):
    # Направление головы и ее позиция
    direction = OptionProperty(
        "Right", options=["Up", "Down", "Left", "Right"])
    x_position = NumericProperty(0)
    y_position = NumericProperty(0)
    position = ReferenceListProperty(x_position, y_position)

    # Представление головы на поле
    points = ListProperty([0] * 6)
    object_on_board = ObjectProperty(None)
    state = BooleanProperty(False)

    def is_on_board(self):
        return self.state

    def remove(self):
        if self.is_on_board():
            self.canvas.remove(self.object_on_board)
            self.object_on_board = ObjectProperty(None)
            self.state = False

    def show(self):
        """
        Размещаем голову на холсте.
        """
        with self.canvas:
            if not self.is_on_board():
                self.object_on_board = Triangle(points=self.points)
                self.state = True
            else:
                # Если объект должен быть на поле - удаляем старую голову
                # и рисуем новую
                self.canvas.remove(self.object_on_board)
                self.object_on_board = Triangle(points=self.points)

    def move(self):
        """
        Не самое элегантное решение, но это работает.
        Здесь мы описываем изображение треугольника для каждого положения головы.
        """
        global x1, y1, x2, y2, y0, x0
        if self.direction == "Right":
            # Обновляем позицию
            self.position[0] += 1

            # Вычисляем положения точек
            x0 = self.position[0] * self.width
            y0 = (self.position[1] - 0.5) * self.height
            x1 = x0 - self.width
            y1 = y0 + self.height / 2
            x2 = x0 - self.width
            y2 = y0 - self.height / 2
        elif self.direction == "Left":
            self.position[0] -= 1
            x0 = (self.position[0] - 1) * self.width
            y0 = (self.position[1] - 0.5) * self.height
            x1 = x0 + self.width
            y1 = y0 - self.height / 2
            x2 = x0 + self.width
            y2 = y0 + self.height / 2
        elif self.direction == "Up":
            self.position[1] += 1
            x0 = (self.position[0] - 0.5) * self.width
            y0 = self.position[1] * self.height
            x1 = x0 - self.width / 2
            y1 = y0 - self.height
            x2 = x0 + self.width / 2
            y2 = y0 - self.height
        elif self.direction == "Down":
            self.position[1] -= 1
            x0 = (self.position[0] - 0.5) * self.width
            y0 = (self.position[1] - 1) * self.height
            x1 = x0 + self.width / 2
            y1 = y0 + self.height
            x2 = x0 - self.width / 2
            y2 = y0 + self.height

        # Записываем положения точек
        self.points = [x0, y0, x1, y1, x2, y2]

        # Рисуем голову
        self.show()


class SnakeTail(Widget):
    # Длинна хвоста. Измеряется в количестве блоков
    size = NumericProperty(3)

    # Позицию каждого блока хвоста мы будем хранить здесь
    blocks_positions = ListProperty()

    # Обьекты (виджеты) хвоста будут находиться в этой переменной
    tail_blocks_objects = ListProperty()

    def remove(self):
        # Сбрасываем счетчик длины
        self.size = 3

        # Удаляем каждый блок хвоста
        for block in self.tail_blocks_objects:
            self.canvas.remove(block)

        # Обнуляем списки с координатами блоков
        # и их представления на холсте
        self.blocks_positions = []
        self.tail_blocks_objects = []

    def add_block(self, pos):
        """
        Здесь действуем в 3 этапа :
            - Передаем позицию нового блока как аргумент и добавляем блок в список объектов.
            - Проверяем равенство длины хвоста и количества блоков и изменяем, если требуется.
            - Рисуем блоки на холсте, до тех пор, пока количество нарисованных блоков не станет равно длине хвоста.
        """
        # Добавляем координаты блоков в список
        self.blocks_positions.append(pos)

        # Делаем проверку соответствия количеству блоков змеи на холсте и переменной отражающей длину
        if len(self.blocks_positions) > self.size:
            self.blocks_positions.pop(0)

        with self.canvas:
            # Рисуем блоки используя координаты из списка
            for block_pos in self.blocks_positions:
                x = (block_pos[0] - 1) * self.width
                y = (block_pos[1] - 1) * self.height
                coord = (x, y)
                block = Rectangle(pos=coord, size=(self.width, self.height))

                # Добавляем новый блок к списку объектов
                self.tail_blocks_objects.append(block)

                # Делаем проверку длины и удаляем лишние блоки с холста, если необходимо
                if len(self.tail_blocks_objects) > self.size:
                    last_block = self.tail_blocks_objects.pop(0)
                    self.canvas.remove(last_block)


class SnakeApp(App):
    game_engine = ObjectProperty(None)

    def build(self):
        self.game_engine = Playground()
        return self.game_engine



if __name__ == '__main__':
    SnakeApp().run()
