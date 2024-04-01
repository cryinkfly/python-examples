# The structur of the programm must be:

# ./demo
# ./demo/demo.py
# ./demo/locales/en/LC_MESSAGES/demo.po <-- The variables in this file are created by yourself or via a command.
# ./demo/locales/en/LC_MESSAGES/demo.mo <-- Must be created/updated with a command* via the terminal after each change to the .po file!
# ./demo/locales/de/LC_MESSAGES/demo.po <-- The variables in this file are created by yourself or via a command.
# ./demo/locales/de/LC_MESSAGES/demo.mo <-- Must be created/updated with a command* via the terminal after each change to the .po file!
# ./demo/locales/fr/LC_MESSAGES/demo.po <-- The variables in this file are created by yourself or via a command.
# ./demo/locales/fr/LC_MESSAGES/demo.mo <-- Must be created/updated with a command* via the terminal after each change to the .po file!

# ------------------------------------------ #
# For example ./demo/locales/en/LC_MESSAGES/demo.po:
# msgid "Hello"
# msgstr ""

# For example ./demo/locales/de/LC_MESSAGES/demo.po:
# msgid "Hello"
# msgstr "Hallo"

# For example ./demo/locales/fr/LC_MESSAGES/demo.po:
# msgid "Hello"
# msgstr "Bonjour"

# *: msgfmt -o locales/en/LC_MESSAGES/demo.mo locales/en/LC_MESSAGES/demo.po
# *: msgfmt -o locales/de/LC_MESSAGES/demo.mo locales/de/LC_MESSAGES/demo.po
# *: msgfmt -o locales/fr/LC_MESSAGES/demo.mo locales/fr/LC_MESSAGES/demo.po

import gettext

def main():
    language = input("Select language (de/en/fr): ").strip().lower()
    
    # Setting up gettext
    translations = gettext.translation('demo', localedir='locales', languages=[language], fallback=True)
    translations.install()
    
    # Translating and displaying "Hello" based on selected language
    print(_("Hello"))
    print(_("Goodbye"))


if __name__ == "__main__":
    main()
