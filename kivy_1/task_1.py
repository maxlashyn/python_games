from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Ellipse(pos=(0,0), size=(20, 20))

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    app = MyApp()
    app.run()
