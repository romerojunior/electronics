import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
f = 50  # Frequency in Hz
omega = 2 * np.pi * f  # Angular frequency (rad/s)
t = np.linspace(0, 0.04, 1000)  # Time vector: 0 to 40 ms (~2 cycles of 50 Hz)

# Current through capacitor: assume sine wave
I = np.sin(omega * t)

# Voltage across capacitor: lags current by 90° (π/2 radians)
V = np.sin(omega * t - np.pi / 2)  # Same as cos(omega * t)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(t * 1000, I, label='Current through Capacitor (I)', linewidth=2)
plt.plot(t * 1000, V, label='Voltage across Capacitor (V)', linewidth=2, linestyle='--')
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')

plt.title('Phase Shift in Capacitor: Current Leads Voltage by 90°')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()