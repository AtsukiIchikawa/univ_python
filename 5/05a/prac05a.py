import random
import jank
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
            id: result
            text: result.text
            size_hint_x: 1.5
            size_hint_y: 0.5
            font_size: 20
            color: root.color

        BoxLayout:
            Label:
                id: label1
                text: label1.text
                size_hint_y: 0.3
                font_size: 20
                color: root.color

            Label:
                id: label2
                text: label2.text
                size_hint_y: 0.4
                font_size: 20
                color: root.color

        BoxLayout:
            size_hint_y: 0.8
            padding: 20,30,20, 10

            Button:
                id: button1
                text: "ぐー"
                font_size: 45
                on_press: root.buttonClicked(result, label1, label2)  #ボタンをクリックした時

            Button:
                id: button2
                text: "ちょき"
                font_size: 45
                on_press: root.buttonClicked2(result, label1, label2) # ボタンをクリックした時

            Button:
                id: button3
                text: "ぱー"
                font_size: 45
                on_press: root.buttonClicked3(result, label1, label2) # ボタンをクリックした時
''')


class TextWidget(Widget):
    text = StringProperty()
    color = ListProperty([1,1,1,1])

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''
        self.color = [0, 1, 0, 1]

    def buttonClicked(self, result, label1, label2):
        computer_hand = random.randint(1, 3)
        result.text = jank.wol(1, computer_hand)
        if computer_hand == 1:
            label1.text = "ぐー"
        elif computer_hand == 2:
            label1.text = "ちょき"
        else:
            label1.text = "ぱー"
        label2.text = "これまで" + str(jank.p_win) + "勝" + str(jank.c_win) + "敗" + str(jank.draw) + "あいこ"

    def buttonClicked2(self, result, label1, label2):
        computer_hand = random.randint(1, 3)
        result.text = jank.wol(2, computer_hand)
        if computer_hand == 1:
            label1.text = "ぐー"
        elif computer_hand == 2:
            label1.text = "ちょき"
        else:
            label1.text = "ぱー"
        label2.text = "これまで" + str(jank.p_win) + "勝" + str(jank.c_win) + "敗" + str(jank.draw) + "あいこ"

    def buttonClicked3(self, result, label1, label2):
        computer_hand = random.randint(1, 3)
        result.text = jank.wol(3, computer_hand)
        if computer_hand == 1:
            label1.text = "ぐー"
        elif computer_hand == 2:
            label1.text = "ちょき"
        else:
            label1.text = "ぱー"
        label2.text = "これまで" + str(jank.p_win) + "勝" + str(jank.c_win) + "敗" + str(jank.draw) + "あいこ"


class TestApp(App):
    def build(self):
        self.title = 'じゃんけん'
        return TextWidget()

TestApp().run()
