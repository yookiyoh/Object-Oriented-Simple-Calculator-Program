# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 7
# Remodified Object-Oriented Simple Calculator



# Import Calculator Functions
from calculator_functions import CalculatorFunctions

# Import necessary libraries or modules 
import tkinter as tk   # import tkinter for GUI
from tkinter import *
from tkinter import messagebox  # import messagebox for the error message

# Define a Calculator UI class with its properties and methods
class CalculatorUI:
    # Enable Calculator UI class constructor/s
    # Constructor that initializes the Calculator UI class
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple Calculator")   # Set title for the window
        self.window.config(bg = "#007FFF")

        # Create GUI elements and configure their properties
        # Create label for first number
        self.label1 = tk.Label(self.window, text = "First Number: ", font = ("Arial", 15, "bold"), bg = "#536878", fg = "#007FFF")
        self.label1.grid(row = 0, column = 0, padx = 10, pady = 10)

        # Create textbox for first number input
        self.num1_entry = tk.Entry(self.window, font = ("Gotham Black", 14), fg = "#F9E076", justify = CENTER)
        self.num1_entry.grid(row = 0, column = 1)

        # Create label for second number
        self.label2 = tk.Label(self.window, text = "Second Number: ", font = ("Arial", 15, "bold"), bg = "#536878", fg = "#007FFF")
        self.label2.grid(row = 1, column = 0, padx = 10)

        # Create textbox for second number input
        self.num2_entry = tk.Entry(self.window, font = ("Gotham Black", 14), fg = "#F9E076", justify = CENTER)
        self.num2_entry.grid(row = 1, column = 1)

        # Create label for Result
        self.labelr = tk.Label(self.window, text = "Result: ", font = ("Stylus", 15, "bold"), bg = "#536878", fg = "#007FFF")
        self.labelr.grid(row = 2, column = 0)

        # Display result output
        self.labeld = tk.Label(self.window, text = "", font = ("Tahoma", 15, "bold"), bg = "#536878", fg = "#007FFF", justify = CENTER)
        self.labeld.grid(row = 2, column = 1)

        # Create button for addition operation
        self.button_add = tk.Button(self.window, text = "Add", width = 11, font = ("Futura", 14, "bold"), bg = "#BDA55D", command = self.addition_num)
        self.button_add.grid(row = 3, column = 0, padx = 5, pady = 5)

        # Create button for subtraction operation
        self.button_sub = tk.Button(self.window, text = "Subtract", width = 11, font = ("Futura", 14, "bold"), bg = "#BDA55D", command = self.subtraction_num)
        self.button_sub.grid(row = 3, column = 1, padx = 5, pady = 5)

        # Create button for multiplication operation
        self.button_mul = tk.Button(self.window, text = "Multiply", width = 11, font = ("Futura", 14, "bold"), bg = "#BDA55D", command = self.multiplication_num)
        self.button_mul.grid(row = 4, column = 0, padx = 5, pady = 5)

        # Create button for division operation
        self.button_div = tk.Button(self.window, text = "Divide", width = 11, font = ("Futura", 14, "bold"), bg = "#BDA55D", command = self.division_num)
        self.button_div.grid(row = 4, column = 1, padx = 5, pady = 5)

        # Create button for clear content
        self.button_clear = tk.Button(self.window, text = "Clear", width = 11, font = ("Helvetica", 12, "bold"), bg = "#FBEC5D", command = self.clear_input)
        self.button_clear.grid(row = 5, column = 0, padx = 5, pady = 15)

        # Create button for reiteration
        self.button_reiterate = tk.Button(self.window, text = "Try Again", width = 11, font = ("Helvetica", 12, "bold"), bg = "#ED7117", command = self.reiterate_program)
        self.button_reiterate.grid(row = 5, column = 1, padx = 5, pady = 15)

        # Create button for motivation
        self.button_motivation = tk.Button(self.window, text = "?", width = 11, font = ("Helvetica", 12, "bold"), bg = "#5DBB63", command = self.motivate_message)
        self.button_motivation.grid(row = 6, column = 1, padx = 5, pady = 15)

        # Create button for program exit 
        self.button_exit = tk.Button(self.window, text = "Exit", width = 11, font = ("Helvetica", 12, "bold"), bg = "#E3242B", command = self.exit_program)
        self.button_exit.grid(row = 6, column = 2, padx = 5, pady = 15)
        
    # Execute Calculator UI class methods
    def addition_num(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = CalculatorFunctions.addition(num1, num2)
            self.labeld.config(text = result)
        except ValueError:
            messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')
        
    def subtraction_num(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = CalculatorFunctions.subtraction(num1, num2)
            self.labeld.config(text = result)
        except ValueError:
            messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')
        
    def multiplication_num(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = CalculatorFunctions.multiplication(num1, num2)
            self.labeld.config(text = result)
        except ValueError:
            messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')
        
    def division_num(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = CalculatorFunctions.division(num1, num2)
            self.labeld.config(text = result)
        except ZeroDivisionError:    # exception for zero division error
            messagebox.showerror('Error detected', 'Error: Cannot divide by zero')
        except ValueError:
            messagebox.showerror('Error detected', 'Error: Invalid input. Please enter a valid input')

    # Define function for clear input
    def clear_input(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)

    # Define function for reiteration
    def reiterate_program(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        messagebox.showinfo('Retry', 'Please input new values for arithmetic calculations')

    # Define function for motivation
    def motivate_message(self):
        messagebox.showinfo('?', 'You are worthy. I hope you know that :3\nKeep moving forward!')

    # Define function for program exit
    def exit_program(self):
        self.window.destroy()
        messagebox.showinfo('Message', 'Thank you for using this program!')
    
    def run(self):
        self.window.mainloop()