# Ask user to input 3 numbers. Find and print the biggest number using if-else statement.

# pseudocode

# Import the required libraries
import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Biggest Number Finder")

# Create a notebook (tabs)
notebook = ttk.Notebook(window, style='MyStyle.TNotebook')

# Create the Tab 1 - Input
tab_input = ttk.Frame(notebook)
notebook.add(tab_input, text='Input')

# Create a notebook (tabs) style
style = ttk.Style()
style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [0, 5, 0, 0], "background": "#FFC0CB"}},
    "TNotebook.Tab": {
        "configure": {"padding": [10, 5], "background": "#FF69B4", "font": ('Helvetica', 10, 'bold')},
        "map": {"background": [("selected", "#FFD700")]}}})
style.theme_use("MyStyle")

# Pack the notebook to make it visible
notebook.pack(expand=1, fill='both')

# Run the main loop
window.mainloop()



# Tab to enter first, second, and third number
# Define the function to find the biggest number
# Create the Tab 2 - Result

