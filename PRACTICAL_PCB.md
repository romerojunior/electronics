# Printed Circuit Boards

## PCB Transfer

To prepare the PCB, make sure it the copper is clean: free of any residue, stains, fingerprints, rust and so on. If necessary use a light sandpaper to make sure the copper will be fully exposed to the etching solution.

To transfer a circuit design onto a PCB, you can use regular paper, though etching paper (toner transfer paper) is recommended. You'll need a toner printer to print the layout. After printing, place the layout face-down on the PCB and apply heat—using a clothes iron pressed firmly against the board for about 3 to 5 minutes.

Here's a comparison between regular paper (top) and etching paper (bottom). While regular paper does work, it can be tricky to clean the PCB afterward, as the toner often causes the paper to stick stubbornly to the copper.

![paper_vs_etching_paper]


|Material|Price|Links|
|---|---|---|
|Etching paper|Starts at €3,00|[Amazon](https://www.amazon.com/Ximimark-20Pcs-Transfer-Electronic-Prototype/dp/B07MYXK4WJ), [AliExpress](https://aliexpress.com/item/32800926240.html)|
|PCB board|Starts at €6,00|[Amazon](https://www.amazon.nl/FOROREH-Koperen-Printplaat-Eenzijdige-Ketels/dp/B087M1GDCP), [AliExpress](https://nl.aliexpress.com/item/1005004595360265.html)|

## PCB Etching

Etching is the process of removing excess copper from a printed circuit board (PCB) to form the desired conductive traces. Traditionally, ferric chloride was the go-to etching solution in workshops, but nowadays, alternatives like sodium persulfate and photoresist methods with UV-sensitive films are more commonly used for cleaner and more precise results.

### Sodium Persulfate

![mol]

Sodium persulfate (Na₂S₂O₈) is a strong oxidizer. When you dissolve it in water and put a PCB into the solution, the persulfate releases oxygen atoms that react with the copper. This reaction turns the solid copper into copper ions (Cu²⁺), which dissolve into the solution, effectively "eating away" the unwanted copper and leaving only the protected parts (covered by ink, for example).

![etching]

With 100g of sodium persulfate per 0,5L at 50°c the process takes about 30 minutes.

The products of this reaction are copper sulfate (CuSO₄) in solution (this is why the etching solution turns blue over time) and excess sodium sulfate (Na₂SO₄).

Sodium persulfate can be found in eletronics shops or Amazon, example:
![sodium_persulfate]

> #### ⚠️ Precautionary statements:
>
>- Keep away from heat, hot surfaces, sparks, open flames and other ignition
>sources.
>- Avoid breathing dust/fume/gas/mist/vapours/spray.
>- Wear protective gloves.
>
> Safaty data sheet available [here](https://www.fishersci.com/store/msds?partNumber=O61141&countryCode=US&language=en).


Once the etching is complete, you can use alcohol or gasoline to wipe out the protective toner (or ink):

![clear_results]

|Material|Price|Links|
|---|---|---|
|Sodium Persulfate (1 kg)|Starts at €19,00|[Amazon](https://www.amazon.nl/dp/B08WPX5K6J)|

## Drilling

### Drilling the PCB

You can use a Dremel or a drill press to drill the holes for mounting the electronic components.

A **0.8mm** drill bit is ideal for most components (see below).

![drill_bits]

![drilled]


|Material|Price|Links|
|---|---|---|
|0,8-3,2 mm drill set|Starts at €7,00|[Amazon](https://www.amazon.nl/Dremel-628-Boorset-Borenset-Multitool/dp/B0002SMO5Y)|


### Drilling the aluminium case

To drill into the aluminum case, a step drill kit like the one below can be used along with a handheld drill or, preferably, a drill press. You can use a pointed metal tool and a hammer to mark the drilling spot, which helps guide the drill bit.

When using a handheld drill, even slight movements can cause the hole to go off-center, so a steady hand is essential.

![drill_kit]

|Material|Price|Links|
|---|---|---|
|Step drill set|Starts at €6,00|[Amazon](https://www.amazon.nl/Mesybveo-trappenboorset-kegelboor-zeskantige-kegeltrappenboor/dp/B0CCJJPHSH), [AliExpress](https://nl.aliexpress.com/item/1005005882425579.html)|

## Assembly

Assembling the components inside the aluminum case can be tricky as the space becomes quite limited once you install the footswitch along with the input and output jacks. The wiring you choose plays a big role: using too many wires, or wires that are too long, will make the assembly unnecessarily complicated.

Typically, **22 or 24 AWG stranded wire** is used because of its flexibility.

> Brand quality also matters: cheap wires tend to break easily due to the poor quality of the metal.

Example of a custom made pedal inspired on the classic MXR Distortion+:

![pedal]

## Workshop Tools for working with PCBs

List of asorted tools used in the workshop:

- Drill press, [Amazon](https://www.amazon.nl/EBERTH-Tafelboormachine-kolomboormachine-spindelslag-werkplaatsgereedschap/dp/B01DUEDPX6)
- Dremel, [Amazon](https://www.amazon.nl/Dremel-3000-Multitool-130W-Multifunctioneel/dp/B014UXZHGY)
- Multimeter, [Amazon](https://www.amazon.nl/Aeyytoe-DC-spanning-achtergrondlicht-spanningsmeter-elektriciens/dp/B0C8214NBM)
- Oscilloscope, [Amazon](https://www.amazon.nl/HANMATEK-Digitale-Oscilloscoop-Laboratorium-DOS1102/dp/B0833X3RFK)
- Cutting mat, [Amazon](https://www.amazon.nl/Zelfgenezende-roterende-dubbelzijdige-knutselsnijplank-plakboekproject/dp/B088LZNS1M)
- Breadboards, [Amazon](https://www.amazon.nl/Solderless-Prototype-Breadboard-Protoboard-Universal/dp/B07MY24K28)
- Function Generator, [Amazon](https://www.amazon.nl/ANGEEK-Generator-Adjustable-Frequency-Amplitude/dp/B08LGRG7L2)
- Soldering Iron, [Amazon](https://www.amazon.nl/Lytool-Soldeerstation-Display-Temperatuurbereik-Wachtwoordbeveiliging/dp/B0987H26KP)
- Solder tin, [Amazon](https://www.amazon.nl/Soldeertin-soldeerdraad-soldeertin-vloeimiddel-colofonium/dp/B07SRXWBDS)
- Solder wick, [Amazon](https://www.amazon.nl/dp/B093ZYD79M/ref=sspa_dk_detail_1?pd_rd_i=B093ZYD79M)
- 24 AWG wires, [Amazon](https://www.amazon.nl/gp/product/B089CHVN7G)
- Shrinkable sleeves, [Amazon](https://www.amazon.nl/Eventronic-Krimpkous-Waterdicht-Elektrische-Draadschakelaars/dp/B08SMGQ93M)


<!-- Assets -->
[sodium_persulfate]: assets/sodium_persulfate.jpg "Sodium persufate"
[paper_vs_etching_paper]: assets/paper_vs_etching_paper.jpg "paper_vs_etching_paper"
[clear_results]: assets/clear_results.jpg "clear_results"
[drilled]: assets/drilled.jpg "drilled"
[mol]: assets/sodium_persulfate_mol.png "mol"
[drill_bits]: assets/drill_bits.jpg "drill_bits"
[drill_kit]: assets/drill_kit.jpg "drill_kit"
[pedal]: assets/pedal.jpg "pedal"
[etching]: assets/etching.gif "etching"