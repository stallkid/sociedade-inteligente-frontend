from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)

class Login(App):

    def build(self):
        c = CustomLayout()
        c.add_widget(
            AsyncImage(
                source="background-login.jpg"))

        lbl = Label(text='Capture Face')
        lbl.font_size= '60sp'
        lbl.bold= True
        lbl.color= [1,1,1,1]
        lbl.size_hint = None, None
        lbl.height = 30
        lbl.width = 300
        lbl.y = 370
        lbl.x = 250

        lbl2 = Label(text='Entre abaixo com seu usuário:')
        lbl2.font_size= '20sp'
        lbl2.bold= True
        lbl2.color= [1,1,1,1]
        lbl2.size_hint = None, None
        lbl2.height = 30
        lbl2.width = 300
        lbl2.y = 290
        lbl2.x = 250

        lbl3 = Label(text='Agora digite sua senha, está quase lá!')
        lbl3.font_size= '20sp'
        lbl3.bold= True
        lbl3.color= [1,1,1,1]
        lbl3.size_hint = None, None
        lbl3.height = 30
        lbl3.width = 300
        lbl3.y = 220
        lbl3.x = 255

        ed = TextInput(text="")
        ed.size_hint = None, None
        ed.height = 30
        ed.width = 300
        ed.y = 250
        ed.x = 250

        ed2 = TextInput(text="")
        ed2.size_hint = None, None
        ed2.height = 30
        ed2.width = 300
        ed2.y = 180
        ed2.x = 250

        bt = Button(text="Acessar")
        bt.size_hint = None, None
        bt.height = 50
        bt.width = 200
        bt.y = 90
        bt.x = 300

        c.add_widget(lbl)
        c.add_widget(lbl2)
        c.add_widget(lbl3)
        c.add_widget(ed)
        c.add_widget(ed2)
        c.add_widget(bt)

        return c

if __name__ == '__main__':
    Window.size = (800, 450)
    Login().run()
