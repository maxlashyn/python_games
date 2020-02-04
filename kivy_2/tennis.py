"""
игра в тенис
2 ракетки по сторонам экрана, могут перемещаться только вверх вниз
мячик отскакиевает от верхней и нижней стороны экрана и от ракеток
при столкновении с ракеткой скорость мячика увеличивается
если мячик вылетает за правую или левую сторону, игрок противоположной стороны получает +1 балл
поле выглядит так:
------------------
.   1   .   0    .
.|   *  .        .
.       .       |.
.       .        .
------------------
"""

from kivy.app import App
from kivy.graphics.vertex_instructions import Line
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Ellipse
from kivy.graphics import Rectangle
from kivy.clock import Clock
from kivy.vector import Vector
from random import choice

SPEED = 2
DELTA_SPEED = 1
RACKET_SPEED = 40
SLEEP_BEFORE_RUN = 500


class Field(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_close, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self.dx = SPEED * choice([-1, 1])
        self.dy = SPEED * choice([-1, 1])
        self.left_player_score = 0
        self.right_player_score = 0
        self.run = 0

        with self.canvas:
            self.center_line = Rectangle(pos=(Window.size[0] // 2, 0), size=(5, Window.size[1]))
            self.left_label = Label(pos_hint=(0.1, 0.1), text=str(self.left_player_score))
            self.left_racket = Rectangle(pos=(20, Window.size[1] // 2 - 50), size=(5, 100))

            self.right_label = Label(pos_hint=(0.2, 0.2), text=str(self.right_player_score))
            self.right_racket = Rectangle(pos=(Window.size[0] - 20, Window.size[1] // 2 - 50), size=(5, 100))

            self.ball = Ellipse(pos=(Window.size[0] // 2 - 15, Window.size[1] // 2 - 15), size=(30, 30))
            self.circle = Line(
                circle=(Window.size[0] // 2, Window.size[1] // 2, 100, 0, 360))

    def _on_keyboard_close(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if text == 'w' and self.left_racket.pos[1] + self.left_racket.size[1] < self.height:
            self.left_racket.pos = Vector(0, RACKET_SPEED) + self.left_racket.pos
        if text == 's' and self.left_racket.pos[1] > 0:
            self.left_racket.pos = Vector(0, -RACKET_SPEED) + self.left_racket.pos
        if text == 'o' and self.right_racket.pos[1] + self.right_racket.size[1] < self.height:
            self.right_racket.pos = Vector(0, RACKET_SPEED) + self.right_racket.pos
        if text == 'l' and self.right_racket.pos[1] > 0:
            self.right_racket.pos = Vector(0, -RACKET_SPEED) + self.right_racket.pos

    def check_collision_left(self, ball, racket):
        return ball.pos[0] < racket.pos[0] + racket.size[0] \
               and racket.pos[1] <= ball.pos[1] + ball.size[1] // 2 <= racket.pos[1] + racket.size[1]

    def check_collision_right(self, ball, racket):
        return ball.pos[0] + ball.size[0] > racket.pos[0] \
               and racket.pos[1] <= ball.pos[1] + ball.size[1] // 2 <= racket.pos[1] + racket.size[1]

    def update(self, dt):
        self.center_line.pos = (Window.size[0] // 2, 0)
        self.center_line.size = (5, Window.size[1])
        self.right_racket.pos = (Window.size[0] - 20, self.right_racket.pos[1])
        self.circle.circle = (Window.size[0] // 2, Window.size[1] // 2, 100, 0, 360)

        if self.run < SLEEP_BEFORE_RUN:
            self.run += 1

        ball_pos = self.ball.pos
        if self.height < ball_pos[1] + self.ball.size[1] + self.dy or ball_pos[1] + self.dy < 0:
            self.dy *= -1

        if self.check_collision_left(self.ball, self.left_racket):
            self.dx = abs(self.dx) + DELTA_SPEED
            self.dy = (abs(self.dy) + DELTA_SPEED) * (1 if self.dy > 0 else -1)
        elif ball_pos[0] + self.dx < 0:
            self.init_ball()
            self.right_player_score += 1
            self.right_label.text = str(self.right_player_score)

        if self.check_collision_right(self.ball, self.right_racket):
            self.dx = -(abs(self.dx) + DELTA_SPEED)
            self.dy = (abs(self.dy) + DELTA_SPEED) * (1 if self.dy > 0 else -1)
        elif ball_pos[0] + self.ball.size[0] + self.dx > self.right:
            self.init_ball()
            self.left_player_score += 1
            self.left_label.text = str(self.left_player_score)

        self.ball.pos = Vector(self.dx, self.dy) + self.ball.pos

    def init_ball(self):
        self.ball.pos = (Window.size[0] // 2 - 15, Window.size[1] // 2 - 15)
        self.dx = SPEED * choice([-1, 1])
        self.dy = SPEED * choice([-1, 1])
        self.run = 0


class Game(App):
    def build(self):
        layout = FloatLayout(size=(Window.size[0], Window.size[1]))
        field = Field()
        Clock.schedule_interval(field.update, 1.0 / 60)
        layout.add_widget(field)
        return layout


if __name__ == '__main__':
    Game().run()
