from collections import deque

def max_sliding_window(sequence, m):
    maximums = []
    d = deque()  # Deque to store indices of elements in the current window

    for i in range(len(sequence)):
        # Remove elements not within the sliding window
        if d and d[0] < i - m + 1:
            d.popleft()
        
        # Remove elements from the back while the current element is greater
        while d and sequence[d[-1]] < sequence[i]:
            d.pop()
        
        # Add current element index to the deque
        d.append(i)

        # If we've processed at least m elements, append the max for the current window
        if i >= m - 1:
            maximums.append(sequence[d[0]])  # The front of the deque is the max for the current window

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
