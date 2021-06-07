"""
Brute Force법으로 문자열 검색, 위치 찾기.
"""
def bf_match(txt:str ,pat:str) -> int:
    pt = 0
    pp = 0

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp ==len(pat) else -1

def bf_match_op(txt:str, pat:str) -> int:

    if pat in txt:
       # return txt.find(pat)
        return txt.index(pat)
    else:
        return -1

if __name__ =='__main__':
    s1 = input('input txt>')
    s2 = input('input pattern>')

    #idx = bf_match(s1,s2)
    idx = bf_match_op(s1,s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{idx+1}번째 부터 패턴이 일치합니다.')