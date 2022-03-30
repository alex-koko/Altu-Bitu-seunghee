# 15663번
import sys
from itertools import combinations # 조합을 이용해서 문제를 해결할 것
input = sys.stdin.readline


# 입력
n, m = input().split() # n, m을 입력받음
numli = set(input().split()) # n개의 수가 주어지면 그 수를 집합(set)에 저장


# 연산 + 출력
a = list(combinations(numli, m)) # 집합 중에 m개의 원소를 선택해서 저장한 것의 리스트 생성
print(list(a)) # 리스트 출력