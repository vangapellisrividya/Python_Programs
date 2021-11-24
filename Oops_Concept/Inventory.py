'''
    Created on Nov 21, 2021

    @author:srividya
    @Date:  21/11/2021
    @Title: Addressbook

    '''


import random
from datetime import datetime
import json


all_products = [
    [1,'smart phone',20,'200$'],
    [2,'chargers',100,'10$']
    ]

def banner():
    print("***********************************************")
    print("\t1.Show All Products")
    print("\t2.Buy roducts")
    print("\t3.Add Products")
    print("\t4.Write and Read JSON")
    print("\t5.Exit")
    print("***********************************************")

def display_all():
    print("***********************************************")
    print("SNO\tProduct\t\tIn Stock\tPrice")
    print("***********************************************")
    for item in all_products:
        print("{0}\t{1}\t{2}\t\t{3}".format(item[0],item[1],item[2],item[3]))

def order(product,name):
    print("***********************************************")
    print("\t\tMobiles shop")
    print("***********************************************")
    print("Order Summary\tDate:{}".format(str(datetime.now())))
    print("Customer name: {}".format(name))
    print("Product name: {}".format(item[1]))
    print("Price: {}".format(item[-1]))
    print("\t\tTotal Bill Amount: {}".format(item[-1]))

def generate_bill(product,name):
    print("***********************************************")
    print("\t\tMobiles shop")
    print("***********************************************")
    print("Bill:{} ".format(int(random.random()*100000)))
    print("Customer name: {}".format(name))
    print("Product name: {}".format(item[1]))
    print("Price: {}".format(item[-1]))
    print("\t\tTotal Bill Amount: {}".format(item[-1]))

def json_obj(self):
    js = json.dumps(all_products)
    ''' json.dumps() function converts a Python object into a json string '''
    js  
    fd = open("all_products.txt", 'w')

    fd.write(js)  # writing string into file
    fd.close() 
    fd = open("all_products.txt", 'r')  # Open file in read mode
    txt = fd.read()  # reading data from file
    data = json.loads(txt)
    fd.close()
    print(data)

if __name__=='__main__':
    
    choice =1
    while(choice):
        banner()
        choice = int(input("enter the choice:   "))
        # choice =int(input())
        if choice ==1:
            display_all()
        elif choice == 2:
            display_all()
            prod_id = int(input("Enter the Product Id: "))
            for item in all_products:
                if item[0] == prod_id:
                    name = input("Customer Name: ")
                    order(item, name)
                    cnf = input("confirm order(Y/N)")
                    if cnf =='Y':
                        item[2] -=1
                        generate_bill(item,name)
                        print("Thanks for shopping with us")
                        display_all()
                        # sys.exit(0)
                    else:
                        print("GoodBye!!!")
                
                else:
                    print("explore shopping")
        elif choice == 3:
            username = input("enteruserid:")
            password = input("password: ")
            if username == "Admin" and password == "Password":
                prod =[]
                prod.append(len(all_products)+1)
                prod.append(input("enter product name: "))
                prod.append(int(input("Available: ")))
                prod.append(int(input("Price: ")))
                all_products.append(prod)
            else:
                print("incorrect username and password")
        elif choice == 4:
            json_obj(all_products)
        elif choice ==5:
            print("welcome to shopping...")
        else:
            print("GoodBye!!")
            break

