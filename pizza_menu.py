import tkinter as tk


# This function prints the order
def ask_details(m, cost):
    def print_order():
     
        receipts = open("orders.txt", "a")
        p1 = pizza_1.get()
       
        if(p1 == "Choose a Pizza"):
            p1 = ""

        p2 = pizza_2.get()

        if(p2 == "Choose a Pizza"):
            p2 = ""

        p3 = pizza_3.get()

        if(p3 == "Choose a Pizza"):
            p3 = ""

        p4 = pizza_4.get()

        if(p4 == "Choose a Pizza"):
            p4 = ""

        p5 = pizza_5.get()

        if(p5 == "Choose a Pizza"):
            p5 = ""

        pizzas_selected = []

        if p1 !="":
            pizzas_selected.append(p1)
        if p2 !="":
            pizzas_selected.append(p2)
        if p3 !="":
            pizzas_selected.append(p3)
        if p4 !="":
            pizzas_selected.append(p4)
        if p5 !="":
            pizzas_selected.append(p5)
       # if pickup
        if(var.get() == 1):
            
                if not any(i.isdigit() for i in name.get()):
            
                    receipts.write("Transport Method : Pickup, Name : {}, Order : {}, Total Cost : ${}\n".format(name.get(), pizzas_selected, cost))
                    print(p1)
                    print("Name entered, Address entered, Phone number entered")
                    details.destroy()
                
                else:
                    print("Error")
        
        elif(var.get() == 2):
            
            if not any(i.isdigit() for i in name.get()) and number.get().isnumeric() and len(name.get())!=0 and len(address.get())!=0 and len(number.get())>0:
                receipts.write("Transport Method : Delivery, Name : {}, Address : {}, Number : {}, Order : {}, Total Cost : ${}\n".format(name.get(), address.get(), number.get(), pizzas_selected , cost))
                print("Name entered, Address entered, Phone number entered")
                details.destroy()
           
            else:
                print("Error")
        receipts.close()
       
       # if pickup it opens a new windown asking for your name
    if(m == "p"):
        details = tk.Toplevel(root)
        
        label_name = tk.Label(details, text = "Name")
        label_name.grid(row = 0, column = 0)
        
        name = tk.Entry(details)
        name.grid(row = 0, column = 1)
        
        message = tk.Label(details, text = "Total Cost : ${}".format(cost))
        message.grid(row = 1, column = 0, columnspan = 2)
        
        submit_order = tk.Button(details, text = "Submit order", command = print_order)
        submit_order.grid(row = 2, column = 0, columnspan = 2)
        
        
        # if delivery it opens up a new window asking for information
    elif(m == "d"):
        details = tk.Toplevel(root)
        
        label_name = tk.Label(details, text = "Name")
        label_name.grid(row = 0, column = 0)
        
        # This is where you enter your name
        name = tk.Entry(details)
        name.grid(row = 0, column = 1)
        
        label_address = tk.Label(details, text = "Address")
        label_address.grid(row = 1, column = 0)
        
        # This is where you enter your adress
        address = tk.Entry(details)
        address.grid(row = 1, column = 1)
        
        label_number = tk.Label(details, text = "Number")
        label_number.grid(row = 2, column = 0)
        
        # This is where you enter you number
        number = tk.Entry(details)
        number.grid(row = 2, column = 1)
        
        message = tk.Label(details, text = "Total Cost : ${}".format(cost))
        message.grid(row = 3, column = 0, columnspan = 2)
        
        submit_order = tk.Button(details, text = "Submit order", command = print_order)
        submit_order.grid(row = 4, column = 0, columnspan = 2)

        
      # this function calculates the cost
def calculate():
    cost = 0
    
    if(var.get() == 2):
        cost += 3
    
    # This is the list of regular and gourmet pizzas
    regular = ["Cheesy Garlic", "Hawaiian", "Pepperoni", "Cheese", "Meat Lovers", "Beef & Onion", "Vegetarian"]    
    gourmet = ["Peri peri chicken", "Garlic prawn", "Apricot Chicken", "Chicken and camemebert", "Chicken & Cranberry"] 
    
    # This sets the price of my pizzas
    if(pizza_1.get() in regular):
        cost += 8.5
    elif(pizza_1.get() in gourmet):
        cost += 13.5
        
    if(pizza_2.get() in regular):
        cost += 8.5
    elif(pizza_2.get() in gourmet):
        cost += 13.5
    
    if(pizza_3.get() in regular):
        cost += 8.5
    elif(pizza_3.get() in gourmet):
        cost += 13.5
        
    if(pizza_4.get() in regular):
        cost += 8.5
    elif(pizza_4.get() in gourmet):
        cost += 13.5
        
    if(pizza_5.get() in regular):
        cost += 8.5
    elif(pizza_5.get() in gourmet):
        cost += 13.5
    
    # This sums up the total cost of the order
    total_cost.configure(text = "${}".format(cost))

  # Pickup
    if(var.get() == 1):
        ask_details("p", cost)
        
    # Delivery
    elif(var.get() == 2):
        ask_details("d", cost)

root = tk.Tk()

root.iconbitmap('pizza_logo.ico')

# This changes the colour of the background
root.configure(background = "#FB9DFF")

#  This chnages the title of my pizza menu
root.title("Heavens Pizza")

# This sets the value of the radiobutton
var = tk.IntVar()
var.set(0)

 # These are the pizza choices
pizzas = ["Cheesy Garlic", "Hawaiian", "Butter Chicken", "Pepperoni", "Cheese", "Meat lovers", "Beef & Onion", "Vegetarian", "Peri peri Chicken", "Garlic prawn", "Apricot Chicken", "Chicken and camemebert", "Chicken & Cranberry"]

# This sets the font style and size
title_label = tk.Label(text = "Heavens Pizza", font = ("Arial", 16))
title_label.grid ( row = 0, column = 0, columnspan = 2)
 
# This changes the colour of the label
title_label.configure(background = "#FB9DFF")
 
# This changes the name of the option menus
pizza_1 = tk.StringVar()
pizza_1.set("Choose a pizza")

pizza_2 = tk.StringVar()
pizza_2.set("Choose a pizza")

pizza_3 = tk.StringVar()
pizza_3.set("Choose a pizza")

pizza_4 = tk.StringVar()
pizza_4.set("Choose a pizza")
 
pizza_5 = tk.StringVar()
pizza_5.set("Choose a pizza")
 
# This is the pizza menu for regular pizzas
menu_label = tk.Label(text = "Regular pizza's $8.50\n\n Chessy Garlic\n Hawaiian\n Butter Chicken\n Pepperoni\n Cheese\n Meat lovers\n Beef & Onion\n Vegetarian", font = ("Arial", 12))
menu_label.grid ( row = 1, column = 0)
 
# This changes the colour of the menu
menu_label.configure(background = "#FB9DFF")
 
menu_label2 = tk.Label(text = "Gourmet pizza's $13.50\n\n\n\n Peri peri Chicken\n Garlic prawn\n Apricot Chicken\n Chicken\n camemebert\n Chicken & Cranberry", font = ("Arial", 12))
menu_label2.grid ( row = 1, column = 1)
 
menu_label2.configure(background = "#FB9DFF")
 
# This is the pickup Radiobutton
pickup = tk.Radiobutton(root, text = "Pickup", variable = var, value = 1)
pickup.grid(row = 2, column = 0)

# This is the delivery button
delivery = tk.Radiobutton(root, text = "Delivery", variable = var, value = 2)
delivery.grid(row = 2, column = 1)

menu_label = tk.Label(root, text = "Regular")

# These are option menus that have a list of all regular and gourmet pizzas
pizza_menu_1 = tk.OptionMenu(root, pizza_1, *pizzas)
pizza_menu_1.grid(row = 4, column = 0, columnspan = 2)

pizza_menu_2 = tk.OptionMenu(root, pizza_2, *pizzas)
pizza_menu_2.grid(row = 5, column = 0, columnspan = 2)

pizza_menu_3 = tk.OptionMenu(root, pizza_3, *pizzas)
pizza_menu_3.grid(row = 6, column = 0, columnspan = 2)


pizza_menu_4 = tk.OptionMenu(root, pizza_4, *pizzas)
pizza_menu_4.grid(row = 7, column = 0, columnspan = 2)

pizza_menu_5 = tk.OptionMenu(root, pizza_5, *pizzas)
pizza_menu_5.grid(row = 8, column = 0, columnspan = 2)

# This is the calculate button
calculate_button = tk.Button(root, text = "Calculate", command = calculate)
calculate_button.grid(row = 9, column = 0, columnspan = 2)

# This calculates the total cost of your order
total_cost = tk.Label(root, text = "$")
total_cost.grid(row = 10, column = 0, columnspan = 2)

root.mainloop()