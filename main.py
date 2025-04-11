import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Function to draw confetti inside the Tkinter window
def draw_confetti():
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set the size of the figure
    fig.set_size_inches(4, 4)  # Smaller size for embedding

    # Generate random positions for confetti
    x = np.random.rand(100)
    y = np.random.rand(100)

    # Generate random colors for confetti
    colors = np.random.rand(100)

    # Generate random sizes for confetti
    sizes = 1000 * np.random.rand(100)

    # Scatter plot to draw confetti
    ax.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')

    # Remove axes
    ax.set_axis_off()

    # Embed the figure in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=2, column=0, columnspan=2, pady=10)
    canvas.draw()

# Function to show birthday message and confetti
def show_birthday_message():
    # Hide the question and buttons
    question_label.grid_forget()
    yes_button.grid_forget()
    no_button.grid_forget()

    # Show the birthday message
    message_label.config(text="¡Feliz cumpleaños!")
    draw_confetti()

# Function to handle "No" button click
def handle_no_button():
    question_label.config(text="¿Seguro que no es tu cumpleaños?")
    yes_button.config(text="Sí", command=close_program)
    no_button.config(text="No", command=reset_question)

# Function to close the program
def close_program():
    message_label.config(text="Okay, bye")
    root.after(1000, root.quit)  # Wait 2 seconds before closing

# Function to reset to the first question
def reset_question():
    question_label.config(text="¿Hoy es tu cumpleaños?")
    yes_button.config(text="Sí", command=show_birthday_message)
    no_button.config(text="No", command=handle_no_button)

# Create the main window
root = tk.Tk()
root.title("Felicidades")

# Ensure the program exits completely when the window is closed
root.protocol("WM_DELETE_WINDOW", root.quit)

# Set the initial size of the window
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Center the window on the screen
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Configure the grid layout
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Create a label with the question
question_label = tk.Label(root, text="¿Hoy es tu cumpleaños?", font=("Arial", 16))
question_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create a label to display the message
message_label = tk.Label(root, text="", font=("Arial", 16))
message_label.grid(row=1, column=0, columnspan=2, pady=10)

# Create buttons for "Sí" and "No"
yes_button = tk.Button(root, text="Sí", command=show_birthday_message, font=("Arial", 14))
yes_button.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

no_button = tk.Button(root, text="No", command=handle_no_button, font=("Arial", 14))
no_button.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

# Run the application
root.mainloop()