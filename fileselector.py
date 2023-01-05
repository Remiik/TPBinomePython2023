import kivy
from kivy.app import App
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import os

class FileSelectorApp(App):
    def build(self):
        filechooser = FileChooserListView(path="")
        filechooser.bind(on_submit=self.selected)
        return filechooser

    def selected(self, instance, selection, touch):
        """Affiche un message de confirmation de sélection de fichier."""
        if selection:
            selected_file = selection[0]
            content = Label(text=f"Voulez-vous sélectionner le fichier {selected_file} ?")
            popup = Popup(title="Confirmation de sélection", content=content, size_hint=(0.5, 0.5))
            content.bind(on_ref_press=popup.dismiss)
            popup.open()
        else:
            # Si aucun élément n'est sélectionné, affichage d'une boîte de dialogue d'erreur
            content = Label(text="Vous devez sélectionner un fichier pour pouvoir le sélectionner.")
            popup = Popup(title="Erreur", content=content, size_hint=(0.5, 0.5))
            content.bind(on_ref_press=popup.dismiss)
            popup.open()

if __name__ == "__main__":
    FileSelectorApp().run()
