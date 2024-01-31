#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Initialize the main application window
root = tk.Tk()
root.title("Portfolio Manager")

# Dictionary to store investment names and their amounts
investments = {}

# Function to add an investment to the portfolio
def add_investment():
    investment_name = investment_name_entry.get()
    amount = float(amount_entry.get())
    investments[investment_name] = amount
    update_investment_list()
    calculate_proportions()

# Function to update the list of investments displayed to the user
def update_investment_list():
    investments_list.delete(0, tk.END)
    for name, amount in investments.items():
        investments_list.insert(tk.END, f"{name}: ${amount:.2f}")

# Function to calculate and display the proportions of each investment
def calculate_proportions():
    total_investment = sum(investments.values())
    proportions = {name: (amount / total_investment) * 100 for name, amount in investments.items()}
    display_proportions(proportions)

# Function to display the proportions in a pie chart
def display_proportions(proportions):
    figure = Figure(figsize=(6, 4), dpi=100)
    subplot = figure.add_subplot(111)
    subplot.pie(proportions.values(), labels=proportions.keys(), autopct='%1.1f%%')
    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, columnspan=4)

# Function to calculate and display real return after accounting for inflation
def calculate_real_return():
    total_investment = sum(investments.values())
    inflation_rate = float(inflation_rate_entry.get())
    return_rate = float(return_rate_entry.get())
    real_return = (total_investment * (return_rate / 100)) - (total_investment * (inflation_rate / 100))
    real_return_label.config(text=f"Real Return (after inflation): ${real_return:.2f}")

# UI elements for investment input
tk.Label(root, text="Investment Name:").grid(row=0, column=0)
investment_name_entry = tk.Entry(root)
investment_name_entry.grid(row=0, column=1)

tk.Label(root, text="Amount:").grid(row=1, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add Investment", command=add_investment)
add_button.grid(row=2, column=0, columnspan=2)

investments_list = tk.Listbox(root)
investments_list.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)

# UI elements for inflation and return rate input
tk.Label(root, text="Inflation Rate (%):").grid(row=0, column=2)
inflation_rate_entry = tk.Entry(root)
inflation_rate_entry.grid(row=0, column=3)

tk.Label(root, text="Return Rate (%):").grid(row=1, column=2)
return_rate_entry = tk.Entry(root)
return_rate_entry.grid(row=1, column=3)

calculate_button = tk.Button(root, text="Calculate Real Return", command=calculate_real_return)
calculate_button.grid(row=2, column=2, columnspan=2)

real_return_label = tk.Label(root, text="Real Return (after inflation):")
real_return_label.grid(row=3, column=2, columnspan=2)

# Start the GUI event loop
root.mainloop()

