# Addition Method

def add(x, y):
    return x + y


# Subtraction Method

def subtract(x, y):
    return x - y


# Multiplication Method
def multiply (x,y):
    return x * y
  
# Division Method
def divide(x,y):
    return x / y

# Main Method
print("Select operation:")
print("Press (+) for Addition")
print("Press (-) for Subtraction")
print("Press (x) for Multiplication")
print("Press (/) for Division")

choice = input ("Enter your operation")

num1 = float(input("Enter first number: "))
num2 = float (input("Enter second number: "))

if choice == '+':
    print("Result: ", add(num1, num2))

elif choice == '-':
    print("Result: ", subtract(num1, num2))
elif choice == 'x':
    print("Result: ", multiply(num1, num2))
elif choice == '/':
    print("Result: ", divide(num1, num2))
else:
    print("Invalid input")
