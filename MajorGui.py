from kivy.uix import button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class LogicalLayout(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self, row=4, column=4)
