import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# Function to draw confetti
def draw_confetti():
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set the size of the figure
    fig.set_size_inches(8, 8)

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

    # Show the plot
    plt.show()

# Function to show birthday message and confetti
def show_birthday_message():
    message_label.config(text="¡Feliz cumpleaños!")
    draw_confetti()

# Create the main window
root = tk.Tk()
root.title("Felicidades")

# Create a label with the question
question_label = tk.Label(root, text="¿Hoy es tu cumpleaños?")
question_label.pack()

# Create a label to display the message
message_label = tk.Label(root, text="")
message_label.pack()

# Create buttons for "Sí" and "No"
yes_button = tk.Button(root, text="Sí", command=show_birthday_message)
yes_button.pack(side=tk.LEFT, padx=10)

no_button = tk.Button(root, text="No", command=root.quit)
no_button.pack(side=tk.RIGHT, padx=10)

# Run the application
root.mainloop()