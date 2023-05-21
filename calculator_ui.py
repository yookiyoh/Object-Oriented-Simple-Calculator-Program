# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 7
# Remodified Object-Oriented Simple Calculator

# Pseudocode

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
        self.label1 = tk.Label(self.window, text = "First Number: ")
        self.label1.grid(row = 0, column = 0)

# Execute Calculator UI class methods