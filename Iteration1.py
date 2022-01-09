#We have to display 5 times "Hello World" on screen

def Iteration():
    no = 0;
    
    while(no < 5):
        print("Hello World");
        no = no + 1;

def Sequence():
	print("Hello World");
	print("Hello World");
	print("Hello World");
	print("Hello World");
	print("Hello World");

def main():
	#Sequence();
    Iteration();

if __name__=="__main__":
	main()