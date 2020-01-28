from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse
from kivy.clock import Clock
from kivy.vector import Vector

DX_SPEED = 10
DY_SPEED = 10


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dx = DX_SPEED
        self.dy = DY_SPEED
        with self.canvas:
            self.ellipse = Ellipse(pos=(0, 0), size=(20, 20))

    def update(self, dt):
        pos = self.ellipse.pos
        if 0 > pos[0] + self.dx or pos[0] + self.dx > self.right:
            self.dx *= -1
        if 0 > pos[1] + self.dy or pos[1] + self.dy > self.top:
            self.dy *= -1

        self.ellipse.pos = Vector(self.dx, self.dy) + self.ellipse.pos


class MyApp(App):
    def build(self):
        circle = MyWidget()
        Clock.schedule_interval(circle.update, 1.0 / 60)
        return circle


if __name__ == '__main__':
    app = MyApp()
    app.run()
