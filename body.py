from data import save_data, load_data


def add_product():
   product= load_data()
   print("---Add new product---")
   name = input("Product name:_")
   try:
       price= float(input("Product price:_"))
       quantity=int(input("Product quantity:_"))
       product.append({"Name":name, "Price": price, "Quantity": quantity})
       save_data(product)
       print(f"Registered '{name}' product!!")
   except ValueError:
       print("Error:( Introduce only number in this section.")

def product_list():
   product = load_data()
   print("\n---Product Inventory---")
   if not product:
       print("Inventory is empty.")
       return
   for i, p in enumerate(product, 1):
       print(f"\n{i}. {p['Name']}\nPrice: {p['Price']}\nQuantity: {p['Quantity']}")
       
def update_quantity():
   product = load_data()
   name = input("Name of the product to modify:_")
   for p in product:
       if p['Name'].lower() == name.lower():
           try:
               p['Quantity'] = int(input(f"New quantity for {p['Name']}: "))
               save_data(product)
               print("Updated quantity.")
               return
           except ValueError:
               print("Error:( Invalid quantity.")
               return
   print("Product not found.")