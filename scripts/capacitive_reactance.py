import numpy as np
import matplotlib.pyplot as plt

# Frequency range from 20 Hz to 5 kHz, logarithmic scale
frequencies = np.logspace(np.log10(20), np.log10(5000), 500)

# 8 capacitor values in Farads (common values from µF to nF)
capacitor_values = [
    1e-6,   # 1 µF
    470e-9, # 470 nF
    220e-9, # 220 nF
    100e-9, # 100 nF
    47e-9,  # 47 nF
    22e-9,  # 22 nF
    10e-9,  # 10 nF
    1e-9    # 1 nF
]

plt.figure(figsize=(10, 6))

# Plot capacitive reactance for each capacitor value
for C in capacitor_values:
    Xc = 1 / (2 * np.pi * frequencies * C)
    plt.plot(frequencies, Xc, label=f'{C*1e9:.0f} nF')

# Configure plot
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Capacitive Reactance (Ω)')
plt.title('Capacitive Reactance vs Frequency for Various Capacitor Values')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(title='Capacitor Value')
plt.tight_layout()
plt.show()