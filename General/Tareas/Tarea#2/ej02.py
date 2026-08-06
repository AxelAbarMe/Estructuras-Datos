# Escriba un programa en Python que permita guardar y recuperar datos de archivos en los tres formatos: XML, JSON, YAML. Ustedes pueden utilizar los datos que deseen en estos archivos.

import json
import yaml
import xml.etree.ElementTree as ET

FILE_JSON = "data.json"
FILE_YAML = "data.yaml"
FILE_XML = "data.xml"

inv = {
    "shop": "Store",
    "items": [
        {"code": "001", "name": "item1", "price": 10.99, "quantity": 5},
        {"code": "002", "name": "item2", "price": 5.49, "quantity": 10},
        {"code": "003", "name": "item3", "price": 20.00, "quantity": 3},
    ],
}

def save_json(data, filename=FILE_JSON):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_json(filename=FILE_JSON):
    with open(filename, "r") as f:
        return json.load(f)

def save_yaml(data, filename=FILE_YAML):
    with open(filename, "w") as f:
        yaml.dump(data, f, sort_keys=False)

def load_yaml(filename=FILE_YAML):
    with open(filename, "r") as f:
        return yaml.safe_load(f)

def save_xml(data, filename=FILE_XML):
    root = ET.Element("inventory")
    shop = ET.SubElement(root, "shop")
    shop.text = data["shop"]
    items = ET.SubElement(root, "items")
    for item in data["items"]:
        item_elem = ET.SubElement(items, "item")
        for key, value in item.items():
            sub_elem = ET.SubElement(item_elem, key)
            sub_elem.text = str(value)
    ET.indent(root, space="  ")
    tree = ET.ElementTree(root)
    tree.write(filename)

def load_xml(filename=FILE_XML):
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {"shop": root.find("shop").text, "items": []}
    for item_elem in root.find("items"):
        item = {
            "code": item_elem.find("code").text,
            "name": item_elem.find("name").text,
            "price": float(item_elem.find("price").text),
            "quantity": int(item_elem.find("quantity").text),
        }
        data["items"].append(item)
    return data

def main():
    save_json(inv)
    save_yaml(inv)
    save_xml(inv)

    print("Data saved in JSON, YAML, and XML formats.")

    loaded_json = load_json()
    loaded_yaml = load_yaml()
    loaded_xml = load_xml()

    print("\nLoaded JSON data:")
    print(loaded_json)
    print("\nLoaded YAML data:")
    print(loaded_yaml)
    print("\nLoaded XML data:")
    print(loaded_xml)

if __name__ == "__main__":
    main()