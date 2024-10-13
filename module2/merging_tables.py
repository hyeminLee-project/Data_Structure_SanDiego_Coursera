class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts  # 각 테이블의 초기 행 수 저장
        self.max_row_count = max(row_counts)  # 최대 테이블 크기 저장
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables  # 각 테이블의 트리 깊이(랭크) 초기화
        self.parents = list(range(n_tables))  # 초기에는 모든 테이블이 자기 자신을 부모로 가짐

    def merge(self, src, dst):
        # src와 dst 테이블의 부모 테이블을 찾음
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False  # 이미 같은 그룹이면 병합할 필요가 없음

        # Union by rank 사용: 더 깊이가 낮은 트리를 깊이가 높은 트리에 병합
        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            self.row_counts[dst_parent] = 0
        else:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            self.row_counts[src_parent] = 0
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[dst_parent] += 1

        # 병합 후 최대 테이블 크기 업데이트
        self.max_row_count = max(self.max_row_count, self.row_counts[src_parent], self.row_counts[dst_parent])
        return True

    def get_parent(self, table):
        # 경로 압축 기법을 사용해 부모 테이블을 찾음
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)  # 입력된 테이블 번호는 1-based이므로, 0-based로 변환
        print(db.max_row_count)  # 현재 최대 테이블 크기 출력


if __name__ == "__main__":
    main()
