class Arithematic:
    def __init__(self,a,b):    #a,b = local variable
        print("Inside init(Constructor)");
        self.no1 = a;     #self.a = instance 
        self.no2 = b;

    def Addition(self):
        ans = self.no1 + self.no2;      #ans = local variable
        return ans;

def main():
    print("Enter first number: ");
    x = int(input());
    
    print("Enter second number: ");
    y = int(input());
    
    obj = Arithematic(x,y);
    ret = obj.Addition();
    
    print("Addition is : ",ret);


if __name__ == "__main__":
    main();