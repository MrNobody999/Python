def Display(value):
    for i in range (1,value):
        print(i, end =" ")

def main():
    no = int(input("Enter number"))
    Display(no)

if __name__=="__main__":
    main()