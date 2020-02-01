"""
нарисовать шарик размером 35, 35 который будет летать
по окну и отскакивать от границ окна
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Rectangle
from kivy.clock import Clock
from kivy.vector import Vector

SPEED = 10

class NewWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dx = SPEED
        self.dy = SPEED
        with self.canvas:
            self.rectangle = Rectangle(pos=(300, 300), size=(100, 100))
            self.ellipse = Ellipse(pos=(0, 0), size=(30, 30))

    def collision(self, ellipse, rectangle):
        return ellipse.pos[0] > rectangle.pos[0]

    def update(self, dt):
        print('update')
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

        if self.collision(self.ellipse, self.rectangle):
            print('collision')

        self.ellipse.pos = Vector(self.dx, self.dy) + self.ellipse.pos



class NewApp(App):
    def build(self):
        widget = NewWidget()
        Clock.schedule_interval(widget.update, 1.0 / 60)
        return widget

app = NewApp()
app.run()