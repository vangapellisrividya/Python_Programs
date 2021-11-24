'''
    Created on Nov 16, 2021

    @author:srividya
    @Date:  16/11/2021
    @Title: HarmonicNumber

    '''

   
if __name__=='__main__':
    num = int(input(" Enter a number: "))
     # H1 = 1
    harmonic = 1.00
    # loop to apply the forumula
    for i in range(2, num + 1) :
        harmonic += 1 / i
    print(harmonic) 
    print(round((num),5))
