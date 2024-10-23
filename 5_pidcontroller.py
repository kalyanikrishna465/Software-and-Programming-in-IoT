import numpy as np
import matplotlib.pyplot as plt

# PID Controller parameters
Kp = 2.0
Ki = 1.0
Kd = 0.5

# Time parameters
dt = 0.1  # Time step
time = np.arange(0, 50, dt)

# Desired temperature
setpoint = 100.0  # Target temperature
temperature = 20.0  # Initial temperature
error = 0.0  # Initial error
integral = 0.0  # Integral term
derivative = 0.0  # Derivative term

# Lists to store results for plotting
temperatures = []
setpoints = []

# PID Controller simulation
for t in time:
    # Calculate error
    error = setpoint - temperature
    
    # Calculate integral and derivative
    integral += error * dt
    derivative = (error - derivative) / dt if t > 0 else 0
    
    # Calculate control output
    control_output = Kp * error + Ki * integral + Kd * derivative
    
    # Simulate temperature response (simple first-order system)
    temperature += (control_output - (temperature - 20.0)) * dt
    
    # Store the temperature and setpoint for plotting
    temperatures.append(temperature)
    setpoints.append(setpoint)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(time, temperatures, label='Temperature (°C)', color='blue')
plt.plot(time, setpoints, label='Setpoint (°C)', color='red', linestyle='--')
plt.title('PID Controller for Temperature Regulation')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid()
plt.show()