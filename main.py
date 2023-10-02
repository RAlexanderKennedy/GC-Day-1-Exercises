##Prompt the user to enter a string. After the user enters a string, output the same string back to the console.

userText: str = input("Enter some text: ")
print(userText)

##Prompt the user to enter a number. After the user enters a number, add 1 to the number and output it back to the console.

userNumber: int = int(input("Enter a number: "))
print(userNumber + 1)

##Prompt the user to enter a number. After the user enters a number, add .5 to the number and output it back to the console.
userNumber2: float = float(input("Enter a number: "))
print(userNumber2 + 0.5)

##Prompt the user to enter two numbers. After the user enters the numbers, add them together and output the sum back to the console.
firstNumber: float = float(input("Enter a number: "))
secondNumber: float = float(input("Enter another number: "))
print("The sum is " + str((firstNumber + secondNumber)))

##Prompt the user to enter two numbers. After the user enters the numbers, multiply them and output the product back to the console.
firstNumber: float = float(input("Enter a number: "))
secondNumber: float = float(input("Enter another number: "))
print("The product is " + str((firstNumber * secondNumber)))

##Prompt the user to enter two numbers. After the user enters the numbers, divide them and output the result back to the console

firstNumber: int = int(input("Enter a number: "))
secondNumber: int = int(input("Enter another number: "))
print("The result is " + str((firstNumber / secondNumber)))