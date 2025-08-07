import numpy as np
import matplotlib.pyplot as plt


scenarios = [
    (10_000, 10e-9),    # 10kΩ, 10nF
    (20_000, 10e-9),    # 10kΩ, 10nF
    (40_000, 10e-9),    # 10kΩ, 10nF
    (80_000, 10e-9),    # 10kΩ, 10nF
    (160_000, 10e-9),    # 10kΩ, 10nF
    (320_000, 10e-9),    # 10kΩ, 10nF
    (640_000, 10e-9),    # 10kΩ, 10nF
    # (10_000, 100e-9),   # 10kΩ, 100nF
    # (100_000, 10e-9),   # 100kΩ, 10nF
    # (100_000, 47e-9),   # 100kΩ, 47nF
    # (200_000, 220e-9), # 200kΩ, 220nF
    # (50_000, 47e-9),    # 50kΩ, 47nF
    # (22_000, 100e-9),   # 22kΩ, 100nF
    # (470_000, 10e-9)    # 470kΩ, 10nF
]

# Frequency range for plotting
frequencies = np.logspace(1, 5, 500)  # 10 Hz to 100 kHz

# line_styles = ['-', '--', '-.', ':', '-', '--', '-.', ':']
# markers = ['o', 's', '^', 'v', 'x', '*', 'D', '+']

plt.figure(figsize=(12, 8))

for i, (R, C) in enumerate(scenarios):
    print(f'R={R}, C={C}')
    fc = 1 / (2 * np.pi * R * C)  # Calculate cutoff frequency
    gain = 1 / np.sqrt(1 + (frequencies / fc) ** 2)  # Low-pass gain
    # gain = (frequencies / fc) / np.sqrt(1 + (frequencies / fc) ** 2)  # High-pass gain
    gain_db = 20 * np.log10(gain)
    label = f'R={R/1000:.0f}kΩ, C={C*1e9:.0f}nF, fc={fc:.1f}Hz'
    if np.any(np.isnan(gain_db)) or np.any(np.isinf(gain_db)):
        print(f"Skipping R={R}, C={C} due to invalid values.")
        continue
    print(f'Plotting: {label}')
    # plt.semilogx(frequencies, gain_db, label=label, linestyle=line_styles[i % len(line_styles)],marker=markers[i % len(markers)], markevery=50)
    plt.semilogx(frequencies, gain_db, label=label)

plt.axhline(-3, color='gray', linestyle='--', label='-3 dB cutoff')
plt.title('Frequency Response of Different RC Low-Pass Filters')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.ylim(-30, 2)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend(loc='lower left', fontsize='small')
plt.tight_layout()
plt.show()