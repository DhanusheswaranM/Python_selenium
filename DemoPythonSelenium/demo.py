import numpy as np
import matplotlib.pyplot as plt

# Define PWM signal parameters
frequency = 50  # Hz
period = 1 / frequency  # in seconds
pulse_width_min = 1  # ms (0°)
pulse_width_max = 2  # ms (180°)
pulse_width_neutral = 1.5  # ms (90°)

# Time array (in milliseconds)
time_ms = np.linspace(0, period * 1000, 1000)  # 1000 points over one period

# PWM signal array (in milliseconds)
pulse_widths = np.linspace(pulse_width_min, pulse_width_max, len(time_ms))

# Create the PWM signal
pwm_signal = np.zeros_like(time_ms)
for i in range(len(time_ms)):
    if time_ms[i] % period * 1000 < pulse_widths[i]:
        pwm_signal[i] = 1  # High
    else:
        pwm_signal[i] = 0  # Low

# Plot the PWM signal
plt.figure(figsize=(10, 4))
plt.plot(time_ms, pwm_signal, drawstyle='steps-pre')
plt.title('PWM Signal for Servo Motor')
plt.xlabel('Time (ms)')
plt.ylabel('PWM Signal (High/Low)')
plt.grid(True)
plt.show()

# Add vertical lines for specific angles
plt.axvline(x=pulse_width_min * 1000, color='r', linestyle='--', label='0°')
plt.axvline(x=pulse_width_neutral * 1000, color='g', linestyle='--', label='90°')
plt.axvline(x=pulse_width_max * 1000, color='b', linestyle='--', label='180°')

# Add legend
plt.legend()