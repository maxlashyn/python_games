"""
игра в змейку
по экрану лазит змейка у которой есть голова и хвост
на игровое поле в случайное место падает еда
если голова сталкивается с едой, еда исчезает, а хвост увеличивается
если голова змеи врезается в стенку экрана или в свой хвост змея погибает
"""
from random import randint

from kivy.app import App
from kivy.clock import Clock

from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Rectangle
from kivy.vector import Vector

SPEED = 20


class GameOverException(Exception):
    pass


class Snake(Widget):
    head = []
    tail = []
    food = None

    def __init__(self, **kwargs):
        super(Snake, self).__init__(**kwargs)
        self.dx, self.dy = SPEED, 0
        self.game_over = False

        with self.canvas:
            Color(rgba=(1, 1, 1, 1))
            self.head = Ellipse(size=(20, 20), pos=(self.width // 2, self.height // 2))
            self.tail.append(Rectangle(size=(20, 20), pos=(self.head.pos[0] - 20, self.head.pos[1])))

    def update(self, dt):
        if not self.game_over:
            head_pos = Vector(self.head.pos[0], self.head.pos[1])
            self.head.pos = Vector(self.dx, self.dy) + self.head.pos

            last = self.tail.pop()
            last_segment_pos = Vector(last.pos[0], last.pos[1])
            last.pos = head_pos
            self.tail.insert(0, last)
            if self.food is None:
                with self.canvas:
                    Color(rgba=(0.5, 0.5, 0.5, 1))
                    self.food = Ellipse(size=(20, 20),
                                        pos=(randint(0, Window.size[0] - 20), randint(0, Window.size[1] - 20)))
            if self.collide_with(self.food):
                self.canvas.remove(self.food)
                self.food = None
                with self.canvas:
                    Color(rgba=(1, 1, 1, 1))
                    self.tail.append(Rectangle(size=(20, 20), pos=last_segment_pos))

            try:
                for segment in self.tail:
                    if self.collide_with(segment):
                        raise GameOverException()

                if self.head.pos[0] < 0 or self.head.pos[1] < 0:
                    raise GameOverException()
                if self.head.pos[0] + self.head.size[0] > self.width or self.head.pos[1] + self.head.size[
                    1] > self.height:
                    raise GameOverException()
            except GameOverException:
                self.add_widget(Label(text='game over', size=self.size, font_size=35))
                self.dx, self.dy = 0, 0
                self.game_over = True

    def collide_with(self, element):
        x1, y1 = self.head.pos
        x2, y2 = Vector(self.head.size[0], self.head.size[1]) + self.head.pos
        x3, y3 = element.pos
        x4, y4 = Vector(element.size[0], element.size[1]) + element.pos

        left = max(x1, x3)
        top = min(y2, y4)
        right = min(x2, x4)
        bottom = max(y1, y3)

        width = right - left
        height = top - bottom

        return width > 0 and height > 0

    def on_touch_down(self, touch):
        delta = Vector(touch.pos[0], touch.pos[1]) - self.head.pos
        if abs(delta[0]) > abs(delta[1]):
            self.dx, self.dy = SPEED * (-1 if delta[0] < 0 else 1), 0
        else:
            self.dx, self.dy = 0, SPEED * (-1 if delta[1] < 0 else 1)


class SnakeApp(App):
    def build(self):
        game_field = Snake(size=Window.size)
        Clock.schedule_interval(game_field.update, 10.0 / 60)
        return game_field


if __name__ == '__main__':
    SnakeApp().run()
