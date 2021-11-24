'''
Created on Nov 16, 2021

@author:srividya 
@Date:  17/11/2021
@Title: Taking the input from the user
'''

import re

if __name__=='__main__':
    username = input("enter the name: ")
    Pattern = "(.*[A-Z]|[a-z]){3,}$"
    result=re.match(Pattern,username)

    if result:
        print("Hello ",username,"how are you?") 
    else:
        print(" Username is not valid")

