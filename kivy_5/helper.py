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
from random import choice

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from dictionary import dictionary

class Helper(GridLayout):
    inp = ObjectProperty('')
    out = ObjectProperty('')
    message = ObjectProperty('')
    words = {}
    english = ''
    russian = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.words = dictionary

    def press_button_next(self, button):
        pair = choice(list(self.words.items()))
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

class HelperApp(App):
    def build(self):
        return Helper()


HelperApp().run()
