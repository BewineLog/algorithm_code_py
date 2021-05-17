"""
Deque의 main 함수 입니다.
"""
from enum import Enum
from Deque import Stack

Menu = Enum('Menu',['push','pop','peek','find','count','dump','exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name} ' for m in Menu]
    while True:
        print(*s,sep='',end='')

        n = int(input(": "))

        if 1 <= n <= 7:
            return Menu(n)

s = Stack()

while True:
   # print(f'data/capacity : {len()}/{s.capacity}')
    menu = select_menu()

    if menu == Menu.push:
        if s.is_Full():
            print('stack is Full')
        else:
            value = input('input push value')
            s.push(value)
    elif menu == Menu.pop:
        if s.is_empty():
            print('Deck is empty')
        else:
            print(f'pop data : {s.pop()}')

    elif menu == Menu.peek:
        if s.is_empty():
            print(f'Deck is empty!!!')
        else:
            print('Peek data:'+s.peek())

    elif menu == Menu.find:
        value = input('input find value:')
        idx = s.find(value)

        if idx != -1:
            print(f'value\'s idx is {idx}')
        else:
            print(f'cannot find value')

    elif menu == Menu.count:
        value = input("input value to get count:")
        print(f'{s.count(value)}')

    elif menu == Menu.dump:
        s.dump()

    elif menu == Menu.exit:
        break
