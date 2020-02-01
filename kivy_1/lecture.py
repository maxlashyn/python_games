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
from kivy.graphics import Ellipse, Rectangle
from kivy.clock import Clock

SPEED = 1

class NewWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            for x in range(0, 200, 50):
                for y in range(0, 200, 50):
                    Rectangle(source='assets/l0_SpaceShip0021.png', size=(50, 50), pos=(x, y))
            self.rectagle = Ellipse(pos=(0, 0), size=(30, 20))

            self.line = Line(points=[
                100, 100,
                200, 100,
                200, 200,
                100, 200,
                100, 100
            ], width=1)

    def update(self, dt):
        # self.top, self.right, 0, 0
        # self.rectagle.pos[0] - x
        # self.rectagle.pos[1] - y
        # a = self.rectagle.size[0] - width
        # self.rectagle.size[1] - height
        self.rectagle.pos = Vector(SPEED, SPEED) + self.rectagle.pos


class NewApp(App):
    def build(self):
        widget = NewWidget()
        Clock.schedule_interval(widget.update, 1.0 / 60)
        return widget


app = NewApp()
app.run()