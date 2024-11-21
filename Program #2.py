import tkinter as tk
services = {
    "Oil Change": 30.00,
    "Lube Job": 20.00,
    "Radiator Flush": 40.00,
    "Transmission Fluid": 100.00,
    "Inspection": 35.00,
    "Muffler Replacement": 200.00,
    "Tire Rotation": 20.00
}
def calculate_total():
    total = 0
    for service, var in checkbuttons_vars.items():
        if var.get():
            total += services[service]
    total_label.config(text=f"Total Charges: ${total:.2f}")
root = tk.Tk()
root.title("Joe's Automotive - Service Selection")
checkbuttons_vars = {}
for service, price in services.items():
    var = tk.BooleanVar()
    checkbuttons_vars[service] = var
    checkbutton = tk.Checkbutton(root, text=f"{service} - ${price:.2f}", variable=var, command=calculate_total)
    checkbutton.pack(anchor="w")
total_label = tk.Label(root, text="Total Charge = : $0.00", font=("Arial", 14))
total_label.pack(pady=10)
root.mainloop()

# Matthew Beekman
# Program 2
# 11/21/2024