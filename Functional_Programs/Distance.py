'''
    Created on Nov 17, 2021

    @author:srividya
    @Date:  17/11/2021
    @Title: Finding Euclidian Distance

    '''


import math
def distance(x, y):
    """
       Description:
            This function will give the distance from
            the points to the origin(0,0) 
       Prameters:
            x and y parameters are used
        Return:
            It will return the distance
        """
    dist = math.pow((x*x +y*y),y)
    return dist

if __name__=='__main__':
    x=int(input("enter the value: "))
    y=int(input("enter the value: "))
    print(" Euclidian distance is: ",distance(x,y))
    