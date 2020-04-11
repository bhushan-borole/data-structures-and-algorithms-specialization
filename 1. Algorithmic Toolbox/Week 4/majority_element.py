# Uses python3
import sys
from collections import Counter

def get_majority_element(a):
    counts = dict(Counter(a))
    found = False
    for v in counts.values():
        if v > len(a)/2:
            found = True
            break
    return found

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if get_majority_element(a):
        print(1)
    else:
        print(0)
