from kivy.core.window import Window
Window.fullscreen = False
Window.size = (500,300)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty
import japanize_kivy
from kivy.lang import Builder

Builder.load_string('''
<TextWidget>:
    BoxLayout:
        orientation: 'vertical'
        size: root.size

        Label:
            size_hint_x: 1.5
            size_hint_y: 0.5
            font_size: 20
            text: root.text
            color: root.color

        BoxLayout:
            Label:
                id: label1
                size_hint_y: 0.3
                font_size: 20
                text: root.text
                color: root.color

            Label:
                id: label2
                size_hint_y: 0.4
                font_size: 20
                text: root.text
                color: root.color

        BoxLayout:
            size_hint_y: 0.8
            padding: 20,30,20, 10

            Button:
                id: button1
                text: "ぐー"
                font_size: 45
                on_press: root.buttonClicked()  #ボタンをクリックした時

            Button:
                id: button2
                text: "ちょき"
                font_size: 45
                on_press: root.buttonClicked2() # ボタンをクリックした時

            Button:
                id: button3
                text: "ぱー"
                font_size: 45
                on_press: root.buttonClicked3() # ボタンをクリックした時
''')

class TextWidget(Widget):
    text = StringProperty()
    color = ListProperty([1,1,1,1])

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def buttonClicked(self):
        self.text = 'おはよう'
        self.color = [1, 0, 0 , 1]

    def buttonClicked2(self):
        self.text = 'こんにちは'
        self.color = [0, 1, 0 , 1 ]

    def buttonClicked3(self):
        self.text = 'こんばんは'
        self.color = [0, 0, 1 , 1 ]

class TestApp(App):
    def build(self):
        self.title = 'greeting'
        return TextWidget()

TestApp().run()
