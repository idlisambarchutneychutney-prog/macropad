## Macropad

A custom 9-key macropad powered by the **Seeed XIAO RP2040** microcontroller running **KMK Firmware** on CircuitPython. Featuring a 3x3 key matrix, an EC11 rotary encoder for media control, a 0.91" OLED status display, and per-key SK6812MINI-E RGB lighting.

---

## Features

- **Brain:** Seeed XIAO RP2040 Microcontroller
- **Key Matrix:** 9 MX switches configured in a 3x3 matrix with 1N4148 diodes (`COL2ROW`).
- **Rotary Encoder:** EC11 encoder mapped to Volume Down, Volume Up, and Mute (push button).
- **Display:** 0.91" I2C OLED display (128x32) running custom status text.
- **Lighting:** 9x SK6812MINI-E addressable per-key RGB LEDs.
- **Firmware:** KMK Firmware (CircuitPython) with built-in productivity macros and application launchers.

---

## Keymap & Macro Layout

| Key Position | Action / Macro | Description |
| :--- | :--- | :--- |
| **Top Left** | `Ctrl + C` | Copy |
| **Top Middle** | `Ctrl + V` | Paste |
| **Top Right** | `Ctrl + Z` | Undo |
| **Mid Left** | Macro | Opens GitHub in browser via Windows Run |
| **Mid Middle** | Macro | Launches VS Code via Windows Run |
| **Mid Right** | Macro | Launches Google Chrome via Windows Run |
| **Bot Left** | Macro | System Shutdown (`shutdown /s /t 0`) |
| **Bot Middle** | Macro | System Restart (`shutdown /r /t 0`) |
| **Bot Right** | `Win + L` | Lock Windows PC |

### Encoder Controls
- **Rotate CCW:** Volume Down (`KC.VOLD`)
- **Rotate CW:** Volume Up (`KC.VOLU`)
- **Press Button:** Mute Audio (`KC.MUTE`)

---

## Hardware & Bill of Materials (BOM)

| Component | Quantity | Description |
| :--- | :--- | :--- |
| Microcontroller | 1 | Seeed Studio XIAO RP2040 |
| Switches | 9 | MX-compatible mechanical switches |
| Diodes | 9 | 1N4148 switching diodes |
| Rotary Encoder | 1 | EC11 Rotary Encoder with push switch |
| Display | 1 | 0.91" I2C OLED Display Module (128x32) |
| RGB LEDs | 9 | SK6812MINI-E surface-mount LEDs |
| Custom PCB | 1 | Designed in KiCad |
| Enclosure | 1 | 3D-printed enclosure designed in Onshape |

---

## Pinout & Schematic Mapping

| Peripheral | Component Pin | XIAO RP2040 Pin |
| :--- | :--- | :--- |
| **Matrix Columns** | Col 0, Col 1, Col 2 | `D5`, `D3`, `D6` |
| **Matrix Rows** | Row 0, Row 1, Row 2 | `D4`, `D1`, `D0` |
| **Encoder** | Pin A, Pin B, Switch | `D8`, `D9`, `D7` |
| **OLED Display** | SCL, SDA | `D2`, `D10` |
| **RGB LED Chain** | Data In (DIN) | `D7` |

---

## Hardware Gallery

### Schematic Diagram
<img width="982" height="543" alt="Screenshot 2026-08-30 222048" src="https://github.com/user-attachments/assets/6eb875eb-b690-435a-ab2d-be8cda6da218" />

### PCB Design
<img width="1409" height="1366" alt="Screenshot 2026-08-23 035549" src="https://github.com/user-attachments/assets/4ff94f1c-50f5-4701-9079-569b71024b6d" />

### 3D Enclosure Render
<img width="1427" height="916" alt="Screenshot 2026-08-23 030317" src="https://github.com/user-attachments/assets/f5d36838-42c4-4892-98b5-c7f2f48ee19f" />
