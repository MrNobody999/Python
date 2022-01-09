print("Start of program");
def fun():
    print("Inside Demo");

def main():
    print("Inside main");
    fun();

if __name__=="__main__":
    print(__name__);
    main()
    print("End of Application");