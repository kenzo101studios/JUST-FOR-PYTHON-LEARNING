#INPUT FOR SCRIPT

print("Hello, Welcome To The Coffee Shop.")

#BASICS

name = input("What Is Your NAME? \n")

print("Hello " + name + "! Welcome To The Coffee Shop! \n \n \n")

menu = "Espresso, Latte, Cappuccino, Frappuccino, Tea, Coffee, Hot Chocolate, Water"

print("Here Is Our Menu: \n " + menu)

order = input("\n What Would You Like To Order? \n")

print("Sounds Good " + name + "! We Will Have That " + order +
       " Ready For You In A Moment.")

#MORE VARIABLES

price = 5

quantity = input("How Many Would You Like? \n")

total = int(price) * int(quantity)

#TOTAL PRICE

print("Thank You. Your Total Is: \n")
print("$" + str(total))
