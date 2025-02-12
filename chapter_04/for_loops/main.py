'''
for반복문
정해진 구간 혹은 집합 내의 요소들을 순서대로 꺼내어 반복 작업 수행

예를 들어 문자열을 인덱스 개념을 학습합니다
string의 경우 문자열의 문자 개수만큼 반복 진행된다고 해석 할 수 있습니다.
collection을 기반으로 반복문을 배울 수도 있지만 이건 다음 시간


    1) 숫자 법위 이용한 반복
        range() : 몇번반복 할 것인가 지정하는 함수


'''

# n = 1
# while n < 11:
#     print(n)
#     n += 1
# for i in range(11):
#     print(i)
#
# print()
#
# for i in range(10):
#     print(i+1)


'''
range() 함수의 응용
    range( (시작값),종료값, (증감값) )
    시작값: 생략 가능, 생략 할 경우 0부터
    종료값: 명시 하지 않으면 끝까지 진행 
    증감값: 생략 가능, 생략 할 경우 1씩 증가
    
    
    
    
    
    
    for 반복문 
    형식 
    for i in range:
    

'''
# for i in range(1, 11, 1):
#     print(i)



'''
문자열 사용 방법
문자열 사용하는 경우[]를 통해  내부에 인덱스 넘버를 명시 할 수 있다
그래서 in range()를 사용하는 방법 및 향산된 for문을 사용하는 방법을 통해 문자를 하나씩 추출 가능
'''


# name = "watermelon"
# for i in range(len(name)):
#     print(name[i])
#
#
# for letter in name:     #name이라는 string에서 각 문자 하나씩 뽑아 letter에 대입함
#     print(letter)
# #첫 번째 반복
# letter = name[0]
# print(letter)
# #두번째 반복
# letter = name[1]
# print(letter)
# ...
# letter = name[9]
# print(letter)
#


'''
대부분의 경우 반복문을 사용하게 되면 대상이 된는 객체는 복수형의 변수명을 지닙니다
numbers = [1,2,3,4,5]

for number in numbers:
print(number)


for loop 형식:
for 변수 in 반복대상객체:
반복 실행문 

반복대상객체: 내부에 요소가 다수 들어가



주의 상황

들여쓰기 주의
 
'''
# count_a = 0
# count_letter = "banana"
# for letter in "banana":
#     if letter == "a":
#         count_a += 1
#         print(letter)
# print(f"의 개수 : {count_a}")
# print(f"전체의 개수 : {count_letter}")
# print(f"전체의 개수 : {count_letter}")
# print(f"전체의 개수 : {len("banana")}")


# def turn_right():
#     for _ in range(3):
#         turn_left()
#
#
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
# for _ in range(6):
#     jump()
#
#
# def pause():
#     at_goal()
#


# def turn_right():
#     for _ in range(3):
#         turn_left()
#
#
# def jump():
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
#     if wall_in_front():
#         jump()
#     else:
#         move()

# huddle_4 내 코드
# def turn_right():
#     for _ in range(3):
#         turn_left()
#
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     while right_is_clear():
#         turn_right()
#         move()
#         turn_right()
#         move()
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





# huddle_4 선생님 코드
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
#     turn_right()
#     move()
#     turn_right()
#     while not wall_in_front():
#         move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()


# def turn_right():
#     for _ in range(3):
#         turn_left()
# while not at_goal():
#     if wall_on_right() and front_is_clear():
#         move()
#     elif wall_on_right() and wall_in_front():
#         turn_left()
#     elif right_is_clear():
#         turn_right()
#         move()

#(2.4)일떄 안 됨