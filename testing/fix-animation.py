# Skript zum Lesen von parrot.py, Hinzufügen von Anführungszeichen und Speichern in einer neuen Datei

def add_quotes_to_parrot():
    # Pfad zur Originaldatei
    input_file_path = '../parrot.py'
    # Pfad zur neuen Datei
    output_file_path = 'quoted_parrot.py'

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Beginn der Bearbeitung jeder Zeile
        quoted_lines = []
        for line in lines:
            # Entfernen des Zeilenumbruchs am Ende und Hinzufügen von Anführungszeichen
            new_line = f'"{line.rstrip()}"\n'
            quoted_lines.append(new_line)

        # Schreiben der bearbeiteten Zeilen in die neue Datei
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(quoted_lines)

        print(f"Datei erfolgreich bearbeitet und gespeichert als {output_file_path}")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Funktion ausführen
add_quotes_to_parrot()