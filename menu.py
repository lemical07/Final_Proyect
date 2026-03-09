def main_menu():
   menu="""
   1._Add products
   2._List products
   3._Update quantity
   4._Delete product
   5._Calculate total value of the inventory
   0._Out to program
"""
   print (menu)


def separator ():
   print("="*25)


def ask_option ():
   while True:
       try:
           opc = int(input("Enter an option:_"))
           return opc
       except ValueError:
           print("Error:( Enter only number:_")