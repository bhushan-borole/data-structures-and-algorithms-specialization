# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops = [0] + stops + [distance]
    n_ref = 0
    cur_ref = 0
    if distance - stops[-2] > tank:
        return -1
    while cur_ref < len(stops)-2:
        last_ref = cur_ref
        while cur_ref <= len(stops)-2 and \
                stops[cur_ref+1] - stops[last_ref] <= tank:
            cur_ref += 1
        if cur_ref == last_ref:
            return -1
        if cur_ref <= len(stops)-2:
            n_ref += 1
    return n_ref


if __name__ == '__main__':
    # d, m, _, *stops = map(int, sys.stdin.read().split())
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    print(compute_min_refills(d, m, stops))
