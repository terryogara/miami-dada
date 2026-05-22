![Status](https://img.shields.io/badge/status-completed-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-blue)

---

# TITLE: 'Miami Dada' 🌴👮‍♂️🚨
# COMPOSER: Terry O'Gara
# DATE: 12/07/2023

# About the Work
'Miami Dada' is a cinematic computer music composition created with Python. It explores 
the intersection of cabaret and 1980s-era 'Miami Vice' style noir through a programmatic 
lens, utilizing a layered approach to synthesis and sound design to capture that specific 
atmospheric, high-stakes aesthetic.

## Detail
* **Composition:** Approx. 2-minute original track.
* **Engine:** Built using [SCAMP](https://scamp.readthedocs.io/) (Suite
for Computer-Assisted Music Production).
* **Assets:** Utilizes 36 custom instruments and sound effects across
three SoundFonts (.sf2).

## Technical Implementation
The code is structured to manage complex musical layering:
* **27 musical part functions** nested into **9 musical section
functions**.
* **Advanced Sequencing:** Uses `fork()` to manage multi-part
concurrency and rhythmic timing.
* **Logic:** Employs range commands and iterative loops to create
dynamic, non-repetitive textures.

### Code Organization
* **Section A:** Sample Triggers and Instrument Definitions.
* **Section B:** Core Musical Functions.
* **Section C:** Musical Section Definitions.
* **Section D:** 'Play Music' Execution and Forks.

## Musical Structure
The piece follows a traditional yet programmatic arrangement:
1. Intro
2. Verse
3. Chorus
4. Breakdown / Bridge
5. Chorus (Outro)

## Assets & SoundFonts
This composition relies on external SoundFont files to achieve its cinematic, 
noir-cabaret sound. If you wish to run the code locally, please download the following:

* **[Synths.sf2](https://www.polyphone.io/en/soundfonts/synthesizers/186-various-synths)**: A collection of sampled electronic synthesizers and effects.
* **[Emu_Planet_Phatt_Hip_Hop.sf2](https://www.polyphone.io/en/soundfonts/instrument-sets/405-planet-phatt-examples)**: Iconic sounds from the classic 1990s E-mu Systems hardware module.

> **Important Note:** After downloading these files, ensure they are renamed exactly to
 `Synths.sf2` and `Emu_Planet_Phatt_Hip_Hop.sf2` respectively, and place them in the 
 same folder as the Python script.

---

## How to Listen/Run
1. **Requirements:** Ensure you have Python installed and the SCAMP
library.
   `pip install scamp`
2. **Setup:** Place your SoundFont files (`Synths.sf2`,
`Emu_Planet_Phatt_Hip_Hop.sf2`) in the project directory.
3. **Execution:** Run the script from your terminal:
   `python3 miamidada_terryogara_120723.py`
4. Customization Note: By default, this script saves the composition to a .wav file. 
If you prefer to listen without saving to your disk, open miami-dada.py and change 
GENERATE_WAV = True to GENERATE_WAV = False.

*(Note: Audio preview is available in the
[Releases](https://github.com/terryogara/compmus-miamidada/releases)
section.)*

---
**Copyright © 2022–2026 Terry O'Gara. All rights reserved.**