# Eletronics


## Etching
Etching is the process of removing excess copper from a printed circuit board (PCB) to form the desired conductive traces. Traditionally, ferric chloride was the go-to etching solution in workshops, but nowadays, alternatives like sodium persulfate and photoresist methods with UV-sensitive films are more commonly used for cleaner and more precise results.

### Sodium Persulfate

Sodium persulfate (Na2S2O8) is a strong oxidizer. When you dissolve it in water and put a PCB into the solution, the persulfate releases oxygen atoms that react with the copper. This reaction turns the solid copper into copper ions (Cu²⁺), which dissolve into the solution, effectively "eating away" the unwanted copper and leaving only the protected parts (covered by ink, for example).

![mol]

The products of this reaction are copper sulfate (CuSO₄) in solution (this is why the etching solution turns blue over time) and excess sodium sulfate (Na₂SO₄).

Sodium Persulfate can be found in eletronics shops or Amazon, example:
![sodium_persulfate]

## Transfer to board

To transfer a circuit design onto a PCB, you can use regular paper, though etching paper (available on Amazon or AliExpress) is recommended. You'll need a toner printer to print the layout. After printing, place the layout face-down on the PCB and apply heat—using a clothes iron pressed firmly against the board for about 3 to 5 minutes.

Here's a comparison between regular paper (top) and etching paper (bottom). While regular paper does work, it can be tricky to clean the PCB afterward, as the toner often causes the paper to stick stubbornly to the copper.

![paper_vs_etching_paper]

Once the etching is complete, you can use alcohol to wipe out the protective toner (or ink):

![clear_results]

## Drilling

### Drilling the PCB

You can use a Dremel or a drill press to drill the holes for mounting the electronic components.

A **0.8mm** drill bit is ideal for most components (see below).

![drill_bits]

![drilled]

### Drilling the aluminium case

To drill into the aluminum case, a drill kit like the one below can be used along with a handheld drill or, preferably, a drill press. You can use a pointed metal tool and a hammer to mark the drilling spot, which helps guide the drill bit.

When using a handheld drill, even slight movements can cause the hole to go off-center, so a steady hand is essential.

![drill_kit]

## Assembly

Assembling the components inside the aluminum case can be tricky as the space becomes quite limited once you install the footswitch along with the input and output jacks. The wiring you choose plays a big role: using too many wires, or wires that are too long, will make the assembly unnecessarily complicated.

Typically, **22 or 24 AWG stranded wire** is used because of its flexibility.

> Brand quality also matters: cheap wires tend to break easily due to the poor quality of the metal.

Example of a custom made MXR Distortion+:

![pedal]


[sodium_persulfate]: assets/sodium_persulfate.jpg "Sodium persufate"
[paper_vs_etching_paper]: assets/paper_vs_etching_paper.jpg "paper_vs_etching_paper"
[clear_results]: assets/clear_results.jpg "clear_results"
[drilled]: assets/drilled.jpg "drilled"
[mol]: assets/sodium_persulfate_mol.png "mol"
[drill_bits]: assets/drill_bits.jpg "drill_bits"
[drill_kit]: assets/drill_kit.jpg "drill_kit"
[pedal]: assets/pedal.jpg "pedal"