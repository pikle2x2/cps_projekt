import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define parameters
frequency = 10  # Frequency in Hz
amplitude = 2  # Amplitude in V
duration = 1   # Duration of animation in seconds

# Calculate the angular frequency (2 * pi * frequency)
omega = 2 * np.pi * frequency

# Define time array
t = np.linspace(0, duration, int(1000 * duration))

# Create a function to generate the sinusoidal wave
def generate_wave(t):
    return amplitude * np.sin(omega * t)

# Create the figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [])

# Set axis limits
ax.set_xlim(0, duration)
ax.set_ylim(-2.5, 2.5)

# Initialize function to draw each frame
def init():
    line.set_data([], [])
    return line,

# Function to update animation frames
def update(frame):
    x = t[:frame]
    y = generate_wave(t)[:frame]
    line.set_data(x, y)
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, repeat=False, interval=1)

# Display the animation
plt.show()
