from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class CalcWidget(GridLayout):
    text = ObjectProperty('')
    first_operand_str = ObjectProperty('')
    second_operand_str = ObjectProperty('')
    operation = ''

    def change_label(self):
        self.text = self.first_operand_str
        if self.operation != '':
            self.text += self.operation + self.second_operand_str

    def on_press_clear_button(self, button):
        if button.text == 'C':
            self.first_operand_str = ''
            self.second_operand_str = ''
            self.operation = ''
        if button.text == '<':
            if self.operation == '':
                self.first_operand_str = self.first_operand_str[:-1]
            else:
                self.second_operand_str = self.second_operand_str[:-1]
        self.change_label()

    def action(self):
        if self.second_operand_str != '':
            a, b = float(self.first_operand_str), float(self.second_operand_str)
            result = 0
            if self.operation == '+':
                result = a + b
            if self.operation == '-':
                result = a - b
            if self.operation == '*':
                result = a * b
            if self.operation == '/':
                result = a / b

            self.first_operand_str = str(result)
            self.second_operand_str = ''

    def on_press_operation_button(self, button):
        if self.first_operand_str != '':
            self.action()
            self.operation = ''
            if button.text != '=':
                if self.operation == '' or self.second_operand_str == '':
                    self.operation = button.text
            self.change_label()

    def on_press_number_button(self, button):
        if self.operation == '':
            if button.text == '.' and list(self.first_operand_str).count('.') > 0:
                return
            self.first_operand_str += button.text
        else:
            if button.text == '.' and list(self.second_operand_str).count('.') > 0:
                return
            self.second_operand_str += button.text

        self.change_label()


class CalcApp(App):
    def build(self):
        return CalcWidget()


if __name__ == '__main__':
    CalcApp().run()
