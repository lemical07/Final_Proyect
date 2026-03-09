from body import*
from menu import main_menu, separator, ask_option


while True:
   separator()
   main_menu()
   separator()
   opc = ask_option()
   separator()
   if opc==1:
       add_product()
   elif opc ==2:
       product_list()
   elif opc==3:
       update_quantity()
   elif opc ==4:
       delete_product()
   elif opc ==5:
       calculate_total()
   elif opc ==0:
       print("Thank for use the program:)")
       break
   else:
       print("Invalid option:(")