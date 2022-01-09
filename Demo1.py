
def main():
    size = 0;
    i = 0;
    Data=[];

		
    print("How many elements you want?")
    size = int(input())
	
    print("Enter the elements : ")
    for i in range(size):
        Data.append(int(input()))
	
	print("You entered data is : ",Data)
	

if __name__ =="__main__":
	main()