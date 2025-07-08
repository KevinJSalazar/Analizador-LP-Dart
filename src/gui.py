import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Set window size
root.geometry("400x300")

# Add a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=50)

# Add a button
def on_button_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Start the GUI event loop
root.mainloop()