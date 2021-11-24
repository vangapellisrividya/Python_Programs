'''
    Created on Nov 17, 2021

    @author:srividya
    @Date:  17/11/2021
    @Title: Displaying 2D array

    '''

import numpy as np

def array(arr,m,n):
    """
       Description:
            this function prints the array by taking
            the rows and cloumns from the user input 
       Prameters:
            arr,m,n
        Return:
            It returns array
        """
    
    for i in range(0,m):
        arr+=[0]
    # initialize the arr
    for i in range (0,m):
        arr[i] =[0]*n

    for i in range (0,m):
        for j in range (0,n):
         print ('entry in row: ',i+1,' column: ',j+1)
         arr[i][j] =int(input())
    
def printing(arr,m,n):

     for i in range (0,m):
        print()
        for j in range (0,n):
            arr[i][j] 
            print(arr[i][j],end=" ")

if __name__=='__main__':
    
    arr = []
    m = int(input("Enter the rows: "))
    n = int(input("Enter the columns: "))
    array(arr,m,n)
    printing(arr,m,n)


