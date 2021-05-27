"""
-quick_sort
-if element_number < 9, use insertion_sort
-select pivot by advanced method
"""

from typing import MutableSequence

def sort3(a:MutableSequence, idx1:int, idx2:int, idx3:int) -> int:
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2] #idx1,2 중에 큰 값을 idx2
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3] #idx2,3 중에 큰 값을 idx3
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]

    """
    idx1, idx2, idx3 = sorted([idx1,idx2,idx3])
    return idx2 랑 동일한 코드 아닌가?
    """

    return idx2

def insertion_sort(a:MutableSequence,num:int) -> None:

    for i in range(1,num):
        tmp = a[i]
        j = i
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

def qsort(a:MutableSequence,left:int,right:int) -> None:
    pl = left
    pr = right

    mid = sort3(a,left,(pl+pr)//2,right)
    a[mid], a[right -1] = a[right -1], a[mid]

    pivot = a[mid]

    while pl <= pr:
        while a[pl] < pivot: pl += 1
        while a[pr] > pivot: pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a,left,pr)
    if right > pl : qsort(a,pl,right)

def quick_sort(a:MutableSequence) -> None:
    n = len(a)

    if n < 9:
        insertion_sort(a,n)
    else:
        qsort(a,0,n-1)


if __name__ =='__main__':
    print(f'퀵 정렬을 수행합니다.(단, 원소의 갯수가 9 미만일 경우 단순 삽입 정렬을 수행합니다.)')
    num = int(input(f'원소의 갯수를 입력하십시오>'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]>'))

    quick_sort(x)
    print(x)

