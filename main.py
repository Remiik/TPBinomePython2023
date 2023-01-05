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
		self.window.size_hint = (1, 1)
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
		self.buttonArea = GridLayout(cols=3, size_hint = (1,0.2))
		# création du premier bouton	
		self.button = Button(text="Upload to FTP", 
				size_hint = (1,0.1),
				on_press=self.buttonFTP
		)
		self.button2 = Button(text="Send", 
				size_hint = (1,0.1),
				on_press=self.buttonSend
		)
		# creation du second bouton
		self.button3 = Button(text="Quit", 
				size_hint = (1,0.1),
				on_press=self.buttonQuit
		)
		# ajout des boutons à la zone des boutons
		self.buttonArea.add_widget(self.button)
		self.buttonArea.add_widget(self.button2)
		self.buttonArea.add_widget(self.button3)
		# ajout de la zone des boutons à la fenêtre
		self.window.add_widget(self.buttonArea)
		# affiche la fenetre construite	
		return self.window

	def buttonFTP(self, instance):
		self.message.text = "Bonjour " + self.user.text

	def buttonQuit(self, instance):
		self.stop()

	def buttonSend(self, instance):
		self.message.text = "Ca veux se tappe ou bien ??"

if __name__ == "__main__":
	SayHello().run()

if ButtonBox == 3:
    print("coucou")