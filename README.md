# Night Watch: Outpost Zero
### NASA Space Apps Challenge 2026 — *Build a Junior Astronaut Mission Trainer* (Ages 7–12)

> **Outpost Zero** is an interactive, browser-playable lunar mission trainer that lets students manage a permanent lunar south-pole habitat (Artemis Base Camp). Players balance competing engineering trade-offs—life support, battery storage, radiation shielding, food production, and communication lag—experiencing firsthand the real constraints faced by NASA mission planners.

---

## 🎮 How to Play

### Controls
- **PC / Chromebook / Mac**:
  - **Move**: Arrow keys or `W` `A` `S` `D`
  - **Interact / Select / Confirm**: `Z`, `Enter`, or `Spacebar`
  - **Back / Menu / Field Guide**: `X` or `Escape`
  - **Mute Audio**: `M`
  *(No on-screen pad is displayed on PC, keeping the screen clean).*

- **Phone / Tablet (Touch Devices)**:
  - Automatically displays a **Nintendo Handheld Controller**:
    - **Left**: Classic D-Pad cross for smooth navigation.
    - **Right**: Angled Action Buttons: **`Z` (INTERACT)** and **`X` (BACK / MENU)**.
    - **Landscape Mode**: D-Pad and buttons automatically dock to the bottom corners for comfortable thumb play (like a Game Boy Advance / Nintendo Switch).

---

## 🚀 Key Features

### 1. Interactive Real Outpost Habitat & Machines
During daytime, the player (Duty Officer) explores the outpost and manages critical systems before nightfall:
- **ECLSS Water Recycler (`W`)**: Simulates the ISS Water Recovery System, which recycles 98% of all moisture and urine into pure drinking water. Purging filters refreshes the air scrubbers.
- **ECLSS Oxygen Generator (`O`)**: Splits water into breathable $O_2$ through electrolysis (like ISS OGA and Mars MOXIE). Players can toggle between **Balanced**, **Boost** (+Air, drains Power), and **Eco** (saves Power for cold nights).
- **Hydroponic Greenhouse Bay (`G`)**: Simulates the NASA **Veggie** and **Advanced Plant Habitat (APH)**. Astronauts grow dwarf wheat and radishes to absorb $CO_2$, generate fresh $O_2$, and boost crew mental health.
- **ISRU 3D Regolith Fabricator (`3`)**: In-Situ Resource Utilization workshop that 3D-prints spare rover gears and suit seal patches from lunar soil + binder. Printing an emergency kit during the day provides instant auto-repair protection during sudden emergencies!
- **Bio-Dosimetry & Medical Station (`M`)**: Active crew radiation dosimetry monitoring cumulative radiation dose ($mSv$) and habitat hull shielding integrity.
- **Central Night Console (`C`)**: Receives live NOAA space weather uplinks, monitors battery reserves, and initiates the 14-night freeze.

### 2. Visually Clear, Accessible & Rewarding Minigames
Each emergency features a high-contrast visual tutorial card (**"HOW TO FIX IT"**) and generous difficulty tuning designed for young players:
- **Rover Motor Fault (Reboot Sequence)**:
  - Big, vibrantly color-coded directional arrows (Up: Cyan, Down: Amber, Left: Purple, Right: Green).
  - Clear 3-step sequence with musical chime audio feedback and generous 5-fault allowance.
- **Dust on Solar Panels (Sweep & Wipe)**:
  - Smooth vacuum/wiper cursor sweeps over 18 solar cells.
  - Sparkling particle bursts as panels instantly turn from dusty gray to gleaming photovoltaic silicon!
  - Clear progress bar counter (XX/18 Clean) with generous 50-second timer.
- **Habitat Air Leak (Sonar Radar Locator)**:
  - High-contrast hot/cold sonar heatmap grid. Visited tiles permanently color-code from Deep Blue (Cold) to Amber (Warm) to Blinking Red (Leak!).
  - Sonar audio pings beep faster and higher as you get closer to the puncture.
  - Big "PRESS Z TO SEAL" prompt with a satisfying pneumatic repair sound.
- **Comms Dish Misaligned (Radio Lock)**:
  - Broad green target zone with smooth pendulum sweep.
  - Resonant harmonic audio tone and flashing "LOCKED ON! PRESS Z NOW!" prompt when in target zone.
  - Teaches the real 1.3-second light-speed radio delay between Earth and the Moon.

### 3. Real Live Space Weather (NOAA SWPC) & Environmental Simulation
No API key required! The game directly fetches public, CORS-enabled telemetry from NOAA Space Weather Prediction Center (GOES-18 satellites):
- **GOES-18 Integral Protons ($\ge 10\text{ MeV}$)**: Drives radiation dose calculations and camera sensor noise.
- **Planetary Kp Index**: When geomagnetic activity reaches $\text{Kp} \ge 4$, realistic green and cyan polar aurora ribbons undulate across the night sky.
- **Real-Time Solar Wind Speed ($\text{km/s}$)**: When solar wind exceeds $420\text{ km/s}$, electrostatic dust levitation particles float above crater ridges (replicating Apollo 17's real lunar horizon glow observations).
- **Primary X-Ray Flares**: Measures solar flare strength (Classes A, B, C, M, X) affecting radio communications.
- **Real-time NOAA Bulletins & Alerts**: Reads live space weather warnings directly into the nightly radio broadcast.

### 4. Zero-Login Cloud Save System
- **Outpost Call Sign**: Every mission is automatically assigned a memorable mission call sign (e.g. `ARTEMIS-409`, `ORION-812`).
- **Dual Persistence**:
  - Automatically saves to `localStorage` at the start of every day (100% offline-ready).
  - Automatically syncs in the background to `save.php` on PHP web hosting.
- **No Passwords or Accounts**: A student can start a game in a school classroom, write down their Call Sign, and click **LOAD CALL SIGN** on their home tablet or phone to immediately resume their outpost!

---

## 📚 STEM & Educational Case Files
Includes historical mission debriefs from **NASA**, **ISRO**, and **CNSA**:
- **Apollo 17 (1972)**: Lunar dust adhesion and airlock decontamination.
- **Artemis I (2022)**: Radiation phantom dosimetry (Helga and Zohar).
- **August 1972 Solar Storm**: SPE shelter timing between Apollo 16 and 17.
- **Opportunity Rover (2018)**: Planetary dust storm battery starvation.
- **Chandrayaan-3 (2023)**: Surviving the -170°C lunar polar night.
- **Chang'e-4 (2019)**: Radioisotope thermal heating units on the lunar far side.
- **ISS Soyuz Leak (2018)**: Acoustic ultrasound micro-puncture detection.
- **Apollo 13 (1970)**: Power budgeting and lithium hydroxide scrubber adaptation.
- **MOXIE (2021+)**: Mars atmospheric $CO_2$ to $O_2$ conversion.
