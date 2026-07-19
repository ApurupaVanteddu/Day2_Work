def add(a,b):
    return a + b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def main():
    print("==simple Calculator==")
    print("1.Addition")
    print("2.Substarction")
    print("3.Multiplication")
    print("4.Division")

    choice=int(input("Enter your choice(1-4): "))

    num1=float(input("Enter first number:"))
    num2=float(input("Enter Second number:"))

    if choice == 1:
        print(f" Addition result : {add(num1,num2)}")
    elif choice == 2:
        print(f" Subraction result : {subtract(num1,num2)}")
    elif choice  == 3:
        print(f" Multiplication result : {multiply(num1,num2)}")
    elif choice == 4:
        if num2 !=0:
            print(f"Division result : {divide(num1,num2)}")
        else:
            print("Invalid choice. please selct a valid option.")

if __name__ == "__main__":
    main()

'''


'''