from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from DAO.conexao import db
from telaPrincipal import Principal
import telaPrincipal

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

        usuario = TextInput()
        usuario.size_hint = None, None
        usuario.height = 30
        usuario.width = 300
        usuario.y = 250
        usuario.x = 250

        senha = TextInput()
        senha.size_hint = None, None
        senha.height = 30
        senha.width = 300
        senha.y = 180
        senha.x = 250
        senha.password = True

        bt = Button(text="Acessar")
        bt.size_hint = None, None
        bt.height = 50
        bt.width = 200
        bt.y = 90
        bt.x = 300

        c.add_widget(lbl)
        c.add_widget(lbl2)
        c.add_widget(lbl3)
        c.add_widget(usuario)
        c.add_widget(senha)
        c.add_widget(bt)

        def callback(self):

            cursor = db.cursor()
        # Executa a consulta na tabela selecionada
            cursor.execute("SELECT * FROM inteligenciaArtificialDB.tb_usuarios")
        # Laco for para retornar os valores, ex.: row[0] primeira coluna, row[1] segunda coluna, row[2] terceira coluna, etc.
            for row in cursor.fetchall():
                if usuario.text == row[1] and senha.text == row[2]:
                    popup = Popup(title='Logado', content=Label(text='Logon realizado com sucesso!'),
                                  size_hint=(None, None),
                                  size=(250, 150),
                                  auto_dismiss=True)
                    popup.open()
                    #abre janela principal
                    Principal().run()

        bt.bind(on_press=callback)

        return c

Window.size = (800, 450)
Login().run()