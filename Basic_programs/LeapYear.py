'''
    Created on Nov 16, 2021

    @author:srividya
    @Date:  16/11/2021
    @Title: LeapYear

    '''
import re


if __name__=='__main__':
    year=input("enter the year")
    pattern="^[1-9]{1}[0-9]{4}$"
    result=re.match(pattern,year)
    if result:
        print("valid year")
    if(year%400 == 0) or year %4 ==0:
        print("leap year")
    else:
        print("not valid year")
        
    