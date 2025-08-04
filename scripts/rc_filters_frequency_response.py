import numpy as np
import matplotlib.pyplot as plt


scenarios = [
    (10_000, 10e-9),    # 10kΩ, 10nF
    (10_000, 100e-9),   # 10kΩ, 100nF
    (100_000, 10e-9),   # 100kΩ, 10nF
    (100_000, 47e-9),   # 100kΩ, 47nF
    (1_000_000, 220e-12), # 1MΩ, 220pF
    (50_000, 47e-9),    # 50kΩ, 47nF
    (22_000, 100e-9),   # 22kΩ, 100nF
    (470_000, 10e-9)    # 470kΩ, 10nF
]

# Frequency range for plotting
frequencies = np.logspace(1, 5, 500)  # 10 Hz to 100 kHz

plt.figure(figsize=(12, 8))

for R, C in scenarios:
    fc = 1 / (2 * np.pi * R * C)  # Calculate cutoff frequency
    # gain = 1 / np.sqrt(1 + (frequencies / fc) ** 2)  # Low-pass gain
    gain = (frequencies / fc) / np.sqrt(1 + (frequencies / fc) ** 2)  # High-pass gain
    gain_db = 20 * np.log10(gain)
    label = f'R={R/1000:.0f}kΩ, C={C*1e9:.0f}nF, fc={fc:.1f}Hz'
    plt.semilogx(frequencies, gain_db, label=label)

plt.axhline(-3, color='gray', linestyle='--', label='-3 dB cutoff')
plt.title('Frequency Response of Different RC High-Pass Filters')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.ylim(-30, 2)  # Fix y-axis limits here
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend(loc='lower left', fontsize='small')
plt.tight_layout()
plt.show()