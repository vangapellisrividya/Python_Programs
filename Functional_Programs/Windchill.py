'''
    Created on Nov 17, 2021

    @author:srividya
    @Date:  17/11/2021
    @Title: WindChill

    '''

import math
def windChill(v , t):
    """
       Description:
            This function used to calculate the
            weather service using wind spped and
            temperature.
       Prameters:
            x and y parameters are used
        Return:
            Iwindchill
        """
    windchill = (35.74+0.6215+(0.4275*t-35.75)*v**0.16)
    return windchill

if __name__=='__main__':
    v=int(input("enter the speed: "))
    t=int(input("enter the temperature: "))
    if v<3 and v>120 or t>50:
        print("Weather service giving temperature: ",windChill(v,t))
    else:
        print("Enter the valid values")