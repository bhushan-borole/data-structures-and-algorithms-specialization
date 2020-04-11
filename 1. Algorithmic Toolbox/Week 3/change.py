# Uses python3
import sys

def get_change(m):
    n_10 = int(m / 10)
    n_5 = int((m % 10) / 5)
    n_1 = (m % 10) % 5
    return n_10 + n_5 + n_1

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
