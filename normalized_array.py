import numpy as np

def normalized_array(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)
    if max_val == min_val:
        return np.zeros_like(arr, dtype=float)
    x_norm = (arr - min_val) / (max_val - min_val)
    return x_norm
