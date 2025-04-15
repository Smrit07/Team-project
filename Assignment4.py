try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You can't divide by zero.")
except ValueError:
    print("Error: Please enter a valid number.")

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")

try:
    print("Trying to do something risky...")
    x = 10 / 0
except ZeroDivisionError:
    print("Caught an error!")
finally:
    print("This will run no matter what.")
