'''
# Test cases
print(compare_versions("4", "7"))
print(compare_versions("7", "4"))
print(compare_versions("7.1", "7.1"))
print(compare_versions("3.2", "7"))
print(compare_versions("3.3", "3.2"))
print(compare_versions("4", "4.0"))
'''

from json import dumps, loads
from typing import List


def compare_versions(versiona: str, versionb: str) -> int:
    va = list(map(int, versiona.split('.')))
    vb = list(map(int, versionb.split('.')))
    
    max_len  = max(len(va), len(vb))
    va += [0] * (max_len - len(va))
    vb += [0] * (max_len - len(vb))
    
    for a, b in zip(va, vb):
        print(a)
        print(b)
        if a < b:
            return -1
        elif a > b:
            return 1
    
    return 0
