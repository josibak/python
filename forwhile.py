"""while문 if문과 비슷하게 작동 첫 질문에 T/F로 false가 나올때까지 작동?
"""
'''
<무한 루프>
n=5
while n>0 :
    print('lather')
    print('rinse')
print('day off')
'''

'''
# done을 입력하면 while문이 True로 종료 done! 출력
while True :
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('done!')
'''

# 밑의 line[0]구문은 #표시로 시작하는 input값을 넣을 경우 출력값에 주석을 남기는 용으로 continue를 사용
# 음... 쫌 더 사용해 봐야 될듯
# break는 구문을 끝내는 대신, continue는 반복문의 처음으로 돌아가 계속해서 실행한다는 차이점 이해
# 밑의 구문은 break를 통해 빠져나올 수 있는 무한루프구문
'''
while True :
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('done!')
'''



## 유한루프     
## 예제
'''
for i in [1, 2, 3, 4, 5] :
    print(i)
print('blashoff!')

friends = ['sihyun', 'jo', 'hyun']
for friend in friends :
    print("hello my friend",friend)
print("done")
'''


## 불리안 변수 : True, False 두개의 값을 가짐
## None 타입변수 : 말 그대로 None
## 예제
'''
found = False
print('before', found)
for value in [1, 2, 3, 4, 5] :
    if value == 3 :
        found = True
    else :
        found = False
    print(found, value)
print('after', found)
'''

## 제일 큰 값 찾기
'''
largest_so_far = -1
print('before', largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('after', largest_so_far)
'''
## is와 is not
## is는 == 와 비슷한 기능
## 0 == 0.0(True), but 0 is 0.(False) 즉, is는 == 보다 강한 의미를 가짐 => 자료형과 값 모두의 동등성이 요구
## 보통 is는 불리언(True, False)혹은 None을 대할때만 쓰는게 좋음

