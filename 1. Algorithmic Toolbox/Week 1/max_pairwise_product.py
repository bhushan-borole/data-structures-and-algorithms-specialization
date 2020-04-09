# python3


def max_pairwise_product(numbers):
    n1 = max(numbers)
    numbers.remove(n1)
    n2 = max(numbers)
    return n1 * n2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
