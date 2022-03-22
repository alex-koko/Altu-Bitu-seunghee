import sys # 시스템 모듈을 임포트한다
input = sys.stdin.readline # 수를 여러 개 입력받을 때 input()대신 이거 사용

"""
[30]
30의 배수 = 10의 배수 && 3의 배수
1. 10의 배수 -> 입력된 수에 0이 포함되어 있는지 확인
2. 3의 배수 -> 모든 자리수의 합이 3의 배수인지 확인

30의 배수임이 확인 되었으면,
가장 큰 수를 만들기 위해 9부터 0까지 역순으로 나열한다.
"""

def find_number(n):
    digits = list(n) # 입력 받은 수를 자리수로 끊어서 list에 저장한다
    digits.sort(reverse=True)   # 가장 큰 수를 만들기 위해 역순으로 정렬

    # 0이 존재하지 않으면, return -1
    if digits[-1] != '0': # 0이 없으면 10의 배수가 아니기 때문
        return -1
    
    total = 0   # 3의 배수인지 확인하기 위해 모든 자리수를 더함

    for i in digits: 
        total += int(i) # for문을 이용해 모든 자리수를 더하기

    # 3의 배수임을 확인
    if total % 3 == 0: # 3으로 나눈 나머지가 0이면(3의 배수이다)
        return ''.join(digits) # 자리수들을 연결해서 반환한다
    else:
        return -1 # 3의 배수가 아닐 경우 -1 출력

# 입력
n = input().rstrip() # 문자열의 오른쪽의 공백 제거
# 연산 + 출력
print(find_number(n)) # 30의 배수를 찾는 함수 이용해서 출력