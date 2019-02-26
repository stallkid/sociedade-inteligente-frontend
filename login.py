from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def build():

    layout = FloatLayout()

    ed = TextInput(text="Login:")
    ed.size_hint = None, None
    ed.height = 30
    ed.width = 300
    ed.y = 500
    ed.x = 150

    ed2 = TextInput(text="Senha:")
    ed2.size_hint = None, None
    ed2.height = 30
    ed2.width = 300
    ed2.y = 400
    ed2.x = 150

    bt = Button(text="Acessar")
    bt.size_hint = None, None
    bt.height = 50
    bt.width = 200
    bt.y = 300
    bt.x = 200

    layout.add_widget(ed)
    layout.add_widget(ed2)
    layout.add_widget(bt)

    return layout

janela = App()
janela.title = "Faça seu login"

from kivy.core.window import Window
Window.clearcolor = [1,1,1,1]
Window.size = 600,600

janela.build = build
janela.run()