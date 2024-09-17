from collections import deque #collections 로부터 deque을 임포트한다.
import sys #import문을 이용해 sys모듈을 임포트한다. 

N, K = map(int, sys.stdin.readline().split()) #N,K를 입력받는다 
queue = deque([i for i in range(1, N + 1)]) #rotate()함수를 이용하기 위해 deque을 선언
result = ['<'] #

while True :
    queue.rotate(-K) #왼쪽으로 k만큼 이동하기
    if len(queue) > 1 : #k번재 사람을 pop으로 제거
        result.append(str(queue.pop()) + ', ' )
    
    elif len(queue) == 1 : #queue의 크기가 1인 경우
        result.append(str(queue.pop()) + '>') #>가 붙어서 나옴
        break

result = ''.join(result) #join 이용해서 합치기
print(result) #합쳐진 문자열 출력
