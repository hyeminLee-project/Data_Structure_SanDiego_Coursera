# import sys

# def solve(k, text, pattern):
#     """텍스트 내에서 최대 k개의 불일치로 패턴이 나타나는 위치를 반환합니다."""
#     n, m = len(text), len(pattern)
#     result = []

#     # 가능한 모든 시작 위치에서 비교 수행
#     for i in range(n - m + 1):
#         mismatches = 0  # 불일치 개수 초기화
#         for j in range(m):
#             if text[i + j] != pattern[j]:  # 문자 비교
#                 mismatches += 1
#                 if mismatches > k:  # 불일치가 허용 범위를 초과하면 중단
#                     break
#         if mismatches <= k:  # 불일치가 허용 범위 내인 경우
#             result.append(i)

#     return result

# # 입력 처리 및 실행
# if __name__ == "__main__":
#     input = sys.stdin.read  # 전체 입력 읽기
#     data = input().strip().splitlines()

#     for line in data:
#         k, t, p = line.split()
#         k = int(k)
#         ans = solve(k, t, p)  # 매칭 수행
#         print(len(ans), *ans)  # 결과 출력
# import sys

# def rolling_hash(s, base, prime):
#     """주어진 문자열 s의 해시값을 계산합니다."""
#     hash_value = 0
#     for char in s:
#         hash_value = (hash_value * base + ord(char)) % prime
#     return hash_value

# def update_hash(prev_hash, old_char, new_char, power, base, prime):
#     """슬라이딩 윈도우에서 해시값을 업데이트합니다."""
#     new_hash = (prev_hash - ord(old_char) * power) * base + ord(new_char)
#     new_hash %= prime
#     return new_hash

# def mismatches_within_limit(t, p, start, k):
#     """텍스트 t와 패턴 p를 비교하여 최대 k개의 불일치를 확인합니다."""
#     mismatches = 0
#     for j in range(len(p)):
#         if t[start + j] != p[j]:
#             mismatches += 1
#             if mismatches > k:
#                 return False
#     return True

# def pattern_matching_with_mismatches(k, text, pattern):
#     """텍스트 내에서 최대 k개의 불일치로 패턴이 나타나는 위치를 반환합니다."""
#     n, m = len(text), len(pattern)
#     base = 263
#     prime = 10**9 + 7
#     power = pow(base, m - 1, prime)

#     pattern_hash = rolling_hash(pattern, base, prime)
#     current_hash = rolling_hash(text[:m], base, prime)

#     result = []

#     # 슬라이딩 윈도우를 통해 텍스트 탐색
#     for i in range(n - m + 1):
#         if current_hash == pattern_hash or mismatches_within_limit(text, pattern, i, k):
#             if mismatches_within_limit(text, pattern, i, k):
#                 result.append(i)

#         # 다음 윈도우로 해시값 업데이트
#         if i < n - m:
#             current_hash = update_hash(
#                 current_hash, text[i], text[i + m], power, base, prime
#             )

#     return result

# # 입력 처리 및 실행
# if __name__ == "__main__":
#     input = sys.stdin.read
#     data = input().strip().splitlines()

#     for line in data:
#         k, t, p = line.split()
#         k = int(k)
#         ans = pattern_matching_with_mismatches(k, t, p)
#         print(len(ans), *ans)  # 결과 출력
# import sys

# def rolling_hash(s, base, prime):
#     """주어진 문자열 s의 해시값을 계산합니다."""
#     hash_value = 0
#     for char in s:
#         hash_value = (hash_value * base + ord(char)) % prime
#     return hash_value

# def update_hash(prev_hash, old_char, new_char, power, base, prime):
#     """슬라이딩 윈도우에서 해시값을 업데이트합니다."""
#     new_hash = (prev_hash - ord(old_char) * power) * base + ord(new_char)
#     new_hash %= prime
#     return new_hash

# def mismatches_within_limit(t, p, start, k):
#     """텍스트 t와 패턴 p를 비교하여 최대 k개의 불일치를 허용합니다."""
#     mismatches = 0
#     for j in range(len(p)):
#         if t[start + j] != p[j]:
#             mismatches += 1
#             if mismatches > k:
#                 return False  # 최대 불일치 초과 시 중단
#     return True

# def pattern_matching_with_mismatches(k, text, pattern):
#     """최대 k개의 불일치로 패턴을 찾습니다."""
#     n, m = len(text), len(pattern)
#     base = 263
#     prime = 10**9 + 7
#     power = pow(base, m - 1, prime)  # 윈도우 이동에 사용되는 거듭제곱 값

#     pattern_hash = rolling_hash(pattern, base, prime)
#     current_hash = rolling_hash(text[:m], base, prime)

#     result = []

#     # 슬라이딩 윈도우 탐색
#     for i in range(n - m + 1):
#         # 해시가 일치하거나 불일치 허용 범위 내에 있는 경우
#         if current_hash == pattern_hash:
#             if mismatches_within_limit(text, pattern, i, k):
#                 result.append(i)
#         else:
#             # 해시가 일치하지 않아도 부분 비교 수행
#             if mismatches_within_limit(text, pattern, i, k):
#                 result.append(i)

#         # 다음 윈도우로 해시값 업데이트
#         if i < n - m:
#             current_hash = update_hash(
#                 current_hash, text[i], text[i + m], power, base, prime
#             )

#     return result

# # 입력 처리 및 실행
# if __name__ == "__main__":
#     input = sys.stdin.read
#     data = input().strip().splitlines()

#     for line in data:
#         k, t, p = line.split()
#         k = int(k)
#         ans = pattern_matching_with_mismatches(k, t, p)
#         print(len(ans), *ans)  # 결과 출력
# import sys

# def rolling_hash(s, base, prime):
#     """문자열 s의 해시값을 계산합니다."""
#     hash_value = 0
#     for char in s:
#         hash_value = (hash_value * base + ord(char)) % prime
#     return hash_value

# def update_hash(prev_hash, old_char, new_char, power, base, prime):
#     """슬라이딩 윈도우에서 해시를 O(1) 시간에 업데이트합니다."""
#     new_hash = (prev_hash - ord(old_char) * power) * base + ord(new_char)
#     new_hash %= prime
#     return new_hash

# def fast_mismatches_within_limit(t, p, start, k):
#     """최대 k개의 불일치를 허용하며 빠르게 비교합니다."""
#     mismatches = 0
#     for j in range(len(p)):
#         if t[start + j] != p[j]:
#             mismatches += 1
#             if mismatches > k:
#                 return False  # 불일치 초과 시 중단
#     return True

# def pattern_matching_with_mismatches(k, text, pattern):
#     """최대 k개의 불일치를 허용하며 패턴 매칭을 수행합니다."""
#     n, m = len(text), len(pattern)
#     base = 263
#     prime = 10**9 + 7
#     power = pow(base, m - 1, prime)  # 윈도우 이동에 필요한 값

#     # 패턴과 텍스트 첫 윈도우의 해시값 계산
#     pattern_hash = rolling_hash(pattern, base, prime)
#     current_hash = rolling_hash(text[:m], base, prime)

#     result = []

#     # 슬라이딩 윈도우 탐색
#     for i in range(n - m + 1):
#         # 해시가 일치하거나 불일치가 허용 범위 내인 경우만 추가 확인
#         if current_hash == pattern_hash or fast_mismatches_within_limit(text, pattern, i, k):
#             if fast_mismatches_within_limit(text, pattern, i, k):
#                 result.append(i)

#         # 다음 윈도우로 해시값 이동
#         if i < n - m:
#             current_hash = update_hash(
#                 current_hash, text[i], text[i + m], power, base, prime
#             )

#     return result

# # 입력 처리 및 실행
# if __name__ == "__main__":
#     input = sys.stdin.read
#     data = input().strip().splitlines()

#     for line in data:
#         k, t, p = line.split()
#         k = int(k)
#         ans = pattern_matching_with_mismatches(k, t, p)
#         print(len(ans), *ans)  # 결과 출력
MOD = 10**9 + 9
P = 31
P1 = 53
N = 200005

pp = [1] * N  # p^i % MOD 역원 저장
pp1 = [1] * N  # p1^i % MOD 역원 저장
h = [[], []]  # s와 t 각각의 해시값 저장

def mod_inv(a, m):
    """모듈러 역원을 구합니다."""
    return pow(a, m - 2, m)

def compute_hash(s, idx):
    """문자열 s에 대한 해시값을 미리 계산합니다."""
    hash_value = 0
    hash1_value = 0
    p_pow = 1
    p1_pow = 1

    h[idx].append((0, 0))  # 초기 해시값

    for i, char in enumerate(s):
        hash_value = (hash_value + (ord(char) - ord('a') + 1) * p_pow) % MOD
        hash1_value = (hash1_value + (ord(char) - ord('a') + 1) * p1_pow) % MOD

        pp[i] = mod_inv(p_pow, MOD)
        pp1[i] = mod_inv(p1_pow, MOD)

        p_pow = (p_pow * P) % MOD
        p1_pow = (p1_pow * P1) % MOD

        h[idx].append((hash_value, hash1_value))

def solve():
    """입력된 여러 쿼리에 대해 최대 k개의 불일치를 허용하는 패턴 매칭 수행."""
    while True:
        try:
            # 입력 처리
            k, s, t = input().split()
            k = int(k)
        except EOFError:
            break

        h[0].clear()
        h[1].clear()

        compute_hash(s, 0)
        compute_hash(t, 1)

        ans = []

        for i in range(len(s) - len(t) + 1):
            low = i
            cnt = 0

            while low < i + len(t):
                l, r = low, i + len(t) - 1
                ans1 = -1

                # 이진 탐색을 통해 불일치 위치 찾기
                while l <= r:
                    mid = (l + r) // 2
                    x_hash = (
                        ((h[0][mid + 1][0] - h[0][l][0] + MOD) * pp[l]) % MOD,
                        ((h[0][mid + 1][1] - h[0][l][1] + MOD) * pp1[l]) % MOD,
                    )
                    y_hash = (
                        ((h[1][mid + 1 - i][0] - h[1][l - i][0] + MOD) * pp[l - i]) % MOD,
                        ((h[1][mid + 1 - i][1] - h[1][l - i][1] + MOD) * pp1[l - i]) % MOD,
                    )

                    if x_hash == y_hash:
                        ans1 = mid
                        l = mid + 1
                    else:
                        r = mid - 1

                if ans1 == -1:
                    low += 1
                    cnt += 1
                else:
                    low = ans1 + 1

                if cnt > k:
                    break

            if cnt <= k:
                ans.append(i)

        print(len(ans), *ans)

# 메인 실행부
if __name__ == "__main__":
    solve()
