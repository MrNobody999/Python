class Demo:
    A = 10;    #Class variable
    
    def __init__(self):
        print("Inside constructor");
        self.B = 20;       #Instance variable
    
    def fun_instance(self):       #Instance method
        print("Inside instance method");
        print(self.B);
        print(self.A);
        print(Demo.A);     #this is the correct way to access class variable
        
    @classmethod
    def fun_class(cls):    #Class method
        print("Inside class method");
        print(cls.A);
        print(Demo.A);
        #print(cls.B);
        
    @staticmethod
    def fun_static():      #Static method
        print("Inside static method");
        print(Demo.A);
        #print(Demo.B);
    
    def __del__(self):
        print("Inside Destructor");


def main():
    #obj = Demo();     #Object creation
    #obj.fun_instance();
    #Demo.fun_class();
    #obj = None;
    Demo.fun_static();

if __name__ == "__main__":
    main();
    