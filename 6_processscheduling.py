class IoTDevice:
    def __init__(self, name, burst_time):
        self.name = name  # Name of the device
        self.burst_time = burst_time  # Total processing time required
        self.remaining_time = burst_time  # Remaining time to be processed

def round_robin_scheduling(devices, time_quantum):
    time = 0  # Start time
    while any(device.remaining_time > 0 for device in devices):
        for device in devices:
            if device.remaining_time > 0:
                if device.remaining_time > time_quantum:
                    time += time_quantum
                    device.remaining_time -= time_quantum
                    print(f'Time {time}: {device.name} processed for {time_quantum}s')
                else:
                    time += device.remaining_time
                    print(f'Time {time}: {device.name} processed for {device.remaining_time}s')
                    device.remaining_time = 0

# Example usage
devices = [
    IoTDevice("Temperature Sensor", 10),
    IoTDevice("Humidity Sensor", 5),
    IoTDevice("Pressure Sensor", 8)
]

time_quantum = 3  # Set time quantum for each task
round_robin_scheduling(devices, time_quantum)