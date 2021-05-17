from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu',['enque','deque','peek','find','count','clear','dump','exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name} 'for m in Menu]
    while True:
        print(*s,sep='',end='')

        n = int(input(': '))

        if 1 <= n <= 8:
            return Menu(n)

        break

q = FixedQueue(64)

while True:
    print(f'data size / capacity = {q.num} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.enque:
        try:
            value = input('input enque value:')
            q.enque(value)

        except q.Full():
            print('Queue is full')

    elif menu == Menu.deque:
        try:
            print(f'deque value is {q.deque()}')

        except q.Empty():
            print('Queue is empty')

    elif menu == Menu.peek:
        try:
            print(f'peek data is {q.peek()}')

        except q.Empty():
            print(f'Queue is empty')

    elif menu == Menu.find:
        value = input('input value to find:')

        if value in q:
            idx = q.find(value)
            print(f'{value} has {idx} index')
        else:
            print(f'Queue has not {value}')

    elif menu == Menu.count:
        value = input('input the value to count:')
        print(f'The number of {value} is {q.count(value)}')

    elif menu == Menu.clear:
        q.clear()

    elif menu == Menu.dump:
       q.dump()

    elif menu == Menu.exit:
        break






