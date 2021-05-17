from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class LogicalLayout(GridLayout):
    def __init__(self):
        GridLayout.__init__(self, cols=4, spacing=30, padding=30)
        for i in range(5):
            self.add_widget(Label(text=''))
        self.button1 = Button(text='touch me')
        self.add_widget(self.button1)
        self.button2 = Button(text='don\'t touch me')
        self.add_widget(self.button2)
        for i in range(5):
            self.add_widget(Label(text=''))


class MyApp(App):
    def build(self):
        return LogicalLayout()


if __name__ == '__main__':
    app = MyApp()
    app.run()