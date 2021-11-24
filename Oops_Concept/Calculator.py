class Calculator:
    def sum(self,num1,num2):
        add = num1+num2
        return add
    def sub(self,num1,num2):
        sub = num1-num2
        return sub
    def mul(self,num1,num2):
        mul = num1*num2
        return mul
        
if __name__=='__main__':
    num1 = int(input("enter the num1: "))
    num2 = int(input("enter the num2: "))
    obj = Calculator()
    obj = Calculator()
    obj = Calculator()
    add = obj.sum(num1,num2)
    sub = obj.sub(num1,num2)
    mul = obj.mul(num1,num2)
    print("Addition is : ",add, "\nSubstraction is: ",sub,"\nMultiplication is: " ,mul,sep=" ")        