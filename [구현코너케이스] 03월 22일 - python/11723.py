import sys # 시스템 모듈 임포트
input = sys.stdin.readline # 입력 여러개 받을 것임

"""
집합 단순 구현 문제
리스트 사용 - 이유(set()을 사용해서 매번 연산하면 시간이 오래 걸려서)
입력되는 x의 값이 1~20으로 범위 아주 작기 때문에, 
각 숫자가 집합에 들어있는 여부를 저장하는 리스트 만듦

1. 크기가 21인 리스트 선언
2. add는 True, remove는 false
"""


SIZE = 21 # 왜 20이 아니라 21인가욥...
m = int(input()) # 입력 받기
s = [False]*Size  # 배열의 크기만큼 리스트 만들기, 전부 false로 해서 아무것도 안 들은 것 표현
value = {"all":True, "empty":False} # value에 all이란 다 1부터 20까지 다 참, empty는 공집합 만듦

def update(cmd): # 어떤 연산이 들어올 시에
    for i in range(1, 21): # s[1]부터 s[20]까지 값을 계산
        s[i] = value[cmd] 

def check(num): # check는 
    if s[num]: # 집합에 s[num]이 있으면 1출력
        return 1
    return 0 # 없으면 0 출력

for _ in range(m): # m만큼 연산을 입력받는다
    cmd = input().split() # ( 연산, 수 ) 순서로 입력되므로 split()해서 연산과 수 따로 저장 

    if len(cmd) == 1: # 처음으로 문자열이 들어오면(문자열 길이 1이면)
        update(cmd[0]) # cmd[0]으로 전부 세팅
        continue
    else:
        num  = int(cmd[1]) # 그렇지 않으면 num에 cmd[1] 넣음

    if cmd[0] == "add": # add는 집합 s에 x를 추가
        s[num] = True 
    elif cmd[0] == "remove": # remove는 x를 삭제
        s[num] = False
    elif cmd[0] == "check": # check는 check(num을 출력
        print(check(num))
    elif cmd[0] == "toggle": # toggle은 s[num]을 참거짓 반대로
        s[num] = not s[num]  # 즉, 있->없 없->있


