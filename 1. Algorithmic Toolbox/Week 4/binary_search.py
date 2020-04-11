# Uses python3
import sys

def binary_search(a, left, right, x):
    # left, right = 0, len(a) - 1
    
    if right >= left:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif x > a[mid]:
            return binary_search(a, mid+1, right, x)
        else:
            return binary_search(a, left, mid-1, x)
    else:
        return -1



if __name__ == '__main__':
    n, *a = list(map(int, input().split()))
    k, *b = list(map(int, input().split()))

    for k in b:
        print(binary_search(a, 0, len(a)-1, k), end=' ')
