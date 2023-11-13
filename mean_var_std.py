# type: ignore

import numpy as np

def calculate(list):
  try:
    matrix = np.array(list).reshape(3, 3)
  except ValueError:
    raise ValueError("List must contain nine numbers.")

  calculations = {
    'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(list)],
    'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(list)],
    'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(list)],
    'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(list)],
    'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(list)],
    'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(list)]
  }
  
  return calculations