from typing import Any, Sequence

class FixedStack:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self,capacity):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self,value: Any)-> None:

        if self.is_full():
            raise FixedStack.Full

        self.stk[self.ptr] = value
        self.ptr += 1


    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty

        self.ptr -=1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty

        return self.stk[self.ptr-1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self,value:Any) -> Any: #Top ~ Bottom으로 검색 수행

        for i in range(self.ptr-1,-1,-1): # ptr-1 ~ 0 까지 1씩 감소
            if self.stk[i] == value:
                return i

        return -1

    def count(self,value:Any) -> int:
        cnt = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                cnt +=1

        return cnt

    def __contains__(self,value:Any) -> bool:
        return self.count(value)        #굳이 self.cont(value) > 0 ?

    def dump(self) ->None:
        if self.is_empty():
            print('Stack is Empty')
        else:
            print('#dump 1')
            for i in range(self.ptr):
                print(f'{self.stk[i]} ',end='')
            print()

            print('#dump 2')
            print(self.stk[:self.ptr])
