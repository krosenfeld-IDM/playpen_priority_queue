import numpy as np
from pympler import asizeof

obj = np.arange(10_000, dtype=np.int32)
s = asizeof.asizeof(obj)
print(s)
print(len(obj) * 32 // 8)
