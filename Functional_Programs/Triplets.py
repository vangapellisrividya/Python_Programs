'''
    Created on Nov 17, 2021

    @author:srividya
    @Date:  17/11/2021
    @Title: Quadratic rootts calculattion

    '''
def triplets(arr,n):
    for i in range(0 , n-2):
      for j in range(i+1,n-1):
        for k in range(j + 1, n):
          if arr[i] + arr[j] +arr[k] == 0:
              print("There are Triplets !!")
              print(arr[i], "  ", arr[j] ," ",arr[k] , sep = " ") 
              print("------------------------------------")
              True
          else:
               False
               
              
    if False:
        print("Tripletes not present in array")  
        
if __name__=='__main__':
    arr = []
    n=int(input("Enter number of elements in array :"))
    for i in range(0,n):
        arr+= [0]
    print ("Enter elements in array: ")
    for i in range(n):
        print ("Enter",i+1," element: ")
        arr[i]=int(input())
    print("-----------------------")   
    n = len(arr)
    triplets(arr,n)
    
    
