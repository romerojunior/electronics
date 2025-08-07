# Theory: Resistors and Capacitors

## Basic Concepts

**Current (I)** is the flow of electric charge (how many electrons are moving through a wire per second), and it's measured in Amperes (A).

There are two main types or currents:

- DC (Direct Current): Flows in one direction (linear);
- AC (Alternating Current): Changes direction back and forth (sine wave).

When building audio circuits, you're dealing with both DC and AC.

Audio circuits are powered by DC (usually 9V DC from a battery or power supply), which powers the components like op-amps, transistors, etc. However, a guitar signal is AC, because the voltage fluctuates back and forth as the strings vibrate. It's a small AC signal (usually millivolts to a few volts), carrying the instrument tone.

---

**Voltage (V)** is the **electric potential*** difference between two points. It’s what pushes electric current through a circuit. It's measured in Volts (V).

> \* Electrons (negative charges) want to move toward positive potential, because opposites attract. Electrons move from low to high potential energy, which, because they’re negatively charged, means they flow from negative to positive voltage. But in circuit diagrams we often show conventional current (as if positive charges move from + to –). In reality electrons flow from – to +, but the effect is the same.

Water flow analogy: *Voltage is like the water pressure. Current is like the amount of water flowing. Without pressure (voltage), water (current) won’t flow.*

---

**Impedance** is like resistance but for AC signals. It accounts for how capacitors (capacitive reactance) and inductors (inductive reactance) behave at different frequencies.

---

**Decibel (dB)**  is a logarithmic unit used to measure ratios — often for power, voltage, or signal strength. In audio and electronics, it's commonly used to express gain or loss of a signal.

The formula to convert a voltage ratio into decibels is:

`dB = 20 x log^10(Vout/Vin)`

Positive results represents a gain, negative results represents a loss.

| Voltage Ratio | dB     | Meaning             |
| ------------- | ------ | ------------------- |
| 1             | 0 dB   | No change           |
| 0.707         | -3 dB  | Half power (cutoff) |
| 0.5           | -6 dB  | Half voltage        |
| 2             | +6 dB  | Double voltage      |
| 10            | +20 dB | 10× voltage         |


### Ohm's Law

Voltage equals current times resistance. When applied to audio circuits, Ohm’s Law lets you control voltage, current, and signal strength in any part of the circuit, from gain stages to tone controls.

`V = I × R`

Where:
- **V** = Voltage
- **I** = Current
- **R** = Resistance

## Resistors

A resistor limits the amount of current flowing through a circuit and can create voltage drops. The amount of resistance is measured in ohms (Ω).

Resitors behave in both AC and DC the same way. It does not care about frequency, only about how much current is trying to pass.

In audio circuits, these are the most common types of resistors and how they are used:

| **Type**| **Description** | **Use Case in Guitar Pedals** |
| --- | --- | --- |
| **Carbon Film Resistors** | Made of carbon film, cheap, with ±5% tolerance. Slight noise at high frequencies. Typically light brown color. | Good for general-purpose circuits and vintage tones. |
| ⭐ **Metal Film Resistors** | Made of metal film, low noise, ±1% tolerance. Stable and precise. Typically light blue color.| Preferred in high-fidelity or low-noise pedal designs. |
| **Carbon Composition** | Old-school carbon powder/binder. Warmer tone but less stable, noisy.| Used for vintage-style fuzz/distortion pedals. |
| **Variable Resistors (Potentiometers and Pot-trimmers)** | Adjustable resistance. Potentiometers are knobs; trimmers are small screwdriver-adjustable types. | Used for volume, tone, gain controls in pedals. |

> **Recommended Starter Kit**
>
> * Carbon Film or Metal Film Resistors: 10Ω to 1MΩ in standard values for 1/4w.
> * Potentiometers: 10kΩ, 50kΩ, 100kΩ, 500kΩ, 1MΩ (logarithmic/audio taper for volume/tone).

---

### Voltage Divider

A voltage divider is a circuit made of two resistors (or more) that splits voltage. As long as the values of `R` are the same, the voltage output will be 1/2 of the voltage output.

If you have resistors R1 and R2, and input voltage Vin, the output voltage is:

`Vout = Vin x (R2 / (R1+R2))`

* If `V(in) = 9V` then `V(out) = 4.5V`.

```css
In →---[R]---+----> Output
             |
            [R]
             |
            GND
```

Voltage dividers can be used to:
- Reduce a hot input signal to prevent distortion/clipping at the input stage.
- Adjusts the final signal level sent to your amp.
- Set a stable DC voltage point (bias) for active components.
- Blend clean and processed signals.

## Capacitors

A capacitor stores and releases electrical energy. It resists changes in voltage by temporarily holding charge, making it useful for filtering, timing, and signal coupling. Measured in Farads (F).

Capacitors behave quite differently in AC (Alternating Current) circuits compared to DC (Direct Current) circuits. In DC circuits, a capacitor charges up and then acts like an open circuit (blocks current flow). In AC circuits, because the voltage is constantly changing direction, the capacitor is constantly charging and discharging, allowing AC to pass through.

However, low frequencies (bass) are passed less effectively, and high frequencies (treble) pass more easily.

A capacitor in an AC circuit introduces something called capacitive reactance (`Xc`), which is a **frequency-dependent resistance**. It is also used to calculate the total impedance of a circuit.

`Xc = 1 / (w * C)` where `w = 2 * π * f`.

Where:
- **Xc** = Capacitive reactance (Ohms, Ω)
- **f** =  Frequency of the AC signal (Hz)
- **C** = Capacitance (Farads, F)
- **w** = Angular frequency (`2 * π * f`) (Rad/s)
- π ≈ 3.1416

Below is a chart with the `Xc` for different capacitor values for a typical guitar signal range (82 Hz to about 1,200 Hz, having in mind that guitar sounds also contain harmonics and overtones extending well beyond that, up to around 5,000 Hz or more, which contribute to the tone).

![capacitive_reactance]

In audio circuits, these are the most common types of capacitores and how they are used:

| **Type** | **Description** | **Use Case in Guitar Pedals** |
| --- | --- | --- |
| **Ceramic Capacitors** | Small, cheap, non-polarized. Value range: pF to low µF. Slightly microphonic in some cases. | Good for high-frequency filtering (tone control, noise filtering). |
| **Film Capacitors (Polyester, Polypropylene)** | Non-polarized, very stable, good audio quality. Values from nF to a few µF. | Preferred for signal paths and tone stacks in pedals. |
| **Electrolytic Capacitors** | Polarized (have + and -), larger capacitance (µF to 1000s µF), less precise. | Used for power supply filtering and DC blocking in signal paths.  |
| **Tantalum Capacitors** | Smaller than electrolytics, polarized, more stable but expensive and can fail dramatically. | Sometimes used for compact designs but not common in pedals. |

**Symbols:**

- Non-polarized: ─||─
- Polarized (Electrolytic): ─|(─

> **Recommended Starter Kit**
>
> * Film Capacitors (e.g., Polyester, Polypropylene) — nF range (like 10nF, 47nF, 100nF). Ideal for audio signal paths.
> * Ceramic Capacitors — For small values (pF-nF), good for treble filtering.
> * Electrolytic Capacitors — For µF values (1µF - 470µF), especially for power supply decoupling and DC blocking in signal lines.

Typical values used in audio electronics:

| **Type**     | **Use for**                    | **Preferred Range** |
| ------------ | ------------------------------ | ------------------- |
| Ceramic      | Treble filtering, small bypass | 100pF to 10nF       |
| Film         | Signal path, tone shaping      | 10nF to 470nF       |
| Electrolytic | Power filtering, DC blocking   | 1µF to 470µF        |

#### Unit of measure (Farads)

Converting Farads is important, since you can often find capacitor values written in different units, such as:

`0.5uF = 500nF` or `1000pf = 1nF`

| Unit Symbol | Unit Name      | Value in Farads (F)         | Multiplier (Scientific Notation) |
|-------------|----------------|-----------------------------|-----------------------------------|
| pF          | Picofarad      | 0.000 000 000 001 F          | 1 × 10⁻¹² F                      |
| nF          | Nanofarad      | 0.000 000 001 F              | 1 × 10⁻⁹ F                       |
| µF          | Microfarad     | 0.000 001 F                  | 1 × 10⁻⁶ F                       |
| mF          | MilliFarad     | 0.001 F                      | 1 × 10⁻³ F                       |
| F           | Farad          | 1 F                          | 1 × 10⁰ F                        |

### Tone shaping

At the cutoff frequency, the capacitive reactance (`Xc`) is equal to the resistance (`R`). Therefore, the frequency cut (`Fc`) can be calculate with:

`Fc = 1 / (2 * π * R * C)`

Where:
- **Fc** = Cutoff frequency (in Hz)
- **R** = Resistance (Ohms, Ω)
- **C** = Capacitance (Farads, F)
  - 1µF = 1 × 10⁻⁶ F
  - 1nF = 1 × 10⁻⁹ F
  - 1pF = 1 × 10⁻¹² F
- π ≈ 3.1416

#### Low pass filter (High cut)

```css
Signal →---[R]---+----> Output
                 |
                [C]
                 |
                GND
```
#### High pass filter (Bass Cut)

```css
Signal →---[C]---+----> Output
                 |
                [R]
                 |
                GND
```

#### Combining treble and bass controls (tone stack)

This Fender inspired circuit lets you control both treble and bass interactively:

```css
Signal →---[C1]---+----[POT1]----+
                  |              |
                 [R1]          [C2]
                  |              |
                 GND            GND
```

- C1 (Bass Cut cap): 10nF – 100nF
- C2 (Treble Cut cap): 250pF – 2nF
- POT1 (Tone Pot): 100kΩ – 250kΩ
- R1 (Resistor for shaping response): 10kΩ – 100kΩ

#### `Fc` Quick Reference Table

![rc_frequency_response]
![rc_frequency_response_h]
Source: `rc_filters_frequency_response.py`


<!-- Assets -->
[rc_frequency_response]: assets/rc_frequency_response.png "rc_frequency_response"
[rc_frequency_response_h]: assets/rc_frequency_response_h.png "rc_frequency_response_h"
[capacitive_reactance]: assets/capacitive_reactance.png "Capacitive reactance"