# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    """
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    """

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v,e = map(int,input().split())
parent = [0] * (v+1)

# 부모 테이블 초기화
for i in range(1,v+1):
    parent[i] = i

# cycle 여부 판별
cycle = False

for i in range(e):
    a,b = map(int,input().split())

    # cycle이 발생한 경우, 종료
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)

# cycle 발생 여부 출력
if cycle:
    print('cycle이 발생했습니다.')
else:
    print('cycle은 발생하지 않았습니다.')

