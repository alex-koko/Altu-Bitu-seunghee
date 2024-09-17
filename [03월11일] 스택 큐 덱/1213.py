import sys #import문을 이용해 sys모듈을 임포트한다. 

names = input() #names변수에 영어 이름을 입력받는다.
name_cnt = [ 0 for _ in range(26) ] #names_cnt에 영어 이름이 포함된 알파벳 대문자 수를 저장한다.
for name in names:
	name_cnt[ord(name)-65] += 1 #입력받은 이름의 각 알파벳 개수를 세아려 name_cnt 리스트에 담는다.

odd = 0 #홀수 알파벳 개수를 넣을 변수이다.
odd_alpha = '' #홀수 알파벳을 저장한다.
alpha = '' #짝수 알파벳을 저장한다.

for i in range(26):
	if name_cnt[i]%2 == 1: #name_cnt리스트를 돌면서 홀수인 경우  
		odd += 1#odd count를 1 올리고
		odd_alpha += chr(i+65) #odd_char에 해당 알파벳을 넣는다.
	alpha += chr(i+65) * (name_cnt[i] // 2) #짝수인 경우에는 answer에 갯수의 절반에 해당하는 알파벳을 넣는다.

if odd > 1: #홀수 갯수를 가진 알파벳이 2개 이상인 경우에는 팰린드롬을 구성할 수 없다.
	print("I'm Sorry Hansoo") #따라서 Hansoo에게 미안하다는 메시지를 출력한다.
else: #홀수 갯수가 1개 이하인 경우에는
	print(alpha + odd_alpha + alpha[::-1]) #짝수 알파벳의 절반, 홀수 알파벳을 출력한 후 짝수 알파벳 나머지 절반을 거꾸로 출력한다.