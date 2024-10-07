# python3

import sys
import threading
def compute_height(n, parents):
    # Create an adjacency list for the tree
    tree = [[] for _ in range(n)]
    root = None

    # Build the tree
    for child in range(n):
        parent = parents[child]
        if parent == -1:
            root = child  # This is the root node
        else:
            tree[parent].append(child)  # Add child to its parent's list

    # Function to calculate height using iterative DFS
    def iterative_dfs(start_node):
        stack = [(start_node, 1)]  # (node, current_height)
        max_height = 0
        
        while stack:
            node, height = stack.pop()
            max_height = max(max_height, height)
            for child in tree[node]:
                stack.append((child, height + 1))
        
        return max_height

    # Calculate the height starting from the root
    return iterative_dfs(root)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

if __name__ == "__main__":
    main()
