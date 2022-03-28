import sys # sys 모듈 임포트
input = sys.stdin.readline # 인풋 이렇게 받을 것임
 
def get_size(r, b): # r과 b의 가로 세로 길이를 함수
    area = r + b # r과 b를 더한 값이 넓이임 
    # l > w이므로 w을 작은 것부터 탐색해서 정답이 되는 경우 리턴
    for w in range(1, r+b+1): # 작은 값인 w에 대해 1부터 r+b보다 작을 때까지
        if area % w != 0: # 넓이가 w로 나눠 떨어지지 않으면
            continue # 답이 아니므로 for문으로 돌아감
        l = area // w # 만약 나누ㅓ 떨어지면 l의 값을 정할 수 있다
        if r == (l + w) * 2 - 4: # 만약 r의 값이 l,w을 이용해 계산한 넓이와 같으면
            return l, w # l,w가 정답이 됨

# 입력
r,b = map(int, input().split()) # 빨간색, 갈색 타일 수를 인풋받음
# 출력
print(*get_size(r, b)) # 인지에 *을 붙이면, 뒤의 객체를 풀어서 하나씩 넣어준다