import sys
from collections import defaultdict, namedtuple

Answer = namedtuple('answer_type', 'i j length')

class RollingHash:
    def __init__(self, s, base, prime):
        """문자열 s의 접두사 해시와 base^i 값을 미리 계산합니다."""
        self.s = s
        self.base = base
        self.prime = prime
        self.n = len(s)
        self.prefix_hash = [0] * (self.n + 1)  # 접두사 해시 값
        self.base_powers = [1] * (self.n + 1)  # base^i 값

        for i in range(1, self.n + 1):
            self.prefix_hash[i] = (self.prefix_hash[i - 1] * base + ord(s[i - 1])) % prime
            self.base_powers[i] = (self.base_powers[i - 1] * base) % prime

    def get_hash(self, start, length):
        """시작 인덱스와 길이에 대한 해시 값 반환."""
        end = start + length
        hash_value = (self.prefix_hash[end] - self.prefix_hash[start] * self.base_powers[length]) % self.prime
        return hash_value if hash_value >= 0 else hash_value + self.prime

def longest_common_substring(s, t):
    base = 263
    prime = 10**9 + 7

    hash_s = RollingHash(s, base, prime)
    hash_t = RollingHash(t, base, prime)

    def check(length):
        """길이가 length인 공통 서브스트링이 있는지 확인합니다."""
        seen_hashes = defaultdict(list)
        # s에서 길이 length인 모든 서브스트링의 해시를 저장
        for i in range(len(s) - length + 1):
            h = hash_s.get_hash(i, length)
            seen_hashes[h].append(i)  # 해당 해시의 시작 인덱스 저장

        # t에서 길이 length인 모든 서브스트링의 해시를 확인
        for j in range(len(t) - length + 1):
            h = hash_t.get_hash(j, length)
            if h in seen_hashes:
                # 충돌 가능성을 확인하기 위해 직접 서브스트링 비교
                for i in seen_hashes[h]:
                    if s[i:i + length] == t[j:j + length]:
                        return i, j  # 공통 서브스트링의 인덱스 반환
        return None

    # 이진 탐색으로 최대 공통 서브스트링 길이 찾기
    low, high = 0, min(len(s), len(t))
    best = Answer(0, 0, 0)

    while low <= high:
        mid = (low + high) // 2
        result = check(mid)
        if result:
            best = Answer(result[0], result[1], mid)
            low = mid + 1  # 더 긴 공통 서브스트링을 찾기 위해 탐색 범위 확장
        else:
            high = mid - 1  # 더 짧은 공통 서브스트링을 찾기 위해 탐색 범위 축소

    return best

# 입력 처리 및 실행
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().strip().splitlines()
    for line in data:
        s, t = line.split()
        ans = longest_common_substring(s, t)
        print(ans.i, ans.j, ans.length)
