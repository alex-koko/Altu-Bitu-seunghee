#백준 18115 카드놓기/ 덱(deque)을 이용하는 문제

from sys import stdin #표준 입출력을 임포트한다.
from collections import deque #덱을 임포트한다.
N = int(stdin.readline()) #n을 입력받을 것이다.
card = list(map(int, stdin.readline().split())) 

result = deque() #결과를 덱에 저장한다.

for i in range(N): #n번 반복하는데
    if card[N-i-1] == 1: #첫번째 룰은 가장 위의 카드를 내려놓는 것 
        result.appendleft(i+1) #역으로 해당 카드를 맨 위에 쌓는다.
    elif card[N-i-1] == 2: #2번째 룰은 위에서 두번째에 있는 카드를 내려 놓는 것
        result.insert(1,i+1) #역으로 해당카드를 첫번째에 위치시킨다.
    elif card[N-i-1] == 3: #3번째 룰은 제일 밑의 카드를 내려 놓는 것
        result.append(i+1) #역으로 가장 마지막에 위치시킨다.

print(*result) #값만 출력하기 위해 덱 앞에 *를 붙여준다.

