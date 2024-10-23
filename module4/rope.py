#!/usr/bin/python3

import sys

class Rope:
    def __init__(self, s):
        self.s = s  # 초기 문자열 저장

    def result(self):
        return self.s  # 최종 문자열 반환

    def process(self, i, j, k):
        # 문자열 [i..j] 부분을 추출
        substring = self.s[i:j+1]

        # 남은 문자열은 [0..i-1] + [j+1..] 부분
        remaining = self.s[:i] + self.s[j+1:]

        # k 위치에 substring을 삽입
        self.s = remaining[:k] + substring + remaining[k:]

# 입력 처리
rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())  # 쿼리 수 입력

# 쿼리 처리
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)

# 최종 결과 출력
print(rope.result())
