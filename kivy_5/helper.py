"""
Помощник в изучении слов

1. Слова хранятся в отдельном файле в json формате {'english':'russian'}. Смотри lesson_5
2. Окно содержит
- Label1 в котором выводится слово на английском (выбираются из словаря случайным образом)
- Label2 в котором будем выводить либо подсказку, либо сообщение об ошибке
- TextInput в который пользователь вводит перевод
- кнопка "Проверить", если ввод совпал со словарем, выводим другое слово
    если не правильно, выводим сообщение об ошибке в Label2
- кнопка "Подсказать", выводим в Label2 правильный вариант
- кнопка "Пропустить", выводим другое слово

"""
import json
from random import choice

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager

try:
    fp = open('dictionary.json', 'r')
    dictionary = json.load(fp)
    fp.close()
except json.decoder.JSONDecodeError:
    dictionary = {}


class Dictionary(GridLayout):
    english = ObjectProperty('')
    russian = ObjectProperty('')

    def on_press_save_button(self, button):
        dictionary[self.english.text] = self.russian.text
        fp = open('dictionary.json', 'w')
        json.dump(dictionary, fp)
        fp.close()


class Helper(GridLayout):
    inp = ObjectProperty('')
    out = ObjectProperty('')
    message = ObjectProperty('')
    english = ''
    russian = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def press_button_next(self, button):
        pair = choice(list(dictionary.items()))
        self.english = pair[0]
        self.russian = pair[1]
        self.out = self.english
        self.message = ''
        self.inp.text = ''

    def press_button_check(self, button):
        if self.inp.text == self.russian:
            self.message = 'Вы отгадали'
            self.inp.text = ''
        else:
            self.message = 'Вы ответили неправильно'

    def press_button_help(self, button):
        self.message = self.russian


class MainScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class CalcScreen(ScreenManager):
    pass


class HelperApp(App):
    def build(self):
        return CalcScreen()


HelperApp().run()
