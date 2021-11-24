'''
    Created on Nov 21, 2021

    @author:srividya
    @Date:  21/11/2021
    @Title: Addressbook

    '''


import re
import json
class Book:
    def __init__(self,Addressbook):
        self.Addressbook=Addressbook

    def add(self,Addressbook):
        """
            Description:
                Adding contacts to the address book and validating 
                the entries using regex  pattern

            using given formulea
            Prameters:
                self,Addressbook
            Return:
                None
        """
        try:
            #regex patter for accepting positive integer and maximum one digit 
            
            num=input("enter the count of contacts do you want to add?")
            pattern="^[1-9]{1}$"
            result=re.match(pattern,num)

            if result:
                num=int(num)
                for i in range(num):
                    #regex patter for accepting string and minimum three characters
                    name = input("enter the name: ")
                    pattern="(.*[A-Z]|[a-z]){3,}"
                    result=re.match(pattern,name)
                    address = input("enter the address: ")           
                    pattern1="^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:\\|,.<>\/?]*$"
                    result1=re.match(pattern1,address)
                        
                    phone = input("enter the phoneno: ")
                    pattern2="^[0-9]*$"
                    result2=re.match(pattern2,phone)
                    if result and result1 and result2:
                        Addressbook[name]=address,phone
                    else:
                        print("Give the proper data..")
            else:
                print("Not valid...")                           
        except Exception as e:
            print("Error...!",e)

    def display(self,Addressbook):
        """
            Description:
                This function displays he data stored in
                Addressbook
            Prameters:
                self,Addressbook
            Return:
                None
        """
        print(Addressbook)

    def delete(self,Addressbook):
        """
            Description:
                Delete the contacts in the address book based on the user
                requirement
            using given formulea
            Prameters:
                self,Addressbook
            Return:
                None
        """
        print("enter the student nameto delete")
        try:
            name1 = input("enter the name")
            #regex patter for accepting string and minimum three characters
            pattern="(.*[A-Z]|[a-z]){3,}"
            result=re.match(pattern,name1)
            if result:
                r=Addressbook.pop(name1,"not...")
                if r =="not":
                    print(r)
                else:
                    print("deleted")
                    print(Addressbook)
            else:
                print(" not exsist..")
        except Exception as e:
            print("Error1...!",e)
 
    def search(self,Addressbook):
        """
            Description:
                search the contacts in the Addressbook by entering 
                the key if key exists values will be displayed
            Prameters:
                self,Addressbook
            Return:
                None
        """
        print("enter the contact name to search")
        try:
            name1 = input("enter the name: ")
            #regex patter for accepting string and minimum three characters
            pattern="(.*[A-Z]|[a-z]){3,}"
            result=re.match(pattern,name1)
            if result:
                key = name1
                if key in Addressbook:
                    print("yes exists")
                    print(key)
                    print(Addressbook)
                else:
                    print("Not existed")
            else:
                print("Enter the valid one....")
        except Exception as e:
            print("Error2...!",e)

    def update(self,Addressbook):
        """
            Description:
                Update the contacts in the Addressbook by entering 
                the key if key exists values will be displayed
            Prameters:
                self,Addressbook
            Return:
                None
        """
        print("enter the contact name to search")
        try:
            name1 = input("enter the name: ")
            #regex patter for accepting string and minimum three characters
            pattern="(.*[A-Z]|[a-z]){3,}"
            result=re.match(pattern,name1)
            if result:
                key = name1
                dict={}
                newnumber=input("enter the newnumber: ")
                newaddress=input("enter the newaddress: ")
                dict[name1]=newnumber,newaddress
                if key in Addressbook:
                    Addressbook.update(dict)
                    print(Addressbook)
                else:
                    print("not updated try again...")
            else:
                print("not exists")
        except Exception as e:
            print("Error...!",e)

    def convert_to_jsonfile(self,Addressbook):
        """
            Description:
                In this function using json object we can write and read and write
                functions, and dictionary data will be converted into json format
                and also json to dictionary
            Prameters:
                self,Addressbook
            Return:
                None
        """
        json_object = json.dumps(Addressbook) 
        file = open('Addressbook.json','a')

        file.write(json_object)
        file.close()
        

    def from_jsonto_dictionary(self,Addressbook):
        """
            Description:
                In this function using json object we can write and read and write
                functions, and dictionary data will be converted into json format
                and also json to dictionary
            Prameters:
                self,Addressbook
            Return:
                None
        """
        f= open('Addressbook.json','r')
        json_object= f.read()
        f.close()
        print(json_object)
        Addressbook = json.loads(json_object)
        print(Addressbook)       
            

if __name__=='__main__':
    Addressbook={}
    object = Book(Addressbook)
    choice = 1
    while choice !=0:
        print("**********Welcome to the AddressBook******")
        print("1.Accept Details in AddressBook")
        print("2.Print Details of AddressBook") 
        print("3.Delete Details of  AddressBook")
        print("4.Search Details in AddressBook") 
        print("5.Update Details in AddressBook ")
        print("0.Exit")
        try:
            
            choice = int(input("enter the choice: "))
            if choice==1: 
                object.add(Addressbook)
            elif choice == 2: 
                object.display(Addressbook)
            elif choice ==  3:
                object.delete(Addressbook)
            elif choice ==  4: 
                object.search(Addressbook)
            elif choice ==  5: 
                object.update(Addressbook)
            else:
                print("Thank You For Visting....")
        except:
                print("Please enter number")
                        

   
    
    

    
