import numpy as np
from utils import PriorityQueue
from pympler import asizeof

def print_info(obj):
    s = asizeof.asizeof(obj)
    print(s)

n = 10_000
obj = PriorityQueue(n, dtype=np.uint32)
print_info(obj)
print(32 * n // 8)

obj.push(8,1)
print_info(obj)
print(obj.payloads)
print(obj.priority)

obj.push(16,2)
print_info(obj)
print(obj.payloads)
print(obj.priority)

obj.push(32, 1)
print_info(obj)
print(obj.payloads)
print(obj.priority)
print(obj.pop())
print(obj.pop())

print_info(obj)