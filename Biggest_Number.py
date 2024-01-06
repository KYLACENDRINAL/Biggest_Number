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

# Tab to enter first, second, and third number
tk.Label(tab_input, text="Enter the first number:", font=('Helvetica', 12)).grid(row=0, column=0, pady=10)
entry1 = tk.Entry(tab_input, width=10, font=('Helvetica', 12))
entry1.grid(row=0, column=1)

tk.Label(tab_input, text="Enter the second number:", font=('Helvetica', 12)).grid(row=1, column=0, pady=10)
entry2 = tk.Entry(tab_input, width=10, font=('Helvetica', 12))
entry2.grid(row=1, column=1)

tk.Label(tab_input, text="Enter the third number:", font=('Helvetica', 12)).grid(row=2, column=0, pady=10)
entry3 = tk.Entry(tab_input, width=10, font=('Helvetica', 12))
entry3.grid(row=2, column=1)


# Define the function to find the biggest number
def find_biggest_number():
    # Get user input for three numbers
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    num3 = float(entry3.get())
    # Find the biggest number using if statements
    if num1 >= num2 and num1 >= num3:
        biggest_num = num1
    elif num2 >= num1 and num2 >= num3:
        biggest_num = num2
    else:
        biggest_num = num3

        # Switch to the result tab
    notebook.select(1)

    result_label.config(text=f"The biggest number is: {biggest_num}", fg="#FF69B4")  # Pink color


# Create the calculate button
calculate_button = tk.Button(tab_input, text="Find Biggest Number", command=find_biggest_number, bg="#32CD32", fg="white", font=('Helvetica', 12, 'bold'))
calculate_button.grid(row=3, column=0, columnspan=2, pady=15)

# Create the Tab 2 - Result
tab_result = ttk.Frame(notebook)
notebook.add(tab_result, text='Result')

result_label = tk.Label(tab_result, text="", fg="#FF69B4", font=('Helvetica', 18, 'bold'))
result_label.pack(pady=20)



# Pack the notebook to make it visible
notebook.pack(expand=1, fill='both')

# Run the main loop
window.mainloop()



