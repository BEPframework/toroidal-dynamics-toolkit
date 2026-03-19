# Contributing to Toroidal Dynamics Toolkit

Thanks for your interest in contributing! TDT is a modular Python toolkit for dynamic toroidal modulation in frequency-domain signal processing, with a multi-shot real tokamak benchmark suite.

## Ways to Contribute

- **Bug reports** — open an issue describing the problem, your Python version, and steps to reproduce.
- **Feature requests** — open an issue with a clear description of the proposed feature and its relevance to toroidal dynamics or signal processing.
- **Code contributions** — fork the repo, make your changes, and submit a pull request.
- **Benchmark data** — if you have access to additional tokamak shot data and would like to contribute benchmarks, open an issue or discussion.

## Guidelines

1. **Python code** — keep dependencies minimal. NumPy and SciPy are acceptable; heavy frameworks should be justified.
2. **Reproducibility** — all benchmarks should clearly document their data sources and be reproducible with the provided scripts.
3. **Test before submitting** — verify your changes run cleanly with both `toroidal_dynamics_toolkit.py` and `benchmark_multi_shot.py`.
4. **Respect the framework** — TDT extends the Ψ_universe Attractor Library for real experimental data. Keep that relationship clear in any documentation.

## Pull Request Process

1. Fork and create a feature branch (`git checkout -b feature/my-feature`).
2. Make your changes.
3. Test thoroughly.
4. Submit a PR with a clear description of what changed and why.

## License

By contributing, you agree that your contributions will be licensed under the existing license terms.

## Contact

For questions, reach out to **Nicolas B. Quiroz, MD** via [GitHub](https://github.com/BEPframework).
