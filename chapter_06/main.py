'''
1.함수 : 특정 작업을 수행하는 코드 블록을 정의ㅡ하는 방법

예를 들어 사진을 찍ㄱ는다로 생각하면
1)주머니에서 폰을 꺼낸다
2)잠금을 푼다
3)카메라를 킨다
4)사진을 찍고자 하는 대상을 선정하고 조준한다
5)사진을 찍는다

컴퓨터는 시키는대로만 하기에 1~5의 명령어를 입력한다

명령어를  미리 입력하면 사진을 찍는다를 입력하면 자동으로 수행한다
이것을 함수의 개념이라 할 수 있다.


함수의 정의 형식
turn_left
turn_left
turn_left


함수 호출 형식
turn_right


2함수의 종류
파이썬 내장 함수
메서드
사용자의 정의 함수


3 함수 용어 정리
1) 함수 정의: 사용자 함수를 새로 만드는 것을 의미
2)인수: 함수에 전달하는 입렵값
3)매개변수 : 인수를 밪아서 저장한는 변수
4) 변화값/ 결과값/ 리턴값: 함수의 출력값
5)함수 호출 : 함수를 실제로 사용하는 것을 의미

4.(사용자) 함수의 형식:
def 함수 이름(매개변수):
실행문

변수 = 함수_이름
'''
# def write_name(name):                               #정의 할떄 소괄호 내에 있는 것을 parameter라고 합니다.
#     print(f"당신의 이름은 {name}입니다")
#
# write_name("kjh")                                   #호출할떄 소괄호 내에 있는 것을 argument라고 합니다.
#
#
#
# def write_name_age(name, age):
#     print(f"당신의 이름은 {name} 이고 나이는 {age}입니다.")
#
# write_name_age("kjh", 21)
# write_name_age(age= 21, name= "kjh")


'''
우리가 에를 들어 input("이름을 입력하세요 >>> ")이용해서 이것을 name이라는 변수에 담았다고 가정하면 
name = input("이름을 입력하세요 >>> ")이라고 작성 했습니다.
즉, 저희는 이때까지 함수의 결과값을 변수레 담아오고 있었습니다.
파이썬은 내장 ㅎ함수는 이미 함수가 정의돼있고, 개발자들은 함수 호출만 잘 하면 됩니다
사용자 함구는 개발자 자신이 함구를 정의하고 그 후 호출하는 것까지의 좌정

2. 메서드: 특정 객체가 가지고 있는 함수를 의미 특정 자료형에 포함되어 있는 함수 
사실 ㅎ마수와 메서드는 동일한 개념이지만 호출 방식이 차이가 있음

함수는 독립적으로 사용 가능 / 메서드는 특정 객체

'''

# eng_name = input("당신의 이름을 소문자로:").upper()
# print(eng_name)
# eng_name2 = input("당신의 이름을 소문자로 입력:").title()
# print(eng_name2)


'''
함수(메서드)의 유형
'''
# def call1():
#     print("[x | x]")
#
# def call2(str_type):
#     print("[o | x")
#     print(f"{str_type}이라 입력")
#
# def call3():
#     print("[x | o]")
#     return 1
# def call4(str_type):
#     print("[x | o]")
#     return f"제 이름은 {str_type}입니다"
#
#
# call1()
# call2("춥당")
# call3()
# print(call3())
# print(call3() + 1)
#
#
# new_element = (call3() +3) * 10
# print(new_element)
#
#
# call4("kjh")
# print(call4("kjh"))





'''
call3/ call4 유형에서 함수내에 print를 집어 넣어도 main단계에서(들여쓰가 되어있지 않은 상태)
print 함수를 입력할 필요 없이 훌 편할 텐데
왜 return형태로 입력해서 main에 ptint를 적어 일일이 적용해야 하는가









'''





# def introduce(name, address):
#     return f"제이름은 {name} and, live in {address}"
#
# name = input("name is:")
# address = input("home:")
#
#
# print(introduce(name, address))

'''
700우너 짜리 음ㄹ료수를 뽑을 수 았는 자판기 프로그램을 구하시오 존을 넣으면 몇잔의 음료수를 뽑을 수 있는지 그리고  잔돈은 얼마나인지 경우의 수를 구하시오

합수 정의 
반환값 없음 
함수 이름 vending_machine()
매개변수 정수 money

코드 구성

def vending_machine():

vending_machine(3000)


음ㄹ료수 = 0개 잔돈 3000우너
뭉료수 = 1 개 잔돈 2300우너
믈료수 = 2 개 잔돈 1600원
음료수 = 3개 잔돈 900원
음료수 = 4개 잔돈 200원




'''
#
# def vending_machine():
#     pass
#
#
# my_money = 3000
# drink_price = 700


# charge = 3000 - (700 * "음료수 개수:")

# for i in range(my_money//drink_price + 1):
#     print(f"음료수 = {i}개, 잔돈 = {my_money - (drink_price*i)}")





# def vending_machine(money):
#     for i in range(money// 700 + 1):
#         print(f"음료수 = {i}개, 잔돈 = {money - (700 * i)}")
#
# vending_machine(3000)


'''
예제 구구단  풀력하기

함수 정의 :
함수 이름 multiply
매개변수: 정수 n 

함수 호출 multply(dan)

몇 단을 출력하시겠습니까? >>> 3


'''

# def muliply(n):
#     for i in range(1, 10 ,1):
#         print(f"{n} x {i} = {n*i}")
# multiply2():
#   dan = int(input("몇 단을 출력:"))
#   for i in range(1, 10 ,1):
#       print(f"{dan} x {i} = {dan*i}")
#
#
#
# muliply(4)




# # print(dan)
# # dan = 3
# # print(dan)
# i = 3

