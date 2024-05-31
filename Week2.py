#Simple Calculator using Python to perform the arithmetic operations like Addition, Subtraction, Multiplication, Division.

def add(a, b):
    c=a+b
    print(f"\nAddition of two numbers {a} + {b} is: ", c)

def subtract(a, b):
    c=a-b
    print(f"\nSubtraction of two numbers {a} - {b} is: ", c)

def multi(a, b):
    c=a*b
    print(f"\nMultiplication of two numbers {a} * {b} is: ", c)

def div(a, b):
    c=a/b
    print(f"\nDivision of two numbers {a} / {b} is: ", c)

def floorDiv(a, b):
    c=a//b
    print(f"\nInteger Division of two numbers {a} // {b} is: ", c)

def power(a, b):
    c=a**b
    print(f"\n{a} raised to {b} is: ", c)

if __name__=="__main__":
    num1=int(input("Enter the first number: \n"))
    num2=int(input("Enter the second number: \n"))

    print("\n1: Addition\n"
          "2: Subtraction\n"
          "3: Multiplication\n"
          "4: Division\n"
          "5: Floor Division\n"
          "6: Power")
    
    print("\nPlease select the option to perform the operation: ")
    choice=int(input())

    if choice==1:
        addition=add(num1,num2)

    elif choice==2:
        subtraction=subtract(num1,num2)

    elif choice==3:
        multiplication=multi(num1,num2)
    
    elif choice==4:
        division=div(num1,num2)

    elif choice==5:
        floorDivision=floorDiv(num1, num2)
    
    elif choice==6:
        powers=power(num1,num2)
    
    else:
        print("Try Again!! Please enter the correct choice: ")