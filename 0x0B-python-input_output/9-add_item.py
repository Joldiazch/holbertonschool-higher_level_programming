#!/usr/bin/python3
import json
from sys import argv

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
try:
    lista = load_from_json_file("add_item.json")
except:
    lista = []
finally:
    for idx in range(1, len(argv)):
        lista.append(argv[idx])

    save_to_json_file(lista, "add_item.json")
