def Arithmetic(value1,value2):
    add = value1 + value2;
    sub = value1 - value2;
    mul = value1 * value2;
    div = value1 / value2;
    return add,sub,mul,div;

def main():
    print("Enter first number : ");
    no1 = int(input());
    
    print("Enter second number : ");
    no2 = int(input());
    
    ret1,ret2,ret3,ret4 = Arithmetic(no1,no2);
    
    print("Addition is : ",ret1);
    print("Substraction is : ",ret2);
    print("Multiplication is : ",ret3);
    print("Division is : ",ret4);

if __name__=="__main__":
    main();