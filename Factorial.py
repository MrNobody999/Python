def Factorial(value):
    Fact = 1
    for i in range(1,value+1):
        
        Fact = Fact * i
    
    return Fact
    

def main():
    no = int(input("Enter the Number"))
    
    
    ret = Factorial(no)
    print("Factorial is: ", ret)
   

if __name__=="__main__":
    main()