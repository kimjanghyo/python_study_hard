# print("hello, python!")


#  주석: 커퓨터가 릵는 부분이 아니라 사람이 읽을 수 있도록 정보를 제공하는 방법 주석 처리 된 부분은 파이썬이 인식하지 않음.

'''
다주 주석 처리

앞으로 우리가 필기하는 내용이 여러 줄일때 사용

1번 라인에서 hello, python! 분석
'''

from argparse import BooleanOptionalAction
from selectors import SelectSelector

# print("1")
# print(1)
# print("hello, python!")

# print(type("1"))            #<class 'str'>
# print(type(1))              #<class 'int'>
'''
type 차이에 따른 검증
'''
# print("1" + "2")            #결과값 12
# print(1+2)                  #결과값 3
#
# print("2" + "1")            #결과값 21 문자열이라 순서가 중요
# print(2+1)                  #결과값 3  정수라 상관 x

'''
print(): 컴퓨터에게 출력해 달라고 요청하는 명령어
type(): 소괄호 내에 들어가 데이터가 어떤 자료인지 표시하는 명령어, 주로 print() 함수와 합쳐 사용
str: 문자열
int: 정수
'''

# print("제 이름은 ㅇㅇㅇ입니다.")
# print("MBTI는 ㅇㅇㅇㅇ입니다.")

#print(
'''
이런 경우 엔터를 치게 되면 콘솔에서 엔터가 적용된 상태에서 작성이 가능함
'''

# pants_color = "검은색"
# last_food = "시리얼"
# status = "피곤함"
# print(f"입고 있는 바지 색 {pants_color}, 마지막으로 먹은 음식 {last_food}입니다. 그리고 현재 상태는 {status}입니다.")


#변수: 데이터를 저장하는 바구니
# 변수 명명 규칙
# 1. 변수는 소문자로만
# 2. 여러 단어가 합쳐진 변수는 "_"로 표시
# name 이라는 변수에는 여러분의 이름을 대입
# age 이라는 변수에는 여러분의 나이를 대입

# name = "KJH"
# age = "20"
#
# print(f" 이름은 {name}이고 나이는 {age}입니다.")

# print(name)
# print(age+1)        #변수에 정수가 있다면 수학적 연산이 가능합니다.

# b = 1           #결과 값 1
# print(b)
# b = b + 1       #결과 값 2
# print(b)

#코드는 순서대로 실행
'''
대입 연산자
1. = : = 오른 쪽에 있는 데이터를 = 완쪽애 있는 변수에 대입한다는 의미
변수에 처음 변수 이릅 대입하고 =  표시 뒤 넣고자 하는 데이터를 넣으면 됨

'''

'''
f-string : formatted string의 축약어로 str 내에서 변수를 불러올 수 있음
'''

# name = input("당신의 이름은 무엇인가요? >>>>")
# print(name)
# print(f"제 이름은 {name}입니다.")


