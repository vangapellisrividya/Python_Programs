'''	
    @Author: Srividya
    @Date:  2021-11-18 
    @Title: Generate coupon numbers
    '''

import random
import re

def generateCouponCode(count,length):
     """"
    Description: generating different type of combinations of string
    Parameter: count,length
    Return: none
    """
     count = int(count)
     length = int(length)
     codepattern = "ABCDEFGHIJKLMNOPQRST1234567890"
     print("Coupon Numbers :")
     for i in range(count):
            code = ""
            for x in range(length):
                code += random.choice(codepattern)
            print(code)

        
if __name__ == '__main__':
    # Taking input from the user
    codeCount = input("Enter number of coupons to be generated :")
    codelength = input("Enter length of the coupon number:")
    #regex for integer number and maximum two digit 
    pattern= "^[1-9]{1,2}$"
    result1 = re.match(pattern,codeCount)
    result2 = re.match(pattern,codelength)
    if result1 and result2:  
        generateCouponCode(codeCount,codelength)



	
	
	
	
	
    