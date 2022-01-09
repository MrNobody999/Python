class Demo:
    A = 10;    #Class variable
    
    def __init__(self):
        print("Inside constructor");
        self.B = 20;       #Instance variable
    
    def fun_instance(self):       #Instance method
        print("Inside instance method");
        
    @classmethod
    def fun_class(cls):    #Class method
        print("Inside class method");
        
    @staticmethod
    def fun_static():      #Static method
        print("Inside statis method");
    
    def __del__(self):
        print("Inside Destructor");


def main():
    
    Demo.fun_class();
    Demo.fun_static();
    
    
    obj = Demo();     #Object creation
    obj.fun_instance();

if __name__ == "__main__":
    main();
    