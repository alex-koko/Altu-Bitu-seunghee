#1205번
import sys
input = sys.stdin.readline

# 입력
n, n_score, p = input().split() # n_score는 태수의 점수
list = list(input().split())    # 점수들을 인풋받아서 리스트에 저장


# 풀이
grade = 1       # grade = 등수
num = len(list) # 리스트의 요소 개수를 num에 저장
list.sort(reverse = True) # 리스트를 내림차순으로 정렬

for i in range (1, num, 1):      # 처음부터 끝까지 반복하며 점수 비교할 것
    if ( list[i] != list[i-1] ): # 만약 직전의 점수와 다르면
        grade += 1               # 등수를 1 더한다
    else: 
        continue

    if ( n_score > list[i] ):    # 태수의 점수가 i번째 요소보다 크다면
        print(grade)             # i번째 요소의 등수를 출력한다 (태수의 점수가 그 자리에 들어가므로)

print(-1) # 조건에 해당하지 않은 경우 -1을 출력