def Display(value1,value2):
    for i in range(0,value1):
        
        for j in range(0, i + 1):
            print("*")
def main():
    no1 = int(input("Enter number of rows"))
    no2 = int(input("Enter number of columns"))
    
    
    Display(no1,no2)
    
if  __name__=="__main__":
    main()