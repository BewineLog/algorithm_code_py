from typing import MutableSequence, Sequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)

    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j] < a[j-1]:
                a[j-1], a[j] = a[j], a[j-1]

def bubble_sort_details(a:MutableSequence) -> None:
    ccnt = 0 #Comparison count
    scnt = 0 #Swap count

    n = len(a)

    for i in range(n):
        print(f'pass{i+1}')
        for j in range(n-1, i, -1):
            for m in range(0,n):
                print(f'{a[m]:2}' + ('  ' if m != j-1 else ' +' if a[j] < a[j-1] else ' -'),end='')
            print()

            ccnt += 1
            if a[j] < a[j-1]:
                a[j-1], a[j] = a[j], a[j-1]
                scnt += 1


    print(f'ccnt:{ccnt}, scnt:{scnt}')

#교환횟수가 0이면 정렬이 완료된 것에서 착안.
def bubble_sort2(a:MutableSequence) -> None:
    n = len(a)

    for i in range(n-1):
        exchng = 0 #교환 횟수 check value
        for j in range(n-1,i,-1):
            if(a[j] < a[j-1]):
                a[j-1],a[j] = a[j], a[j-1]
                exchng += 1

        if exchng == 0:
            break

def bubble_sort2_details(a:MutableSequence) -> None:
    ccnt = 0 #Comparison count
    scnt = 0 #Swap count

    n = len(a)

    for i in range(n):
        print(f'pass{i+1}')
        exchng = 0
        for j in range(n-1, i, -1):
            for m in range(0,n):
                print(f'{a[m]:2}' + ('  ' if m != j-1 else ' +' if a[j] < a[j-1] else ' -'),end='')
            print()

            ccnt += 1
            if a[j] < a[j-1]:
                a[j-1], a[j] = a[j], a[j-1]
                scnt += 1
                exchng += 1

        if exchng == 0:
            break


    print(f'ccnt:{ccnt}, scnt:{scnt}')


# 마지막 교환 point 이전은 정렬되었다는 것에서 착안.
def bubble_sort3(a:MutableSequence) -> None:
    i = 0
    last = 0
    n = len(a)

    while i < n-1:
        last = n - 1
        for j in range(n-1,i,-1):
            if a[j] < a[j-1]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        i = last

#bidirectional bubble sort(양방향성)

def shaker_sort(a:MutableSequence) -> None:
    n = len(a)
    left = 0
    right = n - 1
    last = right

    ccnt = scnt = 0 # Comparison count , Swap count

    while left < right:

        #홀수번째 pass
        for i in range(right,left,-1):
            ccnt += 1
            if a[i] < a[i-1]:
                a[i-1],a[i] = a[i], a[i-1]
                last = i
                scnt += 1
        left = last

        #짝수번째 pass
        for i in range(left,right):
            ccnt += 1
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1], a[i]
                last = i
                scnt += 1
        right = last

    print(f'ccnt:{ccnt}, scnt:{scnt}')

def print_ary(a: Sequence, n:int) -> None:
    for i in range(n):
        print(f'{a[i]}',end=' ')
    print()

if __name__ == '__main__':
    print('Bubble Sort')

    nx = int(input('input array size:'))

    # nx가 음수일 경우, 예외처리
    while nx < 0:
        nx = int(input('input array size:'))

    a = [None] * nx

    for i in range(nx):
        a[i] = int(input(f'input a[{i}]:'))

    print_ary(a,nx)
    shaker_sort(a)
    print_ary(a,nx)



