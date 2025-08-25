import json
import os

class JsonDataManager:
    """
    Diese Klasse ist für das Lesen und Schreiben von JSON-Daten aus/in Dateien zuständig.
    Sie kapselt die Logik für den Dateizugriff, sodass andere Teile der Anwendung (wie app.py)
    sich nicht darum kümmern müssen, wie die Daten gespeichert oder geladen werden.
    Sie beinhaltet robuste Fehlerbehandlung für fehlende oder ungültige Dateien.
    """

    def __init__(self):
        """
        Der Konstruktor der Klasse. Für diesen Datenmanager sind keine spezifischen
        Initialisierungen von Instanzvariablen erforderlich.
        """
        pass

    def read_data(self, filepath):
        """
        Liest Daten aus einer JSON-Datei.
        Behandelt FileNotFoundError und json.JSONDecodeError robust.

        Args:
            filepath (str): Der vollständige Pfad zur JSON-Datei.
        Returns:
            list or dict: Die aus der Datei gelesenen Daten (Liste oder Dictionary).
                          Gibt eine leere Liste bei Fehlern oder fehlender Datei zurück.
        """
        if not os.path.exists(filepath):
            print(f"INFO: Datei nicht gefunden: {filepath}. Gebe leere Liste zurück.")
            return [] # Leere Liste zurückgeben, wenn die Datei nicht existiert

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Dieser Fehler tritt auf, wenn der Inhalt der Datei kein gültiges JSON ist.
            print(f"FEHLER: Ungültiges JSON in Datei: {filepath}. Gebe leere Liste zurück.")
            return []
        except Exception as e:
            # Fängt alle anderen unerwarteten Fehler beim Dateizugriff ab.
            print(f"FEHLER: Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}. Gebe leere Liste zurück.")
            return []

    def write_data(self, filepath, data):
        """
        Schreibt Daten in eine JSON-Datei.
        Stellt sicher, dass das Zielverzeichnis existiert.

        Args:
            filepath (str): Der vollständige Pfad zur JSON-Datei.
            data (list or dict): Die Daten, die in die Datei geschrieben werden sollen.
        """
        # Sicherstellen, dass das Verzeichnis existiert, bevor geschrieben wird
        # exist_ok=True verhindert einen Fehler, wenn das Verzeichnis bereits existiert.
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                # json.dump schreibt die Python-Daten als JSON-Text in die Datei.
                # indent=4 macht die JSON-Ausgabe besser lesbar.
                # ensure_ascii=False stellt sicher, dass Nicht-ASCII-Zeichen (z.B. Umlaute) korrekt geschrieben werden.
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"FEHLER: Ein unerwarteter Fehler ist aufgetreten beim Schreiben von {filepath}: {e}")

