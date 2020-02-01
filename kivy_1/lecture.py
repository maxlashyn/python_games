""" установка """
from kivy.graphics.context_instructions import Rotate
from kivy.graphics.vertex_instructions import Line
from kivy.vector import Vector

""" sudo apt-get install libsdl2-2.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0 """

""" что такое kivy """

""" создание окна """
""" рисование круга, прямоугольника """
""" загрузка спрайта в круг, прямоугольник """

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Rotate
from kivy.clock import Clock

SPEED = 1

class NewWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.rectagle = Rectangle(source='assets/l0_SpaceShip0021.png', pos=(0, 0), size=(30, 30))

            self.line = Line(points=[
                100, 100,
                200, 100,
                200, 200,
                100, 200,
                100, 100
            ], width=1)

    def update(self, dt):
        self.rectagle.pos = Vector(SPEED, SPEED) + self.rectagle.pos


class NewApp(App):
    def build(self):
        widget = NewWidget()
        Clock.schedule_interval(widget.update, 1.0 / 60)
        return widget


app = NewApp()
app.run()
