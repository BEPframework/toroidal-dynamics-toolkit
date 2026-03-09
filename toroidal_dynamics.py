```python
import numpy as np
from scipy.integrate import quad

class ToroidalModulator:
    def __init__(self, variant="REQ-T"):
        self.variant = variant
        self.params = {
            'alpha': 1.0, 'sigma': 1.0, 'f0': 0.0,
            'lambda_tor': 1.0, 'r_tor': 1.0,
            'theta': np.pi/4, 'phi': 0.0
        }

    def kernel(self, f, t=0.0):
        phase = 2*np.pi*f*t + self.params['alpha']*f*f
        gaussian = np.exp(-2*self.params['sigma']**2*(f - self.params['f0'])**2)
        
        if self.variant in ["REQ-T", "TEQ-T"]:
            mod = np.sin(self.params['lambda_tor'] * 2*np.pi * self.params['r_tor'])
        elif self.variant in ["REQ-U", "TEQ-U"]:
            mod = np.tan(self.params['theta'])
        elif self.variant in ["REQ-CU", "TEQ-CU"]:
            mod = np.cos(self.params['lambda_tor']*2*np.pi*self.params['r_tor'] + self.params['phi'])
        else:
            mod = np.sin(self.params['lambda_tor'] * 2*np.pi * self.params['r_tor'])
        
        return np.real(np.exp(1j*phase) * gaussian * mod)

    def evolve(self, t=0.0):
        self.t = t
        result, _ = quad(self.kernel, -100, 100, args=(t,))
        return result
