

import sys, threading

# 최대 재귀 깊이와 스택 크기 설정 
sys.setrecursionlimit(10**7)
threading.stack_size(2**25)

def IsBinarySearchTree(tree):
    if not tree:  # 트리가 비어있는 경우는 유효한 BST로 간주
        return True

    # 스택을 사용해 반복적으로 트리를 탐색합니다.
    stack = [(0, float('-inf'), float('inf'))]  # (노드 인덱스, 최소값, 최대값)

    while stack:
        node, min_key, max_key = stack.pop()  # 스택에서 노드 정보 꺼내기
        key, left, right = tree[node]

        # 현재 노드의 키가 범위를 벗어나면 BST가 아님
        if not (min_key < key < max_key):
            return False

        # 오른쪽 자식이 있는 경우 스택에 추가 (현재 키가 최소값이 됨)
        if right != -1:
            stack.append((right, key, max_key))

        # 왼쪽 자식이 있는 경우 스택에 추가 (현재 키가 최대값이 됨)
        if left != -1:
            stack.append((left, min_key, key))

    return True  # 모든 노드를 검사하고 조건을 만족하면 BST

def main():
    nodes = int(sys.stdin.readline().strip())  # 노드 수 입력받기

    tree = []  # 트리 정보를 저장할 리스트
    for _ in range(nodes):
        # 각 노드의 키, 왼쪽 자식, 오른쪽 자식을 입력받아 저장
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    # BST 여부를 검사하고 결과 출력
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

# 새로운 스레드에서 메인 함수 실행
threading.Thread(target=main).start()
