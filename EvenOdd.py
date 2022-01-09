def EvenOdd(value):
    
    if (value%2 == 0):
         return True
         
    else:
        return False
       
def main():
    no = int(input("Enter number to check"))
    
    ret = EvenOdd(no)
    
    if(ret == True):
        print("Number is Even")
        
    else:
        print("Nummber is odd")
       

if  __name__=="__main__":
    main()