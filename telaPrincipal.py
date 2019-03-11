from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)

class Principal(App):

    def build(self):
        c = CustomLayout()
        c.add_widget(
            AsyncImage(
                source="Login/background-login.jpg"))

        lbl = Label(text='Bem vindo')
        lbl.font_size= '60sp'
        lbl.bold= True
        lbl.color= [1,1,1,1]
        lbl.size_hint = None, None
        lbl.height = 30
        lbl.width = 300
        lbl.y = 370
        lbl.x = 250

        bt = Button(text="Iniciar captura de face")
        bt.size_hint = None, None
        bt.height = 50
        bt.width = 200
        bt.y = 210
        bt.x = 300
        def callback(self):
#inserir codigo de reconhecimento facial-captura de fotos
            bt.bind(on_press=callback)


        bt2 = Button(text="Iniciar Treino")
        bt2.size_hint = None, None
        bt2.height = 50
        bt2.width = 200
        bt2.y = 150
        bt2.x = 300
        def callback(self):
# inserir codigo de treino
            bt2.bind(on_press=callback)


        bt3 = Button(text="Iniciar Reconhecimento")
        bt3.size_hint = None, None
        bt3.height = 50
        bt3.width = 200
        bt3.y = 90
        bt3.x = 300


        def callback(self):
# inserir codigo de visualização do reconhecimento
            bt3.bind(on_press=callback)

        c.add_widget(lbl)
        c.add_widget(bt)
        c.add_widget(bt2)
        c.add_widget(bt3)

        return c

Window.size = (800, 450)
Principal().run()