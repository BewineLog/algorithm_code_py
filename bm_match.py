"""
보이어/무어법으로 문자열 검색
"""
def bm_match(txt:str, pat:str) -> int:
    skip = [None] * 256

    # 건너뛰기 표 만들기
    for pt in range(256):
        skip[pt] = len(pat) # 모든 배열의 값을 pattern 길이로 입력

    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt -1

    # 검색하기
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1

        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp

    return -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요>')
    s2 = input('패턴을 입력하세요>')

    idx = bm_match(s1,s2)

    if idx == -1:
        print('텍스트에 패턴이 존재하지 않습니다.')
    else:
        print(f'{idx+1}번째 부터 패턴이 일치합니다')