import sys # 시스템 모듈 인풋
input = sys.stdin.readline # 한 줄 단위로 인풋 받음

"""
[그룹 단어 체커] - 단순 구현 문제
- 이미 등장한 알파벳 저장할 set() 선언 (탐색 O(1))
- 처음 등장하는 알파벳은 set에 추가하고, 무리에서 떨어졌는데 이미 등장한 알파벳이면 그룹 단어가 아니다.
"""

def is_group_word(word): # word를 받아서 true나 false를 리턴함
    checked = set() # 들어있는지 체크하기 위한 집합
    prev = None # 직전의 값

    for c in word: # word에 대해서
        if c == prev: # 직전 값과 같으면 
            continue # 계속하기
        
        if c in checked: # set()에 들어 있으면 false
            return False  

        checked.add(c) # 아직 안 나왔고 직전값도 아니면 c를 checked에 더한다
        prev = c # c를 prev에 넣기

    return True


# 입력
n = int(input()) # 입력받는 데이터 개수를 입력받는다

# 입력 + 연산
count = 0 # 집단단어 개수를 저장할 정수

for _ in range(n): # n번 반복
    word = input().rstrip() # 인풋 받아서 rstrip(공백제거)해서 word에 저장
    if is_group_word(word): # 만약 word가 group_word라면
        count += 1 # count를 1키움

# 출력
print(count) # count를 출력