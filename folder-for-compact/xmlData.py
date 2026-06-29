import xml.etree.ElementTree as ET
import json
import pandas as pd

# get tournaments.json as list
with open("tournaments.json", "r", encoding="utf-8") as f:
    tournaments_json = json.load(f)

# create root element
root = ET.Element('tournaments')

# append subElements
for item in tournaments_json:
    t = ET.SubElement(root, "tournament")

    ET.SubElement(t, 'id').text = str(item['id'])
    ET.SubElement(t, 'fullName').text = item['fullName']
    ET.SubElement(t, 'nbPlayers').text = str(item['nbPlayers'])

# create tree 
tree = ET.ElementTree(root)
# create xml file
tree.write("tournaments.xml", encoding='utf-8', xml_declaration=True)

# get tree and root el from tournaments.xml"
getTree = ET.parse("tournaments.xml")
getRoot = getTree.getroot()

# xml data list
data_xml = []

# append data from gotten root to the list
for item in getRoot.findall("tournament"):
    data_xml.append({
        "id": "https://lichess.org/tournament/" + item.find("id").text,
        "fullName": item.find("fullName").text,
        "nbPlayers": int(item.find("nbPlayers").text)
    })

# convert to pandas for analysis
df_xml = pd.DataFrame(data_xml)

print(df_xml.head())