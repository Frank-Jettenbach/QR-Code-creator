import qrcode
import qrcode.image.pil
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import os

# Topstick 8697 Etikettenlayout (5 Spalten × 13 Reihen = 65 Etiketten pro Bogen)
cols, rows = 5, 13
labels_per_page = cols * rows
label_width = 38.1 * mm
h_spacing = 2.5 * mm       # Horizontaler Abstand

# Eingabe: Ober-/Unterrand
try:
    rand_input = input("Rand oben/unten in mm? [Standard: 5]: ").strip()
    seitenrand_mm = float(rand_input) if rand_input else 5.0
except ValueError:
    print("Ungültige Eingabe – verwende Standardwert 5 mm")
    seitenrand_mm = 5.0

margin_left = 7.25 * mm
margin_top = seitenrand_mm * mm
usable_height = A4[1] - 2 * margin_top
label_height = usable_height / rows
v_spacing = 0.0 * mm  # wird rechnerisch durch die Zeilenaufteilung ersetzt

# Eingabe: QR-Code-Größe
try:
    qr_size_input = input("QR-Code-Größe in mm? [Standard: 15]: ").strip()
    qr_size = float(qr_size_input) * mm if qr_size_input else 15 * mm
except ValueError:
    print("Ungültige Eingabe – verwende Standardwert 15 mm")
    qr_size = 15 * mm

# Eingabe: Startnummer
try:
    start_nummer = int(input("Startnummer (z. B. 155): "))
except ValueError:
    print("Ungültige Eingabe – verwende Standardwert 155")
    start_nummer = 155

# Eingabe: Anzahl der Bögen
try:
    boegen = int(input("Wie viele Bögen drucken? [Standard: 1]: "))
except ValueError:
    boegen = 1

# Eingabe: Rahmen anzeigen?
rahmen_eingabe = input("Rahmen um Etiketten anzeigen? (j/n) [Standard: n]: ").strip().lower()
zeige_rahmen = rahmen_eingabe == "j"

# Gesamtanzahl Labels
anzahl_labels = boegen * labels_per_page

# Ausgabe
output_pdf = "asn_labels_topstick8697.pdf"
tmp_dir = "./tmp_qr"
os.makedirs(tmp_dir, exist_ok=True)
c = canvas.Canvas(output_pdf, pagesize=A4)

for n in range(anzahl_labels):
    nummer = start_nummer + n
    asn_label = f"ASN{nummer:05}"

    # QR-Code erzeugen mit hoher Auflösung
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=1
    )
    qr.add_data(asn_label)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    qr_path = os.path.join(tmp_dir, f"{asn_label}.png")
    img.save(qr_path)

    # Position berechnen
    pos_on_page = n % labels_per_page
    col = pos_on_page % cols
    row = pos_on_page // cols

    if pos_on_page == 0 and n != 0:
        c.showPage()

    x = margin_left + col * (label_width + h_spacing)
    y = A4[1] - margin_top - (row + 1) * label_height

    # Rahmen (optional)
    if zeige_rahmen:
        c.setLineWidth(0.3)
        c.rect(x, y, label_width, label_height)

    # Inhalt platzieren: QR links, Text rechts mittig (ohne "ASN")
    qr_x = x + 1.5 * mm
    qr_y = y + (label_height - qr_size) / 2
    text_x = qr_x + qr_size + 2 * mm
    text_y = y + (label_height - 7) / 2  # Vertikal zentriert bei Schriftgröße 7 pt

    # Bild exakt skalieren
    c.drawImage(qr_path, qr_x, qr_y, width=qr_size, height=qr_size, preserveAspectRatio=False, mask='auto')
    c.setFont("Helvetica", 7)
    c.drawString(text_x, text_y, f"{nummer:05}")

c.save()
print(f"✅ PDF mit {anzahl_labels} Etiketten ({boegen} Bogen) erstellt: {output_pdf}")
