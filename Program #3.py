import tkinter as tk
from tkinter import messagebox
def calculate_charge():
    try:
        selected_category = rate_var.get()
        minutes = float(minutes_entry.get())
        if selected_category == "Daytime":
            rate = 0.02
        elif selected_category == "Evening":
            rate = 0.12
        elif selected_category == "Off-Peak":
            rate = 0.05
        else:
            messagebox.showerror("Error", "Please select a rate category.")
            return
        charge = rate * minutes
        messagebox.showinfo("Charge Information", f"The charge for the call is: ${charge:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of minutes.")
root = tk.Tk()
root.title("Telephone Call Charge Calculator")
rate_var = tk.StringVar()
daytime_radio = tk.Radiobutton(root, text="Daytime (6:00 A.M. - 5:59 P.M.)", variable=rate_var, value="Daytime")
evening_radio = tk.Radiobutton(root, text="Evening (6:00 P.M. - 11:59 P.M.)", variable=rate_var, value="Evening")
off_peak_radio = tk.Radiobutton(root, text="Off-Peak (Midnight - 5:59 A.M.)", variable=rate_var, value="Off-Peak")
daytime_radio.grid(row=0, column=0, sticky="w", padx=10, pady=5)
evening_radio.grid(row=1, column=0, sticky="w", padx=10, pady=5)
off_peak_radio.grid(row=2, column=0, sticky="w", padx=10, pady=5)
minutes_label = tk.Label(root, text="Enter the number of minutes:")
minutes_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
minutes_entry = tk.Entry(root)
minutes_entry.grid(row=3, column=1, padx=10, pady=5)
calculate_button = tk.Button(root, text="Calculate Charge", command=calculate_charge)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)
root.mainloop()

# Matthew Beekman
# Program 3
# 11/21/2024