# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 7
# Remodified Object-Oriented Simple Calculator

# define a Calculator Functions class with its properties and methods
class CalculatorFunctions:
    # Execute Calculator Functions class methods
    @staticmethod
    def addition(num1, num2):
        return num1 + num2
    
    @staticmethod
    def subtraction(num1, num2):
        return num1 - num2
    
    @staticmethod
    def multiplication(num1, num2):
        return num1 * num2
    
    @staticmethod
    def division(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            raise ZeroDivisionError("Error: Cannot divide by zero")