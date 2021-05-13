"""
fixed_stack.py의 main함수 입니다.
"""
from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu',['푸시','팝','피크','검색','덤프','종료'])

#Menu 선택 함수
def select_menu() -> Menu:

    s = [f'({m.value}){m.name}'for m in Menu]
    while True:
        print(*s,sep=' ',end='')
        n = int(input(": "))
        if 1<= n <=6:
            return Menu(n)


s = FixedStack(64)

while True:
    print("현재 데이터 갯수: {} / {}".format(len(s),s.capacity))
    menu = select_menu()

    if menu == menu.푸시:
        value = int(input("푸시 데이터:"))
        try:
            s.push(value)
        except FixedStack.Full:
            print('스택이 꽉 차 있습니다.')

    elif menu == menu.팝:
        try:
            x = s.pop()
            print(f'팝 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어있습니다.')

    elif menu == menu.피크:
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어있습니다.')

    elif menu == menu.검색:
        x = int(input("검색할 데이터:"))

        if x in s:
            print(f'검색한 데이터의 갯수는 {s.count(x)}이고, 맨 앞의 위치 및 값은 s.stk[{s.find(x)}]/{s.stk[s.find(x)]}입니다.')

        else:
            print('검색한 데이터를 찾을 수 없습니다.')

    elif menu == menu.덤프:
        s.dump()

    else:
        break
