'''
문자열 indexing

print(type("안녕하세요"))실행했을떄,
<class'str>이라고 추력되는 것을 확인 할 수 있습니다.
str이란 sttring의 줄임말로 '줄'이라는 의미를 가지고 있음

index란 문장열을 구성하는 모든 요소애 부여한 고유한 번호
01234               시작 번호는 0
'''
from enum import EnumMeta
from traceback import print_tb

# name = "banana"
#
#
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])


'''
마이너스index 뒤에서 부터 시작

'''

# name = "tahw"
# print()
# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])

'''
문자열 슬라이싱 문자열 인덱스를ㄹ 활용하려 한 문자 이상으로구성된 단어나 문장을 추출 하고자 할때 상용하는 방법
추출하고자 하는 잔어나 문장의  시작 인덱스와




시작인덱스 : 생략하면 처음 부터 추출
종료 인덱스 : 생략하면 끝까지 추출
증감값: 생략 하면 1씩 증가


'''


# print(name[:2:])

'''
기본예제 

네자리 숫자를 받아 그 숫자 마지막 숫자를 출력하시오

네자리 숫자 2025
맨 마지막 숫자는 5입니다.

'''

# number = (input("네자리 숫자:"))
# num = int(input("네자리 숫자:"))
# if num % 2 == 0:
#     print(f"짝수입니다.")
# else:
#     print(f"짝수가 아닙니다")
# print(f"맨 마지막은 {number[3]}입니다.")


# num = input("네자리 숫자:")
# print(f"맨 마지막 숫자는 {num[3]}입니다")
# if int(num) % 2 == 0:
#     print(f" 맨 마지막 숫자는 {num[3]}이고 짝수 입니다.")
# else:
#     print(f" 맨 마지막 숫자는 {num[3]}이고 홀수 입니다.")


'''
미세먼지 저감 활동의 일환으로 차량 2부제를 실시

짝수로 끝나면 '운행가능' 아니면 '운행 불가' 
단 차량 번호는 '237가'1234

차량번호 입력 2371234
차량 운행 가능 

차량번호 입력 237가1234
차량 운행 불가능 
'''

num = (input("차량 번호:"))
print(num[6])
if int(num[6]) % 2 == 0:
    print(f"{num}운행 가능")
    even_odd = "운행 가능"
else:
    print(f"{num}운행 불가능")
    even_odd = "운행 불가"
print(f"차량번호는 {num}은 오늘 {even_odd}입니다")


