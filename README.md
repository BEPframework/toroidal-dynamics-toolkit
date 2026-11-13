# Toroidal Dynamics Toolkit (TDT) v1.0

**Benchmark runner for real tokamak data (currently single-shot; multi-shot and risk correlation planned)**

Modular Python toolkit for dynamic toroidal modulation in frequency-domain signal processing. Extends the [Ψ_universe Attractor Library v2.0](https://github.com/BEPframework/psi-universe-attractor) for real experimental tokamak data. The current benchmark runs one EAST discharge (#41195); multi-shot benchmarking and risk correlation analysis are planned, not yet implemented.

---

### Features

- Dynamic toroidal modulation in frequency-domain signal processing
- Benchmark runner for real tokamak data (single shot today; multi-shot planned)
- Risk correlation analysis across discharge parameters (planned)
- Extends the Ψ_universe attractor filter for experimental testing

### Quick Start

```bash
# Run the toolkit
python toroidal_dynamics_toolkit.py

# Run the benchmark (single shot; requires your own east_ip.txt)
python benchmark_multi_shot.py
```

Dependencies: Python 3.x, NumPy, SciPy.

### Related Repositories

- [psi-universe-attractor](https://github.com/BEPframework/psi-universe-attractor) — Ψ_universe attractor filter (exploratory; tested on one EAST discharge)
- [tasd-core](https://github.com/BEPframework/tasd-core) — TASD Core Framework (capstone documentation)
- [tasd-framework](https://github.com/BEPframework/tasd-framework) — TASD Unified Framework (open-source release)
- [q216d-tokamak-simulation](https://github.com/BEPframework/q216d-tokamak-simulation) — Interactive 3D plasma visualization with TASD-enhanced control

### Copyright

Copyright © 2026 Nicolas B. Quiroz, MD. All rights reserved for the original work.

### License

See the [LICENSE](LICENSE) file for details.

### Citation

If you use this toolkit, please cite:

> **Quiroz, N. B. (2026)**. *Toroidal Dynamics Toolkit v1.0*. Zenodo. https://doi.org/10.5281/zenodo.18926038

### Keywords

tokamak · fusion energy · plasma physics · toroidal plasma · magnetic confinement · frequency-domain signal processing
