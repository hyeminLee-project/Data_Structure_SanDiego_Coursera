import sys
import random

class Solver:
    _m1 = 10**9 + 7  # 첫 번째 소수 모듈러
    _m2 = 10**9 + 9  # 두 번째 소수 모듈러
    _x = random.randint(1, 10**9)  # 랜덤한 x 값 선택

    def __init__(self, s):
        self.s = s
        self.n = len(s)
        # 접두사 해시와 제곱값을 미리 계산합니다.
        self.h1, self.h2 = [0] * (self.n + 1), [0] * (self.n + 1)
        self.x_powers1, self.x_powers2 = [1] * (self.n + 1), [1] * (self.n + 1)
        self._precompute_hashes()

    def _precompute_hashes(self):
        """모든 접두사에 대한 해시와 x의 제곱값을 미리 계산합니다."""
        for i in range(1, self.n + 1):
            self.h1[i] = (self._x * self.h1[i - 1] + ord(self.s[i - 1])) % self._m1
            self.h2[i] = (self._x * self.h2[i - 1] + ord(self.s[i - 1])) % self._m2
            self.x_powers1[i] = (self.x_powers1[i - 1] * self._x) % self._m1
            self.x_powers2[i] = (self.x_powers2[i - 1] * self._x) % self._m2

    def _get_hash(self, h, x_powers, a, l, mod):
        """서브스트링의 해시 값을 계산합니다."""
        hash_value = (h[a + l] - h[a] * x_powers[l] % mod) % mod
        return hash_value if hash_value >= 0 else hash_value + mod

    def ask(self, a, b, l):
        """두 서브스트링이 동일한지 확인합니다."""
        hash1_a = self._get_hash(self.h1, self.x_powers1, a, l, self._m1)
        hash1_b = self._get_hash(self.h1, self.x_powers1, b, l, self._m1)
        hash2_a = self._get_hash(self.h2, self.x_powers2, a, l, self._m2)
        hash2_b = self._get_hash(self.h2, self.x_powers2, b, l, self._m2)

        return hash1_a == hash1_b and hash2_a == hash2_b

# 입력 처리 및 쿼리 실행
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    s = data[0]
    q = int(data[1])
    queries = data[2:]

    solver = Solver(s)  # Solver 인스턴스 생성

    result = []
    for i in range(q):
        a, b, l = map(int, queries[i * 3:(i + 1) * 3])
        result.append("Yes" if solver.ask(a, b, l) else "No")

    # 결과 출력
    sys.stdout.write("\n".join(result) + "\n")
# #
# import sys

# class Solver:
#     _base = 263  # 진수(base) 값
#     _prime = 1000000007  # 큰 소수 (충돌 최소화)

#     def __init__(self, s):
#         self.s = s
#         self.n = len(s)
#         self.prefix_hash = [0] * (self.n + 1)  # 접두사 해시 배열
#         self.base_powers = [1] * (self.n + 1)  # base^i 값을 미리 계산
#         self._precompute_hashes()  # 해시와 제곱 값 미리 계산

#     def _precompute_hashes(self):
#         """문자열의 접두사 해시와 base^i 값을 미리 계산합니다."""
#         for i in range(1, self.n + 1):
#             self.prefix_hash[i] = (self.prefix_hash[i - 1] * self._base + ord(self.s[i - 1])) % self._prime
#             self.base_powers[i] = (self.base_powers[i - 1] * self._base) % self._prime

#     def _get_hash(self, start, length):
#         """시작 인덱스와 길이에 대한 서브스트링의 해시 값을 구합니다."""
#         hash_value = (self.prefix_hash[start + length] - self.prefix_hash[start] * self.base_powers[length]) % self._prime
#         return hash_value if hash_value >= 0 else hash_value + self._prime

#     def ask(self, a, b, l):
#         """두 서브스트링이 동일한지 해시 값을 비교하여 판별합니다."""
#         return self._get_hash(a, l) == self._get_hash(b, l)

# # 입력 처리 및 쿼리 실행
# if __name__ == "__main__":
#     input = sys.stdin.read
#     data = input().split()
#     s = data[0]
#     q = int(data[1])
#     queries = data[2:]

#     solver = Solver(s)  # Solver 인스턴스 생성

#     result = []
#     for i in range(q):
#         a, b, l = map(int, queries[i * 3:(i + 1) * 3])
#         result.append("Yes" if solver.ask(a, b, l) else "No")

#     # 결과 출력
#     sys.stdout.write("\n".join(result) + "\n")
