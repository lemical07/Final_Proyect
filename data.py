import json


inventory="inventory.json"


def save_data(product):
   with open (inventory, "w") as f:
       json.dump(product, f, indent =4)


def load_data():
   try:
       with open(inventory, "r") as f:
           return json.load(f)
   except(FileNotFoundError, json.JSONDecodeError):
       return[]