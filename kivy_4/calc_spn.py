from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class WhiteLabel(Label):
    pass


class Calc(GridLayout):
    text = ObjectProperty('')
    stack0 = ObjectProperty('')
    stack1 = ObjectProperty('')
    stack2 = ObjectProperty('')
    stack3 = ObjectProperty('')
    stack4 = ObjectProperty('')
    stack = [
    ]
    operation = ''

    def on_press_to_stack(self, button):
        if self.text != '' and len(self.stack) < 5:
            self.stack.append(self.text)
        self.refresh_stack()

    def refresh_stack(self):
        self.stack0 = ''
        self.stack1 = ''
        self.stack2 = ''
        self.stack3 = ''
        self.stack4 = ''
        if len(self.stack) == 1:
            self.stack4 = self.stack[0]

        if len(self.stack) == 2:
            self.stack4 = self.stack[1]
            self.stack3 = self.stack[0]

        if len(self.stack) == 3:
            self.stack4 = self.stack[2]
            self.stack3 = self.stack[1]
            self.stack2 = self.stack[0]

        if len(self.stack) == 4:
            self.stack4 = self.stack[3]
            self.stack3 = self.stack[2]
            self.stack2 = self.stack[1]
            self.stack1 = self.stack[0]

        if len(self.stack) == 5:
            self.stack0 = self.stack[0]
            self.stack1 = self.stack[1]
            self.stack2 = self.stack[2]
            self.stack3 = self.stack[3]
            self.stack4 = self.stack[4]
        self.text = ''

    def on_press_operation_button(self, button):
        if len(self.stack) > 1:
            b, a = float(self.stack.pop()), float(self.stack.pop())
            if button.text == '+':
                self.stack.append(str(a + b))
            if button.text == '-':
                self.stack.append(str(a - b))
            if button.text == '*':
                self.stack.append(str(a * b))
            if button.text == '/':
                self.stack.append(str(a / b))
            self.refresh_stack()

    def on_press_stack_operation(self, button):
        if button.text == 'swap' and len(self.stack) >= 2:
            a, b = self.stack.pop(), self.stack.pop()
            self.stack.append(a)
            self.stack.append(b)

        if button.text == 'dup' and 0 < len(self.stack) < 5:
            self.stack.append(self.stack[-1:][0])

        if button.text == 'rot' and len(self.stack) > 2:
            a, b, c = self.stack.pop(), self.stack.pop(), self.stack.pop()
            self.stack.append(b)
            self.stack.append(a)
            self.stack.append(c)

        self.refresh_stack()

    def on_press_equal_button(self, button):
        if len(self.stack) > 0:
            self.text = self.stack[-1:][0]

    def on_press_number_button(self, button):
        if button.text == '.' and list(self.text).count('.') > 0:
            return
        self.text += button.text

    def on_press_clear_button(self, button):
        if button.text == 'C':
            self.text = ''
        if button.text == '<' and len(self.text) > 0:
            self.text = self.text[:-1]

        if button.text == 'CS':
            self.stack = []
            self.refresh_stack()

        if button.text == 'CTS':
            self.stack.pop()
            self.refresh_stack()


class CalcApp(App):
    def build(self):
        return Calc()


if __name__ == '__main__':
    CalcApp().run()
