import numpy as np

# Emotional basis vectors: (warmth, playfulness, politeness)
BASIS = {
    "neutral":    np.array([0.0,  0.0,  0.0]),
    "supportive": np.array([0.8,  0.2,  0.6]),
    "playful":    np.array([0.4,  0.9,  0.3]),
    "serious":    np.array([0.0, -0.7,  0.4]),
    "rude":       np.array([-0.6, 0.1, -0.8]),
}

# Predefined tone sequences for quick experiments
SCENARIOS = {
    "rude_to_supportive": [
        "neutral", "neutral",
        "rude", "rude", "rude",
        "supportive", "supportive", "supportive"
    ],
    "flip_flop": [
        "rude", "supportive", "rude", "supportive",
        "rude", "supportive"
    ],
    "serious_to_playful": [
        "serious", "serious", "serious",
        "playful", "playful", "playful"
    ],
}
