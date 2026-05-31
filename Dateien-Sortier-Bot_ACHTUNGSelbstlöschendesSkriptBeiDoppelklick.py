from pathlib import Path
import shutil
import os

# Dieses Skript hier in den Ordner ziehen, wo sortiert werden soll.
# Dann mit Python in der Konsole ausführen in dem Ordner.

# Ordner nehmen, wo dieses Skript liegt, verwenden:
dateipfad = Path(__file__).parent
dieser_ordner = Path(dateipfad)

for datei in dieser_ordner.iterdir():
    if datei.is_file() and datei != Path(__file__):
        endung = datei.suffixes[-1].lower()
        # Keine Endung (z.B. Dateien ohne Punkt) in Extra‑Ordner
        if not endung:
            zielordner = dieser_ordner / "Dateien ohne Endung"
        else:
            # Alle Teile nach Punkt in Unterordner-Namen umwandeln
            endung_sauber = endung.lstrip(".").replace(".", "_")
            zielordner = dieser_ordner / endung_sauber

        # Zielordner anlegen, falls noch nicht vorhanden
        zielordner.mkdir(exist_ok=True)
        # Datei verschieben
        shutil.move(str(datei), str(zielordner / datei.name))

print("Sortierung nach Dateiendungen wurde abgeschlossen.")

# Skript selbst löschen (nur wenn es als .py ausgeführt wird)
if __name__ == "__main__" and Path(__file__).suffix.lower() == ".py":
    try:
        os.remove(__file__)
        # print("Skript-Datei wurde gelöscht.")
    except PermissionError:
        print("Konnte Skript-Datei nicht löschen (evtl. noch geöffnet).")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten beim Löschen der Skript-Datei:\n{e}")