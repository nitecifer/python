menu = {
  'pizza':340,
  'pasta':490,
  'macroni':450,
  'dosa':478,
  'idli':400,
    
}
print ("WELCOME TO KIRTI'S RESTURANT")
print( "pizza:Rs340\n pasta:Rs490\n macroni:Rs450\n dosa:Rs478\n idli:Rs400")

order_total= 0

item_1= input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print("your item {item_1}has been added to your  order")

 else:

    print("ordered item {item_1}is not avai;able yet!")

    another_order = input("do you want to add anoher item?(yes/no)")

    if another_order=="yes":
        item_2 = input ("enter the name of second item = ")
        if item_2 in menu:
      order_total += menu [item_2]
print ("Item{item_2} has been added to order")


else:

print("ordered item {item_2} is not available")
print("the total amount of item to pay is {order_total}")