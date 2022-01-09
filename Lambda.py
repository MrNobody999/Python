def Add(a,b):
	return a + b;
    
AddX = lambda a,b : a+b;

def main():
    ret = AddX(10,20);
    print("Addition is : ", ret);
        
    print(lambda a,b : a + b);
    
if __name__ == "__main__":
	main();