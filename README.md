# ⚡ AeroSilence-ANC

> Real-Time Active Noise Cancellation System for Open Windows  
> An open-source hardware and software system designed to mitigate low-to-mid-frequency ambient noise (traffic, urban rumble, construction) through open window gaps using Filtered-X LMS (FXLMS) adaptive filtering.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-green.svg)
![Hardware: RPi_4_/_ESP32--S3](https://img.shields.io/badge/Hardware-RPi__4_%2F_ESP32--S3-orange.svg)

---

## 🎯 Project Overview

AeroSilence-ANC allows maintaining continuous natural ventilation while actively attenuating incoming external acoustic noise by 18–25 dB.

Unlike passive acoustic barriers, the system operates on the principle of active destructive wave interference. External acoustic waves are detected in real time, and anti-phase sound waves are emitted directly along the window aperture.

---

## 🔬 System Architecture & Signal Flow

The core attenuator utilizes a Filtered-X Least Mean Square (FXLMS) algorithm with real-time secondary path modeling $S(z)$:

`text
[ Ambient Noise x(n) ] ──────► ( External Reference I2S Mic )
                                           │
                                           ▼
                             [ DSP / AeroSilence Engine ]
                                           │
                                           ▼
[ Anti-Noise Wave y(n) ] ───► ( Acoustic Transducers / Exciters ) ◄─── Destructive Interference
                                           │
                                           ▼
                             ( Internal Error I2S Mic e(n) ) ──► ( Weight Update W )
