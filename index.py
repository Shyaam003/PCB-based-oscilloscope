import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Serial port settings (adjust COM port as per your system)
SERIAL_PORT = 'COM3'  # Replace with your Arduino's COM port
BAUD_RATE = 115200
MAX_SAMPLES = 200  # Number of samples to read per capture cycle

# Create a serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Setup for plotting
fig, ax = plt.subplots()
x = np.arange(MAX_SAMPLES)
y = np.zeros(MAX_SAMPLES)
line, = ax.plot(x, y)

# Set up the plot's labels and title
ax.set_ylim(0, 1023)  # Arduino analogRead gives values from 0 to 1023
ax.set_title("Arduino Oscilloscope")
ax.set_xlabel("Time (ms)")
ax.set_ylabel("Analog Value")

def update(frame):
    """This function will be called to update the plot."""
    # Read the new data from Arduino
    line_data = ser.readline().decode('utf-8').strip()
    # Convert string data into a list of integers
    data = list(map(int, line_data.split(',')))
    
    # Update the plot with new data
    y[:] = data  # Assign the new data to the y-values
    line.set_ydata(y)
    
    return line,

# Create an animation that updates the plot every 100ms
ani = FuncAnimation(fig, update, blit=True, interval=100)

# Show the plot
plt.show()
