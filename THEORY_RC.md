# Theory: Resistors and Capacitors

Ohm's Law: Voltage equals current times resistance. Ohm’s Law lets you control voltage, current, and signal strength in every part of an audio circuit, from gain stages to tone controls.

`V = I × R`

Where:
- **V** = Voltage
- **I** = Current
- **R** = Resistance

## Resistors

A resistor limits the amount of current flowing through a circuit and can create voltage drops. The amount of resistance is measured in ohms (Ω).

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

### Voltage Divider

As long as the values of `R` are the same, the voltage output will be 1/2 of the voltage output.

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

A capacitor in an AC circuit introduces something called Capacitive Reactance (`Xc`), which is a frequency-dependent resistance:

`Xc = 1 / (2 * π * f * C)`

Where:
- **Fc** = Cutoff frequency (in Hz)
- **f** =  Frequency of the AC signal (Hz)
- **C** = Capacitance (Farads, F)
- π ≈ 3.1416


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
Source: `rc_filters_frequency_response.py`


<!-- Assets -->
[rc_frequency_response]: assets/rc_frequency_response.png "rc_frequency_response"