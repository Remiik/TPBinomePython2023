# pip install kivy

from tkinter.tix import ButtonBox
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import zipfile
import os


class SayHello(App):
	def build(self):
		self.window = GridLayout()
		self.window.cols=1
		self.window.size_hint = (1, 1)
		self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		
		#on créer l'objet fileSelector
		self.filechooser = FileChooserIconView(path="TPBINOME")
		self.filechooser.bind(on_submit =self.selected_file)
		self.window.add_widget(self.filechooser)

		#ajout d'un champ text
		self.message = Label(text="Chemin du fichier sélectionné : ")
		self.window.add_widget(self.message)
		# création de la zone des boutons
		self.buttonArea = GridLayout(cols=3, size_hint = (1,0.2))
		# création du premier bouton	
		self.button = Button(text="Upload to FTP", 
				size_hint = (1,0.1),
				on_press=self.buttonFTP
		)
		self.button2 = Button(text="Zip/Unzip", 
				size_hint = (1,0.1),
				on_press=self.buttonZip
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

	def selected_file(self, instance, selection, touch):
		if selection :
			self.selected_file = selection[0]
			self.message.text = "Chemin du fichier selectionné :  " + str(selection[0])
	
	def buttonFTP(self, instance):
		pass
	def buttonQuit(self, instance):
		self.stop()

	def buttonZip(self, instance):
		self.message.text = ""

if __name__ == "__main__":
	SayHello().run()

if ButtonBox == 3:
    print("coucou")