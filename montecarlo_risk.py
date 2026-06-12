import numpy as np

def calculate_risk():
    # Simulación de Montecarlo
    trials = 1000
    risks = np.random.normal(0, 1, trials)
    return np.mean(risks)
