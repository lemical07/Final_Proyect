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
