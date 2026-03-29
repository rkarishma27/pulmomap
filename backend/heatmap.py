import numpy as np
from db import collection

def generate_heatmap(patient_id):
    samples = list(collection.find({"patient_id": patient_id}))

    grid = np.zeros((2, 2))
    mapping = {"top_left": (0,0), "top_right":(0,1), "bottom_left":(1,0), "bottom_right":(1,1)}

    for s in samples:
        x, y = mapping.get(s.get("sensor","top_left"), (0,0))
        if s.get("prediction") and "confidence" in s["prediction"]:
            grid[x][y] = s["prediction"]["confidence"]
        else:
            grid[x][y] = 0.0
    return grid.tolist()