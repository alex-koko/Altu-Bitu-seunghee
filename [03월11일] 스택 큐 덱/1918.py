text = input() #입력
answer = '' #결과 출력용
stack = [] # 연산자 관리용

for t in text : #입력받은 것에서 t 가져오기
    if t.isalpha() : #t가 알파벳이면 
        answer += t #결과값 문자열에 더하기 
    else :
        if t == '(' : #t가 (이면 
            stack.append(t) #스택에 저장 
        elif t == '*' or t == '/' : #*,/는 추가 전에 존재하는*,/을 pop하여서 저장
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                answer += stack.pop()
            stack.append(t)
        elif t == '+' or t == '-' : #+,-는 
            while stack and stack[-1] != '(' : #추가 전에 존재하는 ( 직전까지의 값 
                answer += stack.pop() #모두 Pop,저장
            stack.append(t)
        elif t == ')' : #)는 stack에 존재하는 (직전까지의 값을 
            while stack and stack[-1] != '(' :
                answer += stack.pop() #모두 Pop하여 결과값에 저장 
            stack.pop() # '('를 빼는 작업

while stack :
    answer += stack.pop() #결과값 출력

print(answer) 