class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # 버킷 별로 리스트를 생성합니다.
        self.table = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        """해시 함수: 문자열을 정수로 매핑"""
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def process_query(self, query):
        if query.type == 'check':
            # 지정된 버킷의 내용을 출력합니다.
            self.write_chain(self.table[query.ind])

        else:
            hashed_index = self._hash_func(query.s)
            chain = self.table[hashed_index]

            if query.type == 'find':
                # 문자열이 존재하는지 확인합니다.
                self.write_search_result(query.s in chain)

            elif query.type == 'add':
                # 이미 존재하지 않으면 추가합니다.
                if query.s not in chain:
                    chain.insert(0, query.s)  # 체이닝에서 맨 앞에 삽입

            elif query.type == 'del':
                # 존재하면 삭제합니다.
                if query.s in chain:
                    chain.remove(query.s)

    def process_queries(self):
        n = int(input())  # 쿼리 수 입력
        for _ in range(n):
            query = Query(input().split())
            self.process_query(query)

if __name__ == '__main__':
    bucket_count = int(input())  # 버킷 수 입력
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
