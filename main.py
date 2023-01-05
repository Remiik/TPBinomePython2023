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
from zipfile import ZipFile
import pathlib

class Application(App):
	def build(self):
		self.window = GridLayout()
		self.window.cols=1
		self.window.size_hint = (1, 1)
		self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		
		#on créer l'objet fileSelector
		self.selected_path = ""
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
			#va nous permettre de récuperer le nom du fichier avec self.selected_file[-1]
			self.selected_file = self.selected_path.split('\\')
			#on change le texte afficher a l'écran
			self.message.text = "Chemin du fichier selectionné :  " + str(selection[0])
		
			
	def buttonFTP(self, instance):
		#si un fichier a été sélectionner
		if self.selected_path :
			#Connection au serveur ftp
			ftp = FTP('127.0.0.1')
			ftp.login("user", "12345")
			# Ouvrez le fichier en mode binaire
			with open(self.selected_path, "rb") as f:
				# Envoyez le fichier
				ftp.storbinary(f"STOR {self.selected_file[-1]}", f)
			#on se deconnecte du serveur ftp
			ftp.quit()
			#on change le message affiché a l'écran
			self.message.text = "Fichier envoyer au serveur FTP"
		else : 
			self.message.text = "Veuillez selectionnez un fichier"

	def deleteFtp(self, instance):
		#si le fichier se trouve dans get_ftp
		if self.selected_path in "/get_ftp/" : 
			#On se connecte au serveur ftp
			ftp = FTP('127.0.0.1')
			ftp.login("user", "12345")
			#on supprime le fichier selectionner
			ftp.delete(self.selected_file[-1])
		else : 
			"Selectionnez un fichier dans get_ftp"

	#on quitte l'application
	def buttonQuit(self, instance):
		self.stop()
	#compresse ou décompresse un fichier en fonction de son état 
	def buttonZip(self, instance):
		if pathlib.Path(str(self.selected_file)).suffix == ".rar']" or pathlib.Path(str(self.selected_file)).suffix == ".zip']":
		#Décompression du fichier
			with ZipFile(str(self.selected_file[-1]), 'r') as zip:
				#On écrit tout le contenu du fichier ZIP
				zip.printdir()
				#extraction des fichiers dézippés
				zip.extractall()
				self.message.text = "Dossier ZIP décompressé."
		else:
		#Compression du fichier
			with ZipFile(str(self.selected_file[-1]) + '.zip','w') as zip:
				#On compresse le fichier unique sélctionné
				zip.write(str(self.selected_file[-1]))
				self.message.text = "Fichier compressé en fichier ZIP."
		self.filechooser._update_files()
	
		
if __name__ == "__main__":
	Application().run()

