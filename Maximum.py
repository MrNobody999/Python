
def Maximun(value1, value2):
	if(value1 > value2):
		return value1;
	else:
		return value2;
	
def main():
	print("Enter first number");
	no1 = int(input())
	
	print("Enter second number");
	no2 = int(input());
	
	ret = Maximun(no1, no2);

	print("Maximun number is : ", ret);

if __name__=="__main__":
	main()