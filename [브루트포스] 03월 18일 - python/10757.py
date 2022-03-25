import sys
input = sys.stdin.readline

"""
[큰수 A+B]
 1. 한 자릿수씩 더해서 리스트에 저장
 2. 한 자릿수씩 더할 때, 값이 10을 넘어가는 경우 고려 -> 자릿수 올림
 3. A와 B의 길이가 같지만, 둘의 합의 길이는 다른 경우 고려 -> 마지막 자리에서 올림
 4. A와 B의 길이가 다른 경우 고려 -> 더 긴 길이 처리 주의한다
 """

def calcPlus(a, b): # 큰 수 A, B를 더하는 함수
     # 항상 a가 b보다 자리수가 크다고 가정
     if len(a) < len(b): # 만약 a가 b보다 자리수가 작으면 
         a, b = b, a # a,b의 순서 바꿈
     ans = [0] * (len(a) + 1) # 정답 저장할 배열
     
     # -1, -2 ... 일의 자리부터 뒤에서 더하기 위해
     for i in range(-1, -len(b), -1): # 뒤에서부터(-1) len(b)의 자리수까지 더하기
         ans[i] += int(a[i]) + int(b[i]) # carry(올림) + a + b 
         ans[i-1] = ans[i] // 10 # 두 수의 합이 10을 넘는 경우 그 앞 자리수에 1 올림 
         ans[i] %= 10 # 해당 자리의 합이 10이 넘지 않도록, 나눈 나머지로 설정

     
     return int(''.join(map(str, ans))) #맨 앞자리 0이 출력되지 않도록 int() 적용




# 입력
a, b = input().split() #a, b를 각각 입력받음
# 연산 + 출력
print(calcPlus(a, b)) # 덧셈 연산을 처리하는 함수 출력