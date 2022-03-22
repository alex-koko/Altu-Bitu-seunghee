import sys # 시스템 모듈을 임포트한다. 
input = sys.stdin.readline # input()으로 입력받을 수도 있지만, 그러면 시간초과됨

"""
[백대열]
- n과 m의 최대공약수를 찾아서 나눠준다.
"""

def calc_gcd(a, b): 
    # a > b일 때, a와 b의 최대공약수를 리턴
    if b == 0: # b가 0인 경우
        return a # 0과 어떤 수의 gcd는 그 수임 (0에 어떤 수를 곱해도 0이므로 0은 모든 수를 약수로 가진다.)
    return calc_gcd(b, a % b) # 유클리드 호제법을 이용해서 gcd를 구한다

# 입력
n, m = map(int, input().split(':')) # ':' 기준으로 나누기

# 연산 + 출력
gcd = calc_gcd(max(n, m), min(n, m)) # 두 수를 (큰 수, 작은 수)로 정렬해서 gcd 계산
# / 로 계산하면 1.0 과 같이 소수점이 표기되므로 주의
print(n // gcd, ':', m // gcd, sep='') # gcd로 나눈 값을 출력한다