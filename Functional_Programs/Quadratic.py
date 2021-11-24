'''
    Created on Nov 17, 2021

    @author:srividya
    @Date:  17/11/2021
    @Title: Quadratic rootts calculattion

    '''

import math

def getroot(a,b,c):
    """
       Description:
            Finding the roots of the the equation 
            using given formulea
       Prameters:
            a,b and c parameters are used
        Return:
            none
        """
    
    delta=b*b-4*a*c
    #condition for real and different roots
    if delta > 0 :
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("root1 = ", root1,"and root2 =", root2)
    #condition for real and equal roots
    elif delta == 0 :
        root1 = root2 = -b/(2 * a)
        print("root1 = root2 = ",root1)

    # if roots are not real
    else :
        realNumber = -b / (2 * a)
        imagNumber= math.sqrt(-delta) / (2 * a)
        print("root1 =   ",realNumber,",",imagNumber,"i")
        print("root2 =   ",realNumber,",", imagNumber,"i")
        
if __name__=='__main__':
    a = int(input("enter the value"))
    b = int(input("enter the value"))
    c = int(input("enter the value"))
    getroot(a,b,c)