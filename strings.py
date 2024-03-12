## Strings
'''문자는 하나의 칸을 가지고 리스트0부터 시작(다 아는 얘기)
'''

## ex1 
'''
>>>fruit = 'banana'
>>>letter = fruit[1]
>>>print(letter)
a
>>> x=3
>>> w=fruit[x-1]
>>> print(w)
n
>>>fruit = 'banana'
>>>print(len(fruit)) - len함수 : 문자열 길이를 알려준다
6
>>>fruit = 'banana'
>>>x=len(fruit)
>>>print(x)
6
'''

## ex2 while문과 for문을 이용해 문자열 출력
'''
fruit = 'banana'
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1
    
>>>
0 b
1 a
2 n
3 a
4 n
5 a
'''
'''
fruit = 'banana'
for letter in fruit :
    print(letter)   
    
>>>
b
a
n
a
n
a
'''