from __future__ import annotations
from typing import Any, Type

class Node:
    """연결 리스트용 노드 클래스"""

    def __init__(self, data: Any = None, next: Node = None):
        self.data = data
        self.next = next


class LinkedList:
    """연결 리스트 클래스"""
    def __init__(self) -> None:
        self.no = 0 # 노드 갯수
        self.head = None # 머리 노드
        self.current = None # 주목 노드

    def __len__(self):
        return self.no

    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head

        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next

        return -1 # 노드 꼬리까지 갔는데도 발견을 못했을 경우.

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    # 머리에 노드 삽입
    def add_first(self,data: Any) -> None:
        ptr = self.head
        self.head = self.current = Node(data,ptr)
        self.no += 1

    # 꼬리에 노드 삽입
    def add_last(self,data: Any) -> None:
        if self.head is None:
            self.add_first(data)

        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next

            ptr.next = self.current= Node(data,None)
            self.no += 1

    # 머리 노드 삭제
    def remove_first(self) -> None:
        if self.head is not None:
            self.head = self.current = self.head.next
            self.no -= 1

    # 꼬리 노드 삭제
    def remove_last(self) -> None:
        if self.head is not None:
            if self.head.next is None: #Node가 1개 뿐이라면
                self.remove_first()

            else: # 노드가 여러개라면
                ptr = self.head
                pre = self.head

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no -= 1

    # 임의의 노드 삭제
    def remove(self, p: Node) -> None:

        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None: # p Node가 존재 하지 않음
                        return

                # ptr.next = p
                ptr.next = p.next
                ptr.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head is not None:
            self.remove_first()
        self.current = 0
        self.no = 0

    # 주목 노드를 한칸 뒤로 이동
    def next(self) -> bool:
        if self.current is None or self.current.next is None:
            return False

        self.current = self.current.next
        return True

    def print_current(self) -> None:
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)

    def print(self) -> None:
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.head)

# 링크드리스트 이터레이터용 클래스
class LinkedListIterator:
    def __init__(self,head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
