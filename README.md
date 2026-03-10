# Toroidal Dynamics Toolkit (TDT) v1.0

**Multi-Shot Real Tokamak Benchmark Suite with Risk Correlation**

Extends **Psi Universe Attractor Library v2.0** for real experimental data.

---

## Features

- Loads multiple real EAST discharges (or any CSV with `time_s + ip_ma + disruption_risk`)
- Runs Psi v2 with realistic plasma effects (noise + wall drift + actuator delay)
- Computes stability scores and disruption-risk correlation
- Generates summary tables and CSV output

---

## Quick Start

```python
from toroidal_dynamics_toolkit import run_multi_shot_benchmark

summary = run_multi_shot_benchmark("data_folder", [41195, 41196])
```

---

## Citation (please use this)

Quiroz, N. B. (2026).  
*Toroidal Dynamics Toolkit (TDT) v1.0 — Multi-Shot Real Tokamak Benchmark Suite with Risk Correlation* [Software].  
Zenodo. https://doi.org/10.5281/zenodo.18926038

---

## License

Copyright (C) 2026 Nicolas B. Quiroz, MD  

Licensed under the **Apache License, Version 2.0**  
(see the `LICENSE` file).

---

## Preprint Note

This is an open-source research artifact. Full technical preprint with derivations and additional shots will be linked in future versions. Feedback and real-shot collaborations welcome.
