'''문자열 인덱싱
print(type("안녕하세요"))를 실행했을 때
<class'str'> 나오는 것을 확인 할 수 있다.
str 이란 staring 줄임말로 줄이다

'''

# name = "ahhgunsu"
#
# # print(name[0])
# # print(name[1])
# # print(name[2])
# # print(name[3])
# # print(name[4])
#
# '''
# 마이너스 인젝스 : 문자열릐 뒤에서부터 부여하는 번호.  마지막 문자의 인덱스는  '-1'
#
# '''
# # print(name[-1])
# # print(name[-2])
# # print(name[-3])
# '''
# 문자열 슬라이싱; 문자열의 인덱스를 활용하여 한 문장 이상으로 구성된 단어나  문장을 추출할 때 사용
#
# 형식 :  a[시작 인덱스: 종ㄹ료 인덱스: 증감값]
# 시작 인덱스 : 생략하면 처음부터 추출
# 종료 인덱스 : 생략하면 끝까지 추출
# 증감값 : 생략하면 1 씩 변화(인덱스 넘버가 1씩 증가 0,1,2순으로)
#
# '''
# # print(name[:2:])
# #
# # b  = "banana"
# # print(b[:4:2])
# '''
#
# 4자리 숫자 입력 2024
# 4자리 마지막 자리의 숫자는 4
# '''
# num = input("네자리 숫자 입력하세요 >>> ")
# # last_num = num[-1]
# # last_num = int(last_num)
# last_num = int(num[-1])
# print(type(last_num))
# # print(f"맨 마지막 숫자는 {num[3]}입니다.") # 인덱스 넘버 사용
# # print(f"맨 마지막 숫자는 {num[-1]}입니다.") #마이너스 인덱스 사용
#
# if last_num  %  2 == 0:
#     print(f"맨 마지막 자리의 숫자는 {num[-1]}이고, 맨 마지막 자리의 숫자는 짝수입니다.")
# else:
#     print(f"맨 마지막 자리의  숫자는{num[-1]}이고, 맨 마지막 자리의 숫자는 홀수입니다.")
#


# n = input("차량 번호 237가1234를 입력하세요 >>>")
# last_n = int(n[-1])
# if last_n % 2 == 0:
#     print(f"차량번호{n}은 운행가능 합니다.")
# else:
#     print(f"차량번호 {n}은 운행불가입니다."
#     driving_possibility = "운행불가"
# print(f"차량번호 {n}은 {driving_possibility}입니다.")