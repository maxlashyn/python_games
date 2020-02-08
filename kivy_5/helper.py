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
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout


class Helper(GridLayout):
    inp = ObjectProperty('')
    out = ObjectProperty('')

    def press_button(self, button):
        self.out = self.inp.text


class HelperApp(App):
    def build(self):
        return Helper()


HelperApp().run()
