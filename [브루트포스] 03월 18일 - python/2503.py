import sys # 시스템 모듈 임포트
from itertools import permutations  # itertools 라이브러리로부터 permutation(순열)을 임포트한다.
input = sys.stdin.readline # 인풋 받을 것임
 
def count_strike_ball(s1, s2): #strike와 볼 수 리턴하는 함수
    # a가 답이라고 가정하고, b에 대한 스트라이크와 볼 수를 세서 리턴한다.
    strike = 0 # 일단 각각 0으로 설정
    ball = 0
    for i in range(3): # 세 자리이므로 세 번 반복 
        if s2[i] == s1[i]: # 위치와 숫자가 모두 맞으면
            strike += 1 # 스트라이크를 하나 더함
        elif s2[i] in s1: # 숫자는 있지만 위치가 다르면
            ball += 1 # 볼을 하나 더함

    return (strike, ball) # 스트라이크와 볼 수를 리턴함

def play_game(questions): # 게임을 하는 함수

    answer = 0 # 일단 리턴값을 0으로 둔다

    for i in range(123, 987 + 1): # 123부터 987+1 까지 반복하는데
        s1 = str(i) # i번째 항을 s1에 일단 넣어둠
        # 0은 포함되지 않으므로
        if '0' in s1: # 만약 0이 s1에 포함되어 있다면
            continue # 제끼고 다음으로 넘어감
        # 같은 수를 중복해서 사용할 수 없으므로 
        if s1[0] == s1[1] or s1[0] == s1[2] or s1[1] == s1[2]: # 같은 수가 있는 경우
            continue # 역시나 제끼고 넘어감 -> 다시 for반복문 수행

        answer += 1 # 0도 없고 중복되는 수도 없으면 정답 후보 +1

        for s2, count in questions:
            if count_strike_ball(s1, s2) != count: # 들어온 s,b 값이 count와 다르면
                answer -= 1 # 정답후보 -1
                break 

        return answer

def play_game_with_permutations(questions):
    digits = [str(i) for i in range(1, 10)] # i를 1부터 10보다 작을 때까지 반복

    answer = 0 # 답 저장할 곳

    for s1 in permutations(digits, 3): # s1에 대해서 digits에서 3개 선택
        answer += 1 # 정답후보+1
        for s2, count in questions: # 만약 주어진 s1, count에 대해서
            if count_strike_ball(s1, s2) != count: # 볼, 스트라이크 값이 다르면
                answer -= 1 # answer를 -1한다.
                break
    return answer




# 입력
n = int(input()) # n을 입력받는다 질문 몇 번 할지
# 세 자리 수는 string, 스트라이크와 볼 수는 int형으로 tuple로 묶어서 저장
initialize_input = lambda x: (x[0], (int(x[1]), int(x[2]))) # 세자리수와 스트라이크볼수를 입력받는다
questions = [initialize_input(input().split()) for _ in range(n)] # n번 인풋을 받는다

# 연산 + 출력
print(play_game_with_permutations(questions)) # 인풋받은 값을 함수로 보내서 계산한다