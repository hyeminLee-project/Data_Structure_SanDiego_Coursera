def read_input():
    return input().rstrip(), input().rstrip()

def print_occurrences(output):
    print(' '.join(map(str, output)))

def rabin_karp(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    base = 256  # 해시 계산용 진수
    prime = 1000000007  # 큰 소수 (충돌 최소화)

    # 해시 계산을 위한 초기화
    pattern_hash = 0  # 패턴 해시 값
    window_hash = 0  # 현재 윈도우 해시 값
    h = 1  # 슬라이딩 윈도우에서 사용할 값 (base^(p_len-1) % prime)

    # h 계산: base^(p_len-1) % prime
    for _ in range(p_len - 1):
        h = (h * base) % prime

    # 패턴과 첫 번째 윈도우의 해시 값을 계산
    for i in range(p_len):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime

    occurrences = []  # 매칭 위치 저장

    # 슬라이딩 윈도우로 텍스트를 탐색
    for i in range(t_len - p_len + 1):
        # 현재 윈도우 해시와 패턴 해시가 같을 경우
        if pattern_hash == window_hash:
            # 실제 문자열 비교로 일치 확인
            if text[i:i + p_len] == pattern:
                occurrences.append(i)

        # 다음 윈도우 해시 값 계산 (슬라이딩 윈도우)
        if i < t_len - p_len:
            window_hash = (window_hash - ord(text[i]) * h) % prime
            window_hash = (window_hash * base + ord(text[i + p_len])) % prime

            # 음수 해시 값을 양수로 변환
            if window_hash < 0:
                window_hash += prime

    return occurrences

if __name__ == '__main__':
    pattern, text = read_input()
    print_occurrences(rabin_karp(pattern, text))
