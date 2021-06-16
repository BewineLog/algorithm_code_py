from __future__ import annotations
from typing import Any, Type

class Node:
    """이진 검색 트리의 노드"""
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        """생성자"""
        self.key = key #키
        self.value = value #값
        self.left = left #왼쪽 노드 포인터
        self.right = right #오른쪽 노드 포인터

class BinarySearchTree:
    """이진 검색 트리"""
    def __init__(self):
        self.root = None #Root

    def search(self,key: Any) -> Any:
        """키가 key인 노드를 검색"""
        p = self.root

        while True:
            if p is None:
                return None

            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self,key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 노드를 삽입"""

        def add_node(node: Node, key: Any, value: Any) -> None:
            """node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입"""
            if key == node.key: #트리에 동일한 키는 들어갈 수 없음
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key,value,None,None) #비어 있으면 노드 추가
                else:
                    add_node(node.left,key,value)#왼쪽 노드가 차 있으면, 왼쪽 노드를 매개변수로 하여 재귀적 호출

            else:
                if node.right is None:
                    node.right = Node(key,value,None,None) #비어 있으면 노드 추가
                else:
                    add_node(node.right,key,value) #오른쪽 노드가 있으면, 오른쪽 노드를 매개변수로 하여 재귀적 호출
            return True

        if self.root is None:
            self.root = Node(key,value,None,None)
            return True
        else:
            return add_node(self.root,key,value)

    def remove(self,key: Any) -> bool:
        """키가 key인 노드 삭제"""
        p = self.root #스캔 중인 노드
        parent = None #스캔 중인 노드의 부모 노드
        is_left_child = True #p는 parent의 왼쪽 자식 노드인지 확인

        while True:
            if p is None:
                return False

            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right

        if p.left is None:
            if p is self.root: #왼쪽 자식이 없고, p가 루트이면 오른쪽 자식으로 이동
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right

        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left

        else: # 자식이 둘 다 있으면
            parent = p
            left = p.left
            is_left_child = True

            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key
            p.value = left.value

            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        return True

    def dump(self,reverse = False) -> None:
        """모든 노드의 키를 오름차순으로 출력(LVR)"""

        def print_subtree(node:Node):
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key} {node.value}')
                print_subtree(node.right)

        def print_subtree_rev(node:Node):
            if node is not None:
                print_subtree_rev(node.right)
                print(f'{node.key} {node.value}')
                print_subtree_rev(node.left)

        print_subtree_rev(self.root) if reverse else print_subtree(self.root)



    def min_key(self) -> Any:
        if self.root is None:
            return None

        p = self.root
        while p.left is not None:
            p = p.left

        return p.key

    def max_key(self) -> Any:
        if self.root is None:
            return None

        p = self.root
        while p.right is not None:
            p = p.right
        return p.key
