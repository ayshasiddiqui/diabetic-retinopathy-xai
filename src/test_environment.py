import torch
import cv2
import numpy as np
import pandas as pd

print("=" * 50)
print("DIABETIC RETINOPATHY PROJECT")
print("=" * 50)

print("Python environment: OK")
print("PyTorch:", torch.__version__)
print("OpenCV:", cv2.__version__)
print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("CUDA Available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
else:
    print("Running on CPU")

print("=" * 50)
print("Environment setup successful!")
print("=" * 50)