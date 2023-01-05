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
from ftplib import FTP
import zipfile
import os
import shutil
import pathlib

class Application(App):
	def build(self):
		self.window = GridLayout()
		self.window.cols=1
		self.window.size_hint = (1, 1)
		self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		
		#on créer l'objet fileSelector
		self.filechooser = FileChooserIconView(path="")
		self.filechooser.bind(on_submit =self.selected_file_menu)
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
		# creation du second bouton
		self.button2 = Button(text="Zip/Unzip", 
				size_hint = (1,0.1),
				on_press=self.buttonZip
		)
		# creation du troisieme bouton
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
	
	#enregistre le fichier selectionner 
	def selected_file_menu(self, instance, selection, touch):
		if selection :
			#enregistre le chemin du fichier selectionner
			self.selected_path = str(selection[0])
			#va nous permettre
			self.selected_file = self.selected_path.split('/')
			self.message.text = "Chemin du fichier selectionné :  " + str(selection[0])
			#shutil.copy(self.selected_path, './TPBINOME/get_ftp')
			
	def buttonFTP(self, instance):
		if self.selected_path :
			ftp = FTP('127.0.0.1')
			ftp.login("user", "12345")
			# Ouvrez le fichier en mode binaire
			with open(self.selected_path, "rb") as f:
				# Envoyez le fichier
				ftp.storbinary(f"STOR {self.selected_file[-1]}", f)
			ftp.quit()
			self.message.text = "Fichier envoyer au serveur FTP"

	def buttonQuit(self, instance):
		self.stop()

	def buttonZip(self, instance):
		pass
		
if __name__ == "__main__":
	Application().run()

