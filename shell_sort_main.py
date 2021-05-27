from typing import MutableSequence

def shell_sort(a:MutableSequence) -> None:
    n = len(a)
    h = n // 2

    while h > 0:
        for i in range(h,n):
            j = i - h
            tmp = a[i]

            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 2

"""셸 정렬에서 h 값을 (3h+1)수열로 사용하기"""
def shell_sort2(a:MutableSequence) -> None:
    n = len(a)
    h = 1

    while h < n//9:
        h = 3*h+1

    while h > 0:
        for i in range(h,n):
            j = i - h
            tmp = a[i]

            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 3


if __name__ == '__main__':
    print('셸 정렬 수행')
    num = int(input('원소의 갯수을 입력해주십시오>'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]>'))

    shell_sort2(x)
    print(x)