def revDisplay(value):
    for i in range (value, 0,-1):
        print(i, end =" ")

def main():
    no = int(input("Enter number"))
    revDisplay(no)

if __name__=="__main__":
    main()