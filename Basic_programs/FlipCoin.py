'''
    Created on Nov 16, 2021

    @author:srividya
    @Date:  16/11/2021
    @Title: FlipCoin

    '''
import random

if __name__=='__main__':
    number_of_flips = int(input("enter the flips"))
    heads_count = 0
    tails_count = 0
    for i in range(number_of_flips):
        rand =random.randint(1,2)
    if rand ==1:
        tails_count +=1
        print(tails_count,"tails")
    else:
        heads_count +=1
    print(heads_count, "heads")
    
    headpercent = (heads_count * 100)/number_of_flips
    tailpercent = (heads_count * 100)/number_of_flips
    print(headpercent, "heads") 
    print(tailpercent,"tails")

