import sys                 # 시스템 모듈
input = sys.stdin.readline # 여러개 입력 받을 것

last_digit = [[i] for i in range(10)] # 0부터 9까지의 패턴
size = [] # 패턴의 길이

for i in range(10): # 10번 반복
    temp = i # i를 temp에 저장
    while i != (temp * i) % 10: # i가 temp*i를 10으로 나눈 나머지와 다른 경우
        temp *= i # temp에 i를 곱한다
        temp %= 10 # temp를 10으로 나눈 나머지 구하기
        last_digit[i].append(temp) # i의 마지막 자리에 temp를 더함
    size.append(len(last_digit[i])) # last digit의 길이를 size에 더함 

# 입력
t = int(input()) # 정수 t 입력

# 입력 + 연산
for _ in range(t): # t번 반복
    a, b = map(int, input().split()) # 두 수를 입력 받아서 각각 a,b에 저장
    a %= 10 # a를 10으로 나눈 나머지를 a에 저장

    if a == 0: # 만약 a가 0이면
        print(10) # 10번째 컴퓨터가 출력(예외처리)
        continue # 조건문을 빠져나간다

    print(last_digit[a][b%size[a] - 1])  # 함수 프린트