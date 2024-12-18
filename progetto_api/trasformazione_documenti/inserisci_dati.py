import xml.etree.ElementTree as ET
import json

# Percorso del file XML
xml_path = "/home/mauro/Scrivania/dJANGO_apI/progetto_api/trasformazione_documenti/document.xml"

# Dati JSON direttamente all'interno del codice
json_data = {
  "dati_cantiere": {
    "committente": "Ferrovienord S.p.A.",
    "CUP_CIG": {
      "CIG": "9650328697",
      "CUP": "E31B21005960002"
    },
    "numero_commessa": "",
    "importo_lavori": "28.045.191,89 EUR",
    "ubicazione_cantiere": {
      "regione": "Toscana",
      "provincia": "Arezzo",
      "comune": "Arezzo",
      "indirizzo": "SS679 Raccordo Arezzo Battifolle km 6+250 lato sinistro",
      "coordinate": "43.444250, 11.796479",
      "riferimenti_catastali": ["Foglio N. 42 Mappale 417", "437", "525", "526", "527", "528"],
      "superficie": "circa 11.000 m²"
    },
    "oggetto_generale_lavori": "Realizzazione di una stazione di rifornimento a base di idrogeno per veicoli leggeri e pesanti",
    "data_inizio_lavori": "",
    "data_fine_lavori_prevista": "",
    "numero_persone_presenti": "",
    "categorie_OG_OS": []
  },
  "documentazione_contrattuale": {
    "capitolato": True,
    "computo_metrico": False,
    "cronoprogramma": False
  },
  # altre sezioni del JSON...
}

# Carica l'XML
tree = ET.parse(xml_path)
root = tree.getroot()

# Definisce lo spazio dei nomi corretto
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# Cerca il tag body usando lo spazio dei nomi
body = root.find("w:body", namespaces)

# Verifica se body è stato trovato
if body is None:
    print("Errore: Il tag <w:body> non è stato trovato nel file XML.")
else:
    # Crea un paragrafo per ogni voce del JSON
    def add_json_to_xml(parent, data):
        for key, value in data.items():
            p = ET.SubElement(parent, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p")
            r = ET.SubElement(p, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r")
            t = ET.SubElement(r, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t")

            if isinstance(value, dict):
                add_json_to_xml(p, value)  # Ricorsione per i dizionari
            else:
                t.text = f"{key}: {value}"  # Inserisci il testo

    # Aggiungi dati JSON come paragrafi nel corpo
    add_json_to_xml(body, json_data)

    # Salva le modifiche all'XML
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)
    print("Modifica completata con successo.")
