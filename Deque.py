from typing import Any
from collections import deque


class Stack:

    def __init__(self, maxlen: int = 256) -> None:
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        return len(self.__stk)

    def is_empty(self) -> bool:
        return not self.__stk

    def is_Full(self) -> bool:
        return len(self.__stk) == self.__stk.maxlen  # self.capacity?

    def push(self, value: Any) -> None:
        self.__stk.append(value)

    def pop(self) -> Any:
        try:
            return self.__stk.pop()
        except IndexError:
            return -1

    def peek(self) -> Any:
        return self.__stk[-1]

    def clear(self) -> None:
        self.__stk.clear()

    def find(self,value: Any)-> Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self,value:Any)-> int:
        return self.__stk.count(value)

    def __contains__(self,value) -> bool:
        return self.count(value)

    def dump(self) -> int:
        print(list(self.__stk))