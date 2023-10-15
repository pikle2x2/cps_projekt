import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time

# Function to simulate reading analog data from the sensor (replace this with actual sensor reading)
def get_analog_data():
    return random.randint(60, 100)

# Function to convert analog data to BPM
def convert_to_bpm(analog_data):
    return int((analog_data - 60) * 1.5)  # Replace this with your conversion formula

# Function to update BPM display
def update_bpm_display():
    analog_data = get_analog_data()
    bpm = convert_to_bpm(analog_data)
    bpm_label.config(text=f"Current BPM: {bpm}")

    # Update graph
    x_data.append(time.time() - start_time)
    y_data.append(analog_data)
    ax.clear()
    ax.plot(x_data, y_data)
    canvas.draw()

    # Schedule the function to run after 1000ms (1 second)
    root.after(1000, update_bpm_display)

# Create main window
root = tk.Tk()
root.title("Heart Rate Monitor")

# Create a frame for BPM display
bpm_frame = tk.Frame(root)
bpm_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Create a label to display BPM
bpm_label = tk.Label(bpm_frame, font=("Arial", 24))
bpm_label.pack()

# Create a frame for the graph
graph_frame = tk.Frame(root)
graph_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Create a figure for the graph
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Analog Data')
ax.set_title('Heart Rate Monitor')

# Create a canvas to display the graph
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.draw()
canvas.get_tk_widget().pack()

# Initialize data
x_data = []
y_data = []
start_time = time.time()

# Start the data update loop
update_bpm_display()

# Start the main event loop
root.mainloop()
