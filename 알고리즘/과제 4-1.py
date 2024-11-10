# 백준 1927 최소힙

# 최소 힙 구성

def heappush(item):
    # 1. 맨 뒤에 붙인다.
    heap.append(item)

    # 2. 부모와 비교 반복
    child = len(heap) - 1
    parent = child // 2

    while parent and heap[child] < heap[parent]:
        # 스왑
        heap[child], heap[parent] = heap[parent], heap[child]
        # 인덱스 갱신
        child = parent
        parent = child // 2


def heappop(heap):
    if len(heap) == 1:
        return 0
    # 1. 루트노드에서 뽑기
    result = heap[1]
    # 2. 맨 뒤 값을 루트노드로 옮기기(완전이진트리 구조를 유지하기 위해)
    heap[1] = heap[-1]
    heap.pop()
    
    parent = 1 # 루트노드 인덱스
    child = 2 # 왼쪽 자식노드 인덱스

    # 오른쪽 자식노드가 존재하고, 오른쪽 값이 더 작은 경우
    # 오른쪽 자식노드로 변경
    if child+1 <= len(heap)-1 and heap[child+1] < heap[child]:
        child += 1

    # 3. 자식노드와 비교해서 옮길 수 있으면 스왑하기
    while child <= len(heap)-1 and heap[parent] > heap[child]:
        # 스왑
        heap[child], heap[parent] = heap[parent], heap[child]
        # 인덱스 갱신
        parent = child
        child = parent * 2 # 왼쪽 노드부터 고려

        # 오른쪽 자식노드가 존재하고, 오른쪽 값이 더 작은 경우
        # 오른쪽 자식노드로 변경
        if child+1 <= len(heap)-1 and heap[child+1] < heap[child]:
            child += 1

    return result


N = int(input())
# 인덱스 0은 비워두기
heap = ['-']

for _ in range(N):
    x = int(input())
    if x:
        heappush(x)
    else:
        print(heappop(heap))