# pip install kivy

from tkinter.tix import ButtonBox
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
	def build(self):
		self.window = GridLayout()
		self.window.cols=1
		self.window.size_hint = (0.5, 0.5)
		self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		self.image = Image(source="2133.JPG")
		# on créer l'objet Label
		self.window.add_widget(self.image)
  
		self.message = Label(text="Bonjour de Malte")
		# on ajoute le label à la fenêtre
		self.window.add_widget(self.message)
		self.user = TextInput(text="", size_hint = (1,0.2), multiline = False)
		self.window.add_widget(self.user)
		# création de la zone des boutons
		self.buttonArea = GridLayout(cols=2, size_hint = (1,0.2))
		# création du premier bouton	
		self.button = Button(text="Say Hello", 
				size_hint = (1,0.2),
				on_press=self.buttonHello
		)
		# creation du second bouton
		self.buttonQuit = Button(text="Quit", 
				size_hint = (1,0.2),
				on_press=self.buttonQuit
		)
		# ajout des boutons à la zone des boutons
		self.buttonArea.add_widget(self.button)
		self.buttonArea.add_widget(self.buttonQuit)
		# ajout de la zone des boutons à la fenêtre
		self.window.add_widget(self.buttonArea)
		# affiche la fenetre construite	
		return self.window

	def buttonHello(self, instance):
		self.message.text = "Bonjour " + self.user.text

	def buttonQuit(self, instance):
		self.stop()

if __name__ == "__main__":
	SayHello().run()

if ButtonBox == 3:
    print("coucou")