from typing import Sequence, MutableSequence
import heapq

def merge_sorted_list(a:Sequence,b:Sequence, c:MutableSequence) -> None:
    """정렬된 a,b를 병합하여 c에 저장하는 함수"""
    pa, pb, pc = 0, 0, 0
    na, nb, nc = len(a), len(b), len(c)

    while pa < na and pb < nb:
        if a[pa] > b[pb]:
            c[pc] = b[pb]
            pb += 1
        else:
            c[pc] = a[pa]
            pa += 1
        pc += 1

    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:
        c[pc] = b[pb]
        pc += 1
        pb += 1

def merge_sort(a:MutableSequence) -> None:

    def _merge_sort(a:MutableSequence, left: int, right: int) -> None:
        if left < right:
            center = (left + right) // 2

            _merge_sort(a,0,center)
            _merge_sort(a,center+1,right)

            p = j = 0
            i = k = 0

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1 # i 값은 center+1로 종료.

            while i <= right and j < p:
                if a[i] > buff[j]:
                    a[k] = buff[j]
                    k += 1
                    j += 1

                else:
                    a[k] = a[i]
                    k += 1
                    i += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
    n = len(a)
    buff = [None] * n #임시용 buff
    _merge_sort(a,0,n-1)
    del buff #임시용 buff 소멸

"""
if __name__ == '__main__':
    na = int(input('a array size:'))
    nb = int(input('b array size:'))
    nc = na+nb

    a= [None] * na
    b= [None] * nb
    c= [None] * nc

    for i in range(na):
        a[i] = int(input(f'a[{i}]:'))

    a = sorted(a)

    for i in range(nb):
        b[i] = int(input(f'b[{i}]:'))

    b = sorted(b)

    #merge_sorted_list(a,b,c)
    c = list(heapq.merge(a,b))
    print(c)"""

if __name__ == '__main__':
    print('Merge sort')
    num = int(input('input number of element:'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))
    print(x)

    merge_sort(x)

    print(x)
