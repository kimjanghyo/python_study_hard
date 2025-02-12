'''
for 반복문의 기본개념 반복 작업을 수행
staring 의 index개념. string의 경우네는 문잔의 개수만큼 반복 진행되다고 해석할 수 있습니다.
사실 collectionsㄹ를 기준으로

숫자 범위를 ㅣ 이용한 반복
range() : 몇번잉나 반복할 것인가 지점하는함수 for문과 자주 사용
'''
from itertools import count
from logging import lastResort

# for i in range(5):
#     print(i)
# sum =0
# for o in range(11)
#      sum += i
#
# print(f"1부터 10까지의 합 : {sum}")

'''
rangee() 함수의  응용:
range(시작값,종료값, 증감값)
    시작 값 : 셍략가능
    종ㄹ료 값  :명시하지 않으면끝까지 진행
    증감값 :생략가능, 생략할 경우 1씩증가

'''

# for i in range(1, 10, 1):
#     print(i)
'''
    문자열을 잉용하누 반복 
    문자열의 경우[]를 통해 내부에 인덱스를 명시할수 있다는 것과 진난 시간에 배움
    슿래서 IN RANGE()를 상용하는 방법봐
    향상된 FOR문을 상요하는 방법으로 문장를 하나씩 추출  할 수
    있다)
'''
# str_example =  "hello"
# for i in range(5)
#  for i in range(len(str_example)):
#     print(str_example[i])

# print(str_example[0])
# print(str_example(1))
# print(str_example(2))

# for letter in str_example:
#     print(letter)

'''
     for반문의 형식:
     
     for변수 in 반복대상객체
        반봇 수행문
        
        반복대상객체(iterable) : 내부에 요소가 가수 글어ㅓ가 반봇걱으로 요소의 데이터를 다룰수있는 객체
ex)str, list, tuple, set , dict --> str만 배움

주의사황
if 조건문과 마찬가지로 들려쓰기가 매우 중요함
프로그램에 따라서 탭을 한 번 누른 것이 들여쓰기 범위로 설정됨
스페이스바기준2번과4번경우나뉨

문자열에서  특정 문자 개수 세기 
'''

# count_a = 0
#
# for letter in "banana":
#     if letter == "a":
#         count_a += 1
#         print(letter)       # a
#     print(letter)           #b a n a n a
# print(f"a의 개수 : {count_a}")

# 1단계
# def turn_right():
#     for _ in range(3):
#         turn_left()
#
#
# for _ in range(6):
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# #
# #
# turn_right():
# for _ in range(3):
#     turn_left()
# #
# # 2단계
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# while not at_goal():
# #     jump()
#
#
# def turn_right():
#     for _ in range(3):
#         turn_left()
#
#
# def jump():
#     turn_left()
#
#     move()
#
#     turn_right()
#     move()
#     turn_right()
#
#     move()
#
#     turn_left()
#
#
# while not at_goal():
#     while front_is_clear():
#         move()
#     jump()
#
#
#
#
# def turn_right():
#     for _ in range(3):
#         turn_left()
#
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#
#     turn_left()
#
#
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         jump()
#
