import xml.etree.ElementTree as ET

# Percorso del file XML
xml_path = "/home/mauro/Scrivania/dJANGO_apI/progetto_api/trasformazione_documenti/document.xml"

# Carica l'XML
tree = ET.parse(xml_path)
root = tree.getroot()

# Stampa i tag di primo livello per capire la struttura e gli spazi dei nomi
for child in root:
    print(f"Tag: {child.tag}")

