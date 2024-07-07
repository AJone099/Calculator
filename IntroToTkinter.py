import tkinter as tk
from tkinter import Label, Entry, Button, LabelFrame

# Function to calculate interest
def Calculate_Interest():
    try:
        # Get input values
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())
        
        # Calculate simple interest
        interest = (p * r * t) / 100
        
        # Round off the result
        interest = round(interest, 2)
        
        # Destroy previous result label if it exists
        for widget in result_frame.winfo_children():
            widget.destroy()
        
        # Display result
        result_label = Label(result_frame, text=f"Calculated Interest: {interest}")
        result_label.place(x=10, y=10)
    except ValueError:
        # Destroy previous result label if it exists
        for widget in result_frame.winfo_children():
            widget.destroy()
        
        # Display error message
        error_label = Label(result_frame, text="Please enter valid numbers")
        error_label.place(x=10, y=10)

# Create the main window
root = tk.Tk()

# Set window size
root.geometry("400x400")

# Define title for the window
root.title("Simple Interest Calculator")

# Create heading label
heading_label = Label(root, text="Simple Interest Calculator", font=("Arial", 16))
heading_label.place(x=80, y=20)

# Create and place labels and entries for Principal
principal_label = Label(root, text="Principal:")
principal_label.place(x=50, y=80)
principal_entry = Entry(root)
principal_entry.place(x=200, y=80)

# Create and place labels and entries for Rate of Interest
rate_label = Label(root, text="Rate of Interest:")
rate_label.place(x=50, y=120)
rate_entry = Entry(root)
rate_entry.place(x=200, y=120)

# Create and place labels and entries for Time
time_label = Label(root, text="Time (years):")
time_label.place(x=50, y=160)
time_entry = Entry(root)
time_entry.place(x=200, y=160)

# Create and place the Calculate button
calculate_button = Button(root, text="Calculate", command=Calculate_Interest)
calculate_button.place(x=150, y=200)

# Create a LabelFrame for the result
result_frame = LabelFrame(root, text="Result", width=350, height=100)
result_frame.place(x=25, y=250)

# Run the application
root.mainloop()
