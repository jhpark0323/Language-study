import itertools

n, m = map(int, input().split())

card = list(map(int, input().split()))

# 조합 -> itertools에 있는 combinations를 이용해 card의 부분집합중 원소가 3인 모든 부분집합들 생성
combi = list(itertools.combinations(card, 3))

# # 각각의 부분집합이 tuple형태로 생성
# print(combi)

# 합을 담을 변수
similar = 0

# 각각의 부분집합을 순회
for combinations in combi:
    
    # 부분집합의 합이 m보다 작고 similar보다 크면 similar에 그 합을 재할당
    if (sum(combinations) <= m) & (sum(combinations) > similar):
        similar = sum(combinations)

print(similar)

'''
Q : 그럼 얘는 시간복잡도가 얼마나되냐

A : itertools.combinations 함수의 시간 복잡도는 O(nCk)입니다. 여기서 n은 리스트의 길이이고, k는 부분집합의 길이입니다. 따라서 이 함수의 실행 시간은 조합의 개수에 비례합니다.

만약 nCk가 매우 큰 경우, 모든 조합을 생성하는 데 시간이 오래 걸릴 수 있습니다. 하지만 파이썬의 itertools 모듈은 내부적으로 효율적인 알고리즘을 사용하므로, 일반적으로는 빠르게 동작합니다.

또한, 결과를 리스트로 변환하는 부분(list(itertools.combinations(card, 3)))에서도 시간이 소요됩니다. 만약 큰 결과를 다루고 있다면, 결과를 필요에 따라 한 번에 처리하거나 제너레이터로 처리하는 것이 메모리 사용면에서 효율적일 수 있습니다.


Q : 이걸 브루트포스로 하면 for문 3개 돌릴거아니야 그럼 그거보다는 빠르겠네?

A : 네, 맞습니다. itertools.combinations를 사용하는 경우, 이는 내부적으로 최적화된 알고리즘을 활용하여 조합을 생성하기 때문에 브루트포스로 세 개의 for 루프를 돌리는 것보다 훨씬 효율적입니다.

브루트포스로 직접 구현하려면 세 개의 for 루프를 돌려야 하며, 각 루프에서 가능한 모든 조합을 확인해야 합니다. 이렇게 하면 중복된 조합을 고려해야 하고, 효율적이지 않을 수 있습니다.

itertools.combinations는 이러한 작업을 내부적으로 최적화하므로 코드가 간결하고 성능이 우수합니다. 따라서 조합을 생성할 때는 itertools를 사용하는 것이 권장됩니다.

-by chat gpt
'''

'''
한줄요약
브루트포스로 하는 것 보다 훨 빠르다
'''
