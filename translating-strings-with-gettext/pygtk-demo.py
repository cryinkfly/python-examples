import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import gettext

class LanguageSelectionWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Language Selection")

        self.set_border_width(10)

        vbox = Gtk.VBox(spacing=6)
        self.add(vbox)

        self.language_label = Gtk.Label(label="Select language (de/en/fr):")
        vbox.pack_start(self.language_label, True, True, 0)

        self.language_combo = Gtk.ComboBoxText()
        self.language_combo.append_text("de")
        self.language_combo.append_text("en")
        self.language_combo.append_text("fr")
        self.language_combo.set_active(1)  # Default to English
        vbox.pack_start(self.language_combo, True, True, 0)

        self.hello_label = Gtk.Label(label="Hello")
        vbox.pack_start(self.hello_label, True, True, 0)

        self.goodbye_label = Gtk.Label(label="Goodbye")
        vbox.pack_start(self.goodbye_label, True, True, 0)

        button = Gtk.Button(label="Submit")
        button.connect("clicked", self.on_submit_clicked)
        vbox.pack_start(button, True, True, 0)

    def on_submit_clicked(self, button):
        language = self.language_combo.get_active_text()
        translations = gettext.translation('demo', localedir='locales', languages=[language])
        translations.install()
        self.hello_label.set_label(_("Hello"))
        self.goodbye_label.set_label(_("Goodbye"))

def main():
    win = LanguageSelectionWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
