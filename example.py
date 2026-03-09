from toroidal_dynamics import ToroidalModulator

mod = ToroidalModulator(variant="REQ-T")
print("REQ-T at t=0.5:", mod.evolve(0.5))

mod2 = ToroidalModulator(variant="REQ-OMEGA")
print("Omega example:", mod2.evolve(1.0))
