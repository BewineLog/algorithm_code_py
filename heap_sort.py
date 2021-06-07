from typing import MutableSequence
import heapq

def heap_sort(a:MutableSequence) -> None:


    def down_heap(a:MutableSequence, left:int, right:int) -> None:
        temp = a[left] #Root
        parent = left

        while parent < (right+1)//2:
            cl = parent *2 + 1
            cr = cl + 1

            child = cr if cr <= right and a[cr] > a[cl] else cl #child 중 큰 값 선택

            if temp >= a[child]:
                break

            a[parent] = a[child]
            parent = child
        a[parent] = temp



    n = len(a)

    for i in range((n-1)//2,-1,-1): # (n-1)//2 ~ 0
        down_heap(a,i,n-1)

    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a,0,i-1)


"""heapq.push와 heapq.pop을 통해 구현하기"""
def heap_sort2(a:MutableSequence) -> None:
    heap = []

    for i in a:
        heapq.heappush(heap,i)

    for i in range(len(a)):
        a[i] = heapq.heappop(heap)

if __name__ == '__main__':
    print('Heap sort!')
    num = int(input('input num of elements>'))
    x = [None] *num

    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))

    print(x)
#    heap_sort(x)
    heap_sort(x)
    print(x)