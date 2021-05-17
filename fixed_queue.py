from typing import Any

class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self,capacity:int) -> None:
        self.num =0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * self.capacity

    def __len__(self):
        return self.num

    def is_empty(self) -> bool:
        return self.num <= 0

    def is_full(self) -> bool:
        return self.num >= self.capacity

    def enque(self,value) -> None:

        if self.is_full():
            raise FixedQueue.Full

        self.que[self.rear] = value

        self.rear += 1
        self.num += 1

        if self.rear >= self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty

        value = self.que[self.front]

        self.front += 1
        self.num -= 1

        if self.front == self.capacity:
            self.front =0

        return value

    def peek(self) -> Any:
        if self.is_empty():
            raise self.Empty

        return self.que[self.rear -1]

    def find(self,value) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty

        for i in range(self.num):
            idx = (i+self.front)%self.capacity
            if self.que[idx] == value:
                return idx

        return -1

    def count(self,value) -> int:

        cnt = 0
        for i in range(self.num):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                cnt += 1

        return cnt

    def __contains__(self,value) -> bool:
        return self.count(value)

    def clear(self):
        self.front = self.rear = self.num =0

    def dump(self):
        if self.is_empty():
            print(f'queue is empty')

        else:
           """
            print('#dump 1')
            print(self.que)
            print()
            """

            print("#dump 2")
            for i in range(self.num):
                idx = (i+self.front) % self.capacity
                print(f'{self.que[idx]}',end=' ')
            print()