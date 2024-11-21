import tkinter as tk
from tkinter import messagebox
def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        if gallons == 0:
            messagebox.showerror("Input Error", "Gallons of gas cannot be zero.")
            return
        mpg = miles / gallons
        result_label.config(text=f"MPG: {mpg:.2f} miles per gallon")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
root = tk.Tk()
root.title("Car MPG Calculator")
gallons_label = tk.Label(root, text="Enter the number of gallons of gas the car holds:")
gallons_label.pack(pady=5)
gallons_entry = tk.Entry(root)
gallons_entry.pack(pady=5)
miles_label = tk.Label(root, text="Enter the number of miles the car can be driven on a full tank:")
miles_label.pack(pady=5)
miles_entry = tk.Entry(root)
miles_entry.pack(pady=5)
calculate_button = tk.Button(root, text="Calculate MPG", command=calculate_mpg)
calculate_button.pack(pady=10)
result_label = tk.Label(root, text="MPG: ")
result_label.pack(pady=10)
root.mainloop()

# Matthew Beekman
# Program 1
# 11/21/2024