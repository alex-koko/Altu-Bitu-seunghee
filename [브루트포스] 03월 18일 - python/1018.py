﻿import sys
input = sys.stdin.readline

"""
[체스판 다시 칠하기]
- 나올 수 있는 체스판의 경우: 2가지
    -(0,0)이 검정인 경우, 흰색인 경우
    -검정으로 시작하는 체스판의 경우, 인덱스 i+j가 짝수일 때 'B'임을 이용
1. (0,0) 인덱스부터 차례로 8*8 체스판 만들 때 바꿔야 하는 칸 수를 계산하고, 그 중 최솟값 구한다

보드 크기 <= 2,500
한 위치에 대한 체스판 비교 연산 = 64번
총 연산 수 = 2,5-- * 64 < 1억 -> 브루트 포스 가능
"""
SIZE = 64 # 체스판 크기 지정

# (x,y)에서 시작하는 8*8 체스판을 만드는데 필요한 최소 카운트 리턴
# 검정으로 시작하는 체스판을 기준으로 계산(b_count) ->절반(32) 이상이면 흰색으로 시작하는 체스판
def count_change(x, y, board): # 카운트 세는 함수, 인자는 x, y, board
    b_count = 0 # 카운트 셀 변수

    for i in range(8): # 중첩 for문 사용
        for j in range(8): # i, j
            # 검정으로 시작하는 경우, i+j가 짝수일 때 검정, 아니면 흰색
            if (i+j) % 2 == 0 and board[x+i][y+j] != 'B': # 짝수인데 흰색으로 칠해져 있는 경우
                b_count += 1 # b_count를 더한다
            elif (i+j) %2 == 1 and board[x+i][y+j] != 'W': # 홀수인데 검정으로 칠해져 있는 경우
                b_count += 1 # b_count를 더한다

        # 최솟값 리턴
        if b_count > SIZE//2: # 만약 b_count가 32를 넘으면
            return SIZE - b_count # 흰색 체스판 시작 카운트
        return b_count # 검정색 시작 체스판 카운트

    # 입력
    n, m = map(int, input().split()) # 인풋을 맵으로 받는다
    board = [input().rstrip() for _ in range(n)] # 체스보드 입력 받음
    answer = SIZE # 최대값으로 초기화

    for i in range(n - 8 + 1): # i,j 입력받기
        for j in range(m = 8 + 1): 
            answer = min(answer, count_change(i, j, board)) # 최소 변경하는 경우 계산

    print(answer)