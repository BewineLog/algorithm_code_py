from typing import MutableSequence
from stack import Stack

"""배열을 두 그룹으로 나누기"""
def partition(a:MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n-1
    pivot = a[(pl+pr)//2]

    while pl <= pr:
        while a[pl] < pivot: pl += 1
        while a[pr] > pivot: pr -= 1

        if pl <= pr:
            a[pl],a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'Pivot:{pivot}')
    print('pivot 이하의 그룹')
    print(f'{a[0:pl]}')

    print('pivot과 일치하는 그룹')
    if pl > pr + 1:
        print(*a[pr+1:pl])
    print('pivot 이상인 그룹')
    print(*a[pl:n])

def qsort(a:MutableSequence,left:int ,right:int) -> None:
    pl = left
    pr = right
    pivot = a[(pl+pr)//2]

    while pl <= pr:
        while a[pl] < pivot: pl += 1
        while a[pr] > pivot: pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl+=1
            pr-=1

    if left < pr: qsort(a,left,pr)

    if pl < right: qsort(a,pl,right)

def qsort_detail(a:MutableSequence,left:int, right:int) -> None:
    pl = left
    pr = right
    pivot = a[(pl+pr)//2]

    print(f'a[{left}] ~ a[{right}]:', *a[left:right+1])

    while pl <= pr:
        while a[pl] < pivot: pl += 1
        while a[pr] > pivot: pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl+=1
            pr-=1

    if left < pr: qsort_detail(a,left,pr)

    if pl < right: qsort_detail(a,pl,right)

def qsort_not_recur(a:MutableSequence, left:int, right:int) -> None:
    range = Stack(right-left+1)

    range.push((left,right))

    while not range.is_empty():
        pl,pr = left,right = range.pop()
        pivot = a[(pl+pr)//2]

        while pl <= pr:
            while a[pl] < pivot: pl += 1
            while a[pr] > pivot: pr -= 1

            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: range.push((left,pr))
        if right > pl: range.push((pl,right))





if __name__ == '__main__':
    print('배열을 나눕니다.')
    num = int(input('배열 요소의 갯수를 입력하십시오>'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]>'))

#    qsort(x,0,num-1)
#   qsort_detail(x,0,num-1)
    qsort_not_recur(x,0,num-1)
    print(x)
#    print(x)
#    print(*x)