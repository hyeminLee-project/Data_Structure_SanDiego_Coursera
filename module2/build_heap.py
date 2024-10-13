# python3

def min_heapify(data, n, i, swaps):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # compare with left child
    if left < n and data[left] < data[smallest]:
        smallest = left
    #compare with the right child
    if right < n and data[right] < data[smallest]:
        smallest = right
    #if the smallest is not the root
    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        swaps.append((i, smallest))
        #Recursively heapify the affected subtree
        min_heapify(data, n, smallest, swaps)


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    n = len(data)

    #Start from the last non-leaf node and hapify each node
    for i in range(n // 2 -1, -1,-1):
        min_heapify(data, n, i, swaps)

    return swaps

    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
