import sys # 시스템 모듈 임포트
from itertools import combinations # itertools로부터 조합 임포트
input = sys.stdin.readline # 인풋하려고

def play_blackjack(n, m, cards): # 조합 없이 풀기
    cards.sort() # 오름차순 정렬
    answer = 0 # 리턴 변수

    for i in range(n): # 3중 for문 이용해서 각 카드의 값의 합을 구함
        for j in range(i+1, n): # 오름차순 정렬했으니 앞에서부터 카드 선택하면
            for k in range(j+1, n): # 작은 값부터 더할 수 있음
                temp = cards[i] + cards[j] + cards[k] # 세 수를 더함
                if (temp > m): # 더한 값이 m을 초과하면
                    break # 다음 값 
                answer = max(answer, temp) # 최댓값 갱신
    return answer # 최대값 answer를 리턴


def play_blackjack_with_combinations(n, m, cards): # 조합 이용해서 풀기
    combi = combinations(cards, 3) # cards에서 3개로 이루어진 조합 구함
    arr = list(map(lambda x: sum(x), combi)) # 모든 조합에 대해 합 구하기
    arr.sort() # 오름차순 정렬

    answer = 0
    for total in arr: # arr에서
        if total > m:   # 합이 m 넘어갈시 
            break # 끝냄
        answer = total # 가장 큰 값을 answer에 저장

    return answer # 리턴





# 입력
n, m = map(int, input().split())
cards = list(int, input().split())

print(play_blackjack(n, m, cards))
# print(play_blackjack_with_combinations(n, m, cards))