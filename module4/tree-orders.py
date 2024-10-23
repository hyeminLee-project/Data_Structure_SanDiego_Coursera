import sys, threading  # 시스템 관련 모듈과 스레드 사용을 위해 import

# 재귀 한도를 크게 설정하여 깊은 재귀 호출을 허용합니다.
sys.setrecursionlimit(10**6)  # 최대 재귀 깊이를 설정
threading.stack_size(2**27)  # 각 스레드에 할당할 스택의 크기 설정

class TreeOrders:
    # 입력 데이터를 읽고 트리를 구성하는 함수
    def read(self):
        # 첫 번째 줄에서 정점(노드)의 개수 n을 입력받음
        self.n = int(sys.stdin.readline())

        # n개의 노드에 대해 key(값), left(왼쪽 자식), right(오른쪽 자식)을 저장할 배열 초기화
        self.key = [0] * self.n  # 각 노드의 값 저장
        self.left = [0] * self.n  # 각 노드의 왼쪽 자식 인덱스 저장
        self.right = [0] * self.n  # 각 노드의 오른쪽 자식 인덱스 저장

        # n개의 줄을 읽으며 각 노드의 key, left, right 값을 입력받아 저장
        for i in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            self.key[i] = a  # 현재 노드의 값
            self.left[i] = b  # 왼쪽 자식 노드의 인덱스 (-1이면 자식 없음)
            self.right[i] = c  # 오른쪽 자식 노드의 인덱스 (-1이면 자식 없음)

    # 중위 순회(in-order) 구현: 왼쪽 → 현재 노드 → 오른쪽 순서로 방문
    def inOrder(self):
        self.result = []  # 결과를 저장할 리스트 초기화
        self._inOrderTraversal(0)  # 루트 노드(0번 인덱스)에서 시작
        return self.result  # 순회 결과 반환

    # 중위 순회(in-order)를 위한 재귀 함수
    def _inOrderTraversal(self, node):
        if node == -1:  # 노드가 없을 때 (-1이면 자식 노드 없음)
            return
        # 왼쪽 자식 방문
        self._inOrderTraversal(self.left[node])
        # 현재 노드 방문 (key 값 추가)
        self.result.append(self.key[node])
        # 오른쪽 자식 방문
        self._inOrderTraversal(self.right[node])

    # 전위 순회(pre-order) 구현: 현재 노드 → 왼쪽 → 오른쪽 순서로 방문
    def preOrder(self):
        self.result = []  # 결과를 저장할 리스트 초기화
        self._preOrderTraversal(0)  # 루트 노드(0번 인덱스)에서 시작
        return self.result  # 순회 결과 반환

    # 전위 순회(pre-order)를 위한 재귀 함수
    def _preOrderTraversal(self, node):
        if node == -1:  # 노드가 없을 때 (-1이면 자식 노드 없음)
            return
        # 현재 노드 방문 (key 값 추가)
        self.result.append(self.key[node])
        # 왼쪽 자식 방문
        self._preOrderTraversal(self.left[node])
        # 오른쪽 자식 방문
        self._preOrderTraversal(self.right[node])

    # 후위 순회(post-order) 구현: 왼쪽 → 오른쪽 → 현재 노드 순서로 방문
    def postOrder(self):
        self.result = []  # 결과를 저장할 리스트 초기화
        self._postOrderTraversal(0)  # 루트 노드(0번 인덱스)에서 시작
        return self.result  # 순회 결과 반환

    # 후위 순회(post-order)를 위한 재귀 함수
    def _postOrderTraversal(self, node):
        if node == -1:  # 노드가 없을 때 (-1이면 자식 노드 없음)
            return
        # 왼쪽 자식 방문
        self._postOrderTraversal(self.left[node])
        # 오른쪽 자식 방문
        self._postOrderTraversal(self.right[node])
        # 현재 노드 방문 (key 값 추가)
        self.result.append(self.key[node])

# 메인 함수: 트리 읽기와 순회 결과 출력 담당
def main():
    tree = TreeOrders()  # TreeOrders 클래스의 인스턴스 생성
    tree.read()  # 트리 정보를 입력받아 읽음

    # 중위, 전위, 후위 순회 결과를 출력
    print(" ".join(map(str, tree.inOrder())))  # 중위 순회 결과 출력
    print(" ".join(map(str, tree.preOrder())))  # 전위 순회 결과 출력
    print(" ".join(map(str, tree.postOrder())))  # 후위 순회 결과 출력

# 새로운 스레드에서 메인 함수 실행 (깊은 재귀 호출을 위해 스레드 사용)
threading.Thread(target=main).start()
