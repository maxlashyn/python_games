"""
нарисовать шарик размером 35, 35 который будет летать
по окну и отскакивать от границ окна
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Rectangle
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.core.window import Window

SPEED = 10


class NewWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.keyboard = Window.request_keyboard(self._on_keyboard_close, self)
        self.keyboard.bind(on_key_down=self._on_key_down)

        self.dx = SPEED
        self.dy = SPEED
        with self.canvas:
            self.rectangle = Rectangle(source='assets/l0_SpaceShip0021.png', pos=(300, 300), size=(100, 100))
            self.ellipse = Ellipse(pos=(0, 0), size=(30, 30))

    def _on_keyboard_close(self):
        self.keyboard.unbind(on_key_down=self._on_key_down)
        self.keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if text == 'w':
            self.rectangle.pos = Vector(0, SPEED) + self.rectangle.pos
        if text == 's':
            self.rectangle.pos = Vector(0, -SPEED) + self.rectangle.pos
        if text == 'a':
            self.rectangle.pos = Vector(-SPEED, 0) + self.rectangle.pos
        if text == 'd':
            self.rectangle.pos = Vector(SPEED, 0) + self.rectangle.pos


    def update(self, dt):
        pos = self.ellipse.pos
        size = self.ellipse.size
        if pos[0] + size[0] + self.dx >= self.right:
            self.dx *= -1
        if pos[0] + self.dx <= 0:
            self.dx *= -1
        if pos[1] + self.dy <= 0:
            self.dy *= -1
        if pos[1] + size[1] + self.dy >= self.top:
            self.dy *= -1

        self.ellipse.pos = Vector(self.dx, self.dy) + self.ellipse.pos


class NewApp(App):
    def build(self):
        widget = NewWidget()
        Clock.schedule_interval(widget.update, 1.0 / 60)
        return widget


app = NewApp()
app.run()
