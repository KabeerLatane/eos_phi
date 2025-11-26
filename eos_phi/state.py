import numpy as np

class EmotionState:
    """
    EOS-φ emotional state object.

    Maintains:
    - E_t : current emotional state vector
    - alpha : inertia parameter (0.0 = fast changes, 0.99 = very slow changes)
    """

    def __init__(self, dim=3, alpha=0.8):
        self.dim = dim
        self.alpha = alpha
        self.E_t = np.zeros(dim)

    def update(self, S_i):
        """
        Update rule:
            E_{t+1} = alpha * E_t + (1 - alpha) * S_i
        """
        self.E_t = self.alpha * self.E_t + (1 - self.alpha) * S_i
        return self.E_t

    def get(self):
        """Return the current emotional state vector."""
        return self.E_t
