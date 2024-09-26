# T0 add two numbers
def add(num1,num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Operations Menu \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Exit")
for i in range(1,4):
    choice= int(input("Please select operations from above :"))
    if choice>4:
        print("invalid")
        break

    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    if choice == 1:
        print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

    elif choice == 2:
        print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

    elif choice == 3:
        print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

    elif choice== 4:
        print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
        

    

