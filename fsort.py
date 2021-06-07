"""도수 정렬 알고리즘"""
from typing import MutableSequence

def fsort(a :MutableSequence, max: int) -> None:
    n = len(a)
    f = [0] * (max+1)
    b = [0] * n

    for i in range(n): f[a[i]] += 1
    for i in range(1,max+1): f[i] += f[i-1]
    for i in range(n-1,-1,-1):
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]

    for i in range(n):
        a[i] = b[i]

def counting_sort(a:MutableSequence):
    fsort(a,max(a))

if __name__ == '__main__':
    n = int(input('input element number>'))
    x = [None] * n

    for i in range(n):
        while True:
            x[i] = int(input(f'x[{i}]:'))
            if x[i] >= 0:
                break

    print(x)
    counting_sort(x)
    print(x)

