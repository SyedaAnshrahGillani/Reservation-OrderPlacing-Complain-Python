# RESERVATION / ORDER PLACING & COMPLAINING SYSTEM
def reservation():
    seats_available="4 per Table"
    reserved_seats=0
    tables_available=5
    table_no=0
   
    ask=input("Do you want to reserve a table? :")
    if ask=="yes":
         print("Following are the seats available : ",seats_available,"\nTotal tables available: ",tables_available,"\n")
         if tables_available<=5:
             a=int(input("Which table number you'll like to reserve: "))
             table_no=a
             print("----------------------------------------------------------------")
             print("Table Number ",table_no,"is reserved for you. ")
             print("----------------------------------------------------------------")
    else:
        print("----------------------------------------------------------------")
        print("Come back when you'll like to reserve a Table! ")
        print("----------------------------------------------------------------")
def order():
    ask=input("Would you like to order food? : ")
    while True:
        menu="1.pizza\n2.burger\n3.pasta\n4.Ice cream\n5.Cold Coffee\n6.Oreo Shake\n7.Chicken Soup\n8.Cold drink"
        items=["pizza","burger","pasta","Ice cream","Cold Coffee","Oreo Shake","Chicken Soup","Cold drink"]
        price=["700","380","350","220","165","170","250","90"]
        #ask=input("Would you like to order food? : ")
    
        if ask=="yes":
            print("Menu: \n",menu)
            order=int(input("Enter the item you'll like to order: "))
            a=order-1
            print("----------------------------------------------------------------")
            print("the item you ordered is ",items[a],"and the total bill is ",price[a])
            print("----------------------------------------------------------------")
        else:
            print("----------------------------------------------------------------")
            print("Come back when  you'll like to order food!")
            print("----------------------------------------------------------------")
        a=input("Would you like to enter another item? : ")
        if a=="no":
            break
def complain():
    a=input("Do you have any complain? :")
    if a=="yes":
        b=input("Kindly write your complain : ")
        name=input("Kindly enter your name or anynomous respectively :")
        print("----------------------------------------------------------------")
        print("Your complain has been forwarded",name,"\n The complain is following: ",b)
        print("----------------------------------------------------------------")

        
 
        
 
        
reservation()
order()
complain()

    

