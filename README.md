# Night Watch: Outpost Zero (NASA Space Apps 2026)

## Run it
It is a plain website (no build step). On Windows, in this folder:
    python -m http.server 8080      then open http://localhost:8080
(or `npx serve`). Do not double-click index.html: offline mode and the snapshot need http.

## Put it online (free)
Upload this folder to GitHub Pages, Netlify Drop or Cloudflare Pages. Keep the folder structure.

## Controls
PC: arrows/WASD move, Z = interact, X = back / menu, M = mute. No on-screen pad on PC.
Phone/tablet: the D-pad and Z (INTERACT) / X (BACK) buttons appear automatically.

## Saving
Autosaves in the browser (localStorage) at the start of every day. Menu (X) > SAVE GAME to save now,
EXPORT SAVE downloads nightwatch-save.json, and IMPORT SAVE on the title screen loads it on another device.
Private/incognito mode may block saving.

## Live data
Real space weather from NOAA SWPC (GOES protons, Kp, X-rays, solar wind), no key needed, read live by the browser.
Badge rules: LIVE = under 2 hours old, ARCHIVE = saved earlier (last good reading or data/spaceweather.json),
GAME VALUE = nothing available. Menu > SPACE WEATHER, press Z to try SIMULATED storms (labelled not real).
To keep the snapshot fresh: `node scripts/fetch-snapshots.mjs` or enable the included GitHub Action.
The bundled snapshot is a real reading (2026-11-14 22:40 UTC) taken from the team's own check.

## Still to verify before submitting
Case File wording (NASA/ISRO/CNSA), Hindi/Marathi (not included yet), NASA DONKI/OSDR (not connected yet).
Font: Press Start 2P (SIL OFL, see fonts/).
