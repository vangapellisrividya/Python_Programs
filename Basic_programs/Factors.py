'''
    Created on Nov 16, 2021

    @author:srividya
    @Date:  16/11/2021
    @Title: Factors

    '''
import math


if __name__=='__main__':
    number = int(input("Enter a Number"))
    while number % 2 == 0:
        print(number)
    number = number//2
    i=3
    for i in range(int(math.sqrt(number))+1,3):
        while number%i ==0:
            print(i)
    number = number//i
    if number > 2: 
        print(number)
