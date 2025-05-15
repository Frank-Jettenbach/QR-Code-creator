# QR-Code Creator für Topstick 8697

Dieses Python-Script erstellt ein druckbares PDF mit 65 QR-Codes im Layout des Etikettenbogens **Topstick 8697 (38,1 x 21,2 mm, 65 Etiketten pro DIN A4-Seite)**.  
Die QR-Codes können zur automatisierten Dokumentenerkennung oder als Trennetiketten in Systemen wie **Paperless-ngx** verwendet werden.

---

## ✅ Funktionen

- Exakte Anordnung für Topstick 8697 (5 Spalten × 13 Zeilen)
- Ausgabe als druckbares **PDF**
- Eingebaute Nummerierung der QR-Codes (`ASN10000` bis `ASN10064`)
- Keine manuelle Formatierung erforderlich – einfach drucken
- Leicht anpassbar (andere Texte, Startwerte, Anzahl)

---

## ▶️ Verwendung

### 1. Abhängigkeiten installieren

Installiere die benötigten Python-Bibliotheken mit:

```
pip install -r requirements.txt
```

### 2. Script ausführen

Starte das Script mit:

```
python3 create_topstick_65_8697.py
```

### 3. Ergebnis

Das Script erstellt eine Datei `etiketten.pdf` im aktuellen Verzeichnis –  
bereit zum Ausdruck auf einem Etikettenbogen vom Typ **Topstick 8697**.

---

## 🔧 Konfiguration im Script

Im Script kannst du die Inhalte der QR-Codes anpassen. Standardmäßig werden 65 fortlaufende ASN-Nummern generiert:

```python
daten = [f"ASN{10000+i}" for i in range(65)]
```

Du kannst:
- die Startnummer ändern (z. B. `ASN20000`)
- die Anzahl der Codes reduzieren
- beliebige Inhalte (Texte, URLs, Seriennummern) verwenden

---

## 📏 Etikettenlayout

- **Etiketten pro Seite**: 65 (5 Spalten × 13 Reihen)
- **Etikettengröße**: 38,1 mm × 21,2 mm
- **Seitenformat**: DIN A4
- **Ränder und Abstände**: abgestimmt auf Topstick 8697

---

## 📂 Projektstruktur

```
QR-Code-creator/
├── create_topstick_65_8697.py    # Hauptscript zur QR-Code-Erzeugung
├── requirements.txt              # Benötigte Python-Bibliotheken
└── README.md                     # Diese Dokumentation
```

---

## 💡 Erweiterungsideen

- Startnummer und Anzahl als Parameter übergeben (`--start`, `--anzahl`)
- Automatischer Zeilenumbruch auf mehrere Seiten (> 65 Codes)
- Integration mit einer CSV-Datei für benutzerdefinierte Inhalte
- Vorschauanzeige der Etiketten vor dem Druck (z. B. als HTML oder Bild)

---

## 📜 Lizenz

MIT – Dieses Projekt darf frei verwendet, verändert und weitergegeben werden – privat oder kommerziell.
