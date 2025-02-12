'''
컬렉션 여러 값을 하나의 이름으로 묶어서 관리하는 자료형


스트린의 경우 문자 하나 하나르 줄로 묶어 문자열로 출력하는데
예를 들어 다수으ㅏ 다른 스트링을 관리하는 방법
\


'''


#
# ahngeunsu = "이름 : kh\n나이 : 21\n 직업 : 학생"
# dkfjfk = "이름 : 김\n나이 : 22\n 직업: 머오ㅓ"
#
#
#
#
#
# print(ahngeunsu)
'''
 종류
 list 추가 수정 삭제가 언제나 가능 / a [1,2,3] 대괄호 사용
 tuple 추가 수정 삭제가 불가능 a = (1,2,3) 소괄호 사용
 set 중복된 값의 저장 불가능 ㅏa = {1,2,3}중괄호 사용
 dict 키 + 값으로 관리 a {"name" = "kjh", "age": 21} 중괄호 사용
 
1.리스트가 가장 많이 사용. 자형이 달라도 하나의 리스트에 저장가능 
  
 
'''

#
# list = [1,2,3,4,5, "tnqk" ]
# print(list)


'''
1-1 list의 인덱스와 slice
list는 str과 동일한 방식 iundex와 slicing을 지원함 
인덱스와 마이너스 인덱스
'''

# print(list[1])
# print(list[-1])

'''
slice
str의 슬라이싱과 같이 '시작 인덱스:종료인덱스:증감값'으로 이루어져 있음


'''



# list_num1 = [100, 3.14, "hello"]
# list_num2 = list( [4,5,6,7,8,9] )
# print(list_num1)
# print(list_num2[0:4:2])


'''
3)list에 요소의 추과와 삭제
list에 새ㅇ로운 요소를 추가할때 .append()와  . insert() '메서드'를 사용할 수 있습니다.
기존 요소를 삭제할때 .pop() 메서드를 사용합니다.

.append(): 항상 마지맛 인덱스에 요소를 추가하는 메서드
.insert(위치, 값) - 정해진 위치(인덱스)에 해당 값을 추가하는 메서드


'''


# scores = [30,40,50]       #scores라는 list내에 있는 int 데이터인 각각의 30, 40, 50
# print(scores)             #요소라고 합니다
# scores.append(100)        #함수와 달리 list명.메서드명의 형태로 사용됩니다
# print(scores)
# scores.insert(0, 90)
# print(scores)

'''
pop() 의 경우 빈 괄호로 사용하게 되며 맨 마지막 요소가 삭제됨 
pop(인덱스 넘버)로 작성 하면 해당 인덱스의 요소를 삭제함.


'''

# scores.pop()
# print(scores)
# scores.pop(0)
# print(scores)

'''
교제에 없ㄴ,ㄴ 삭제 메서드: .remove(값)을 사용하면 list  내에 없느,ㄴ 값을 찾아 삭제함
'''


# scores.remove(40)
# print(scores)
#이상의 코드를 실현 시킬떄 , 인덱스가 두 개 밖에 없어서 10갸 정도만 element를 추가하는 반복문 작성 한다


# for i in range(10):
#     scores.append(i*10)
# print(scores)
#
#
# for i in range(len(scores)):
#     print(scores[i])
#
#
#
# for score in scores:                #전에 말했던 것 처럼 cellection의 경우 복수로 이름을 짓고 향상된  for문에서  각 단수로 이름을
#     print(score)                    #짓는 경우가 많습니다


'''
2. tuple(): 저장된 값을 변경할 수 없는 list라고 생각하시면 됩니다. 인덱스와 슬라이스를 사용하지만 저장된 값  이외에는 추가/ 수전/ 삭제가 불가능


튜플은 소괄호를 통해 생성
'''



# tuple_num1 = (1,2,3)
# tuple_num2 = tuple((4,5,6))
# tuple_num3 = 7,8,9
# print(tuple_num1)
# print(tuple_num2)
# print(tuple_num3)
#복수의 변수 선언 및 초기화 방법 -> 첫 시간 때 함

a,b,c = 7,8,9
'''
튜플 생성 방법 3을 이용한다고 가정했을 때, 값이 하나 밖에 없는 튜플을 생성한다면
tuple_num4 = 0이라고 입력할 경우 생길 수 있는 문제는 무엇일까요?
'''
# tuple_num4 = 0
# print(tuple_num4)
# print(type(tuple_num4))
# tuple_num5 = 0,
# print(tuple_num5)
# print(type(tuple_num5))

'''
1)튜플에서 인덱스 / 마이너스 인덱스
'''

# tuple_num6 = 1,2,3,4,5,6,7,8,9,10
# print(type(tuple_num6[2]))
#collections의 element에 type() 함수를 적용하면, element의 자료형이 반환됨.
#즉,tuple_num6[2]는 3이라는 element를 가르키기 때문에 type() 함수 적용시 <class 'int'>로 출력됨


# tuple_num7 = "hello", " nice to meet you", "my name is ooo", "I am", "21", "have a nice day"
#
#
# for words in tuple_num7:
#     print(words.title(), end="")
#str_example = "jksjffdk"
#
#print(str_example.upper())
# print()
# for words in tuple_num7:
#     print(words.title(), end="") #words.title()를 적용 시켰다고 해서  튜플 내의 element들이 전부 값이 바뀐 상태가 유지되는 것이 아니라
#                                 # words.title() 이렇게 작성했을 떄만 메서드가 적용된 상태이기 때문에


'''
3. set
수학의 개념을 구현한 자료형.list와의 차이점은 순서가 없기 때문에(비시컨스) 인덱스 및 슬라이싱
set을 이용하기 위 중괄호 사용{}





'''

# set_num1 = {1,2,3}
# set_num2 = set({4,5,6})
# print(set_num1)
# print(set_num2)

# li = []
# tu = ()
# se = {}

# print(type(li))
# print(type(tu))
# print(type(se))

'''
se = {} 형태로 비어있는 set을 생성한 경우 se는 사실<c;ass'dict'>이기 떄문에 비어있는 se을 만들기 위해 세트 2번 방법을 사용

'''

# set2 = set({})
# print(type(set2)) #<class 'set'>
'''
특징
저장되는 순서가 없다. 인덱스 슬라이싱 불가
중복 값 저장 불가
특히 2. 특징으로 set 단독 보가 list어ㅏ 연계 사용이 자주 쓰임

'''
#
# list_num5 = [1,1,2,2,3,3]
# print(list_num5)
# list_num5 = set(list_num5)
#
# print(set_num5)
# list_num6
#
#
#
#
#
# set_num6 = {10,20,30}
# set_num6.add(50)
# print(set_num6)
# set_num6.remove(50)
# print(set_num6)
#
# set_num6.discard(70)

'''
4.dictionary - 말 그대로 의미 
flower - 꽃
dictionary - 사전
등으로 기재 즉 :을 기준으로 좌우측 나누어진 형태
딕셔너리는 리스트, 튜플, 세트와 달리
key: value의 구성으로 이루어져있음
'''

# dict_num1 = {
#     "이름": "ooo",
#     "나이" : 21,
#     "주소" : "ooooooooo",
# }
'''
key: value 형태 작성 대신 ","사용

직션는 인덱스는 존재하지 않지만 위와 같이 key를 인덱스와 유사하게 사용
즉 키 값을 알게 되면 저장된 값(value)확인 가능한 구조

'''

# li2 = [10, 20 ,30, 40]
# for num in li2:
#     print(num)
#
# for k in dict_num1:
#     print(k)
#     print(dict_num1[k])
#     print()
# #key 목록 추출하느 메소드
# print(dict_num1.keys())
# print(dict_num1.values())

# print(type(dict_num1.keys()))
# print(type(dict_num1.values()))

# keys = list(dict_num1.keys())
# values = list(dict_num1.values())

# print(keys[1])
# print(values[2])

'''
1)딕션 요소 추가와 삭제

'''

# dict_num1["직업"] = "학생"      #기존 key대신 value 사용
# print(dict_num1)
# dict_num1["직업"] = "학222생"     #하나의 key에 서로 다른 value를 저장할 수 없음
# key 하나 당 value는 하나여야만 한다
# print(dict_num1)
#삭제 방법
# dict_num1.pop("직업") #key 정확 하게 적어야 삭제 가능
# print(dict_num1)      #key 삭제하면 value도 같이 날아감

'''list [10,20,30,40,50,60,70,80,90.100]
의 3번째 요소 부터 7번쨰 요소만 추출한 결과, 그리고 그 list에서 2번째 요소를 출력하는 프로그램 작성

실행 예 요소부터 7번째 요소 = [30,40,50,60,70]
3~7번째 요소 중 2번쨰 = 40

'''
# last_origin = [10,20,30,40,50,60,70,80,90.100]
#
# print(f"3~7요소 = {last_origin[2:7:1]}")
# print(f"3~7요소 중 2요소 = {last_origin[2:7:1][1]}")
#
#
# list_sliced = last_origin[2:7:1]
# print(f"3~7요소 = {list_sliced}")
# print(f"3~7요소 중 2요소 = {list_sliced[1]}")





'''
사용자로 부터 1~12 사이의 월일 입력 받아 출력하는 프로그램

1~12사이의 월 

'''

# month = input("1~12:")
# month_int = int(month)
#
# last_dates = [31,28,31,30,31,30,31,31,30,31,30,31]
# print(f"{month_int}월은 {last_dates[month_int-1]}일 까지 있습니다")
# last_dates_short = [28,30,31]
# last_dates_dict = {
#     "1": 31,
#     "2": 28,
#     "3": 31, "4": 30, "5": 31, "6":30, "7": 31, "8": 31, "9": 30, "10": 31, "11": 30
#     , "12": 31,
# }
#
# print(f"{month}월 {last_dates_dict[month]}까지")
# last_dates_short = [28,30,31]
#
# if month_int == 2:
#     last_date = last_dates_short[0]
# elif month_int == 4 or month_int == 6 or month_int == 9 or month_int == 11:
#     last_date = last_dates_short[1]
# elif month_int in [1,3,5,7,8,10,12]:                  #in뒤에 collection 중 하나가 오면 됨 (),[].{} 가능
#     last_date = last_dates_short[2]
# else:
#     print("잘못 입력함")
#     last_date = "x"
# print(f"{month}월 {last_date}까지")




'''
수학 여행을 어디로 갈지 결정하기 위해 학생들이 희망한는 모든 수학여행 장소 조사
학생들이 원하는 장소 입력받아 동일한 입력은 무시하고 모든 입력 저장 
학생은 3명으로 가정 



희망하는 수학여행지 입력 제주
희망하는 수학 여행지 제주
''          민속촌


조사된 수학여행지는 {제주,민속촌}
조사된 수학 여행지는 [제주, 민소촌]
'''


# want_palce_list = []
# want_palce_set = set({})
#
# for student in range(3):
#     student = input("희망하는 수학여행지:")
#     want_palce_list.append(student)
#     want_palce_set.add(student)
# #     want_palce_list = [student]     #번복문 사용 x
#
# want_palce_set = set(want_palce_list)
# print(f"조사된 여행지는 {want_palce_list}입니다")
# print(f"조사된 여행지는 {list(want_palce_set)}입니다.")



'''
짝수만 추출

사용자로부터 양의 정수만 입력 받고 그 수를 저장 후 짝수만 새 리스트 저장 출력하는 ㅠㅡ로그램

몇개 숫자 입력 5
1번째 : 10
2번쨰 : 15
3 : 20
4: 25
5: 30
입력받은 숫자는 [5,10,15,20,25,30]
입력 짝수 [10,20,30]
'''
# all_num = []
# n_num= []
#
# number = int(input(":"))
# for i in range(number):
#     num = int(input(f"{i+1}숫자 입력:"))
#     all_num.append(num)
#
#
# print(f"모든 숫자는 {all_num}")
# print(f"모든 숫자는 {list(n_num)}")
#
# for num in all_num:
#     if num % 2 == 0:
#         n_num.append(num)
# print(f"입력받은 숫자 중 짝수는 {n_num}입니다")

#
# li_or = []
# li_de = []
# for i in range(int(input(":"))):
#     num = int(input(f"{i + 1}숫자 입력:"))
#     li_or.qppend(num)
#     if num % 2 == 0:
#         li_de.append(num)
# print(f"모든 숫자는 {li_or}")
# print(f"모든 숫자는 {li_de}")

'''
사용자 3명 이믈 전화번호 받아 딕션너리 저장 입력 정보 추출
1 사람 이름 : 김일
1사람 연락 
2 사람 이름 : 
2 사람 연락 0
3 사람 이름 
3 사람 연락
'''

#
# dict_num = {}
# for i in range(3):
#     dict_key = input(f"{i+1}:")
#     dict_value = input(f"{i+1}:")
#     dict_num[dict_key] = dict_value
# print(f"입력받은 연락처는 {dict_num}")
# {'김일':'010-1234-5678', '김정':'010-1234-1234','윤석':'010-4567-4567'}




'''
list01선언
add_numbers()
정수 n

add_nunmbers(last_num)

숫자 : 10
[1,2,3,4,5,6,7,8,9,10]
'''
# def add_numbers(n):
#     list01 = []
#     for i in range(n):
#         list01.append(i+1)
#     print(list01)
# def add_number2(n):
#     list2= []
#     for i in range(n):
#         list2.append(i+1)
#     return list2
# last_number = int(input(":"))
# add_numbers(last_number)
# print(add_number2(last_number))

# for number in add_number2(last_number):
#     print(number+1)
#
#
# for number in add_numbers(last_number):
#     print(number+1)


'''
짝수 홀수 개수 세기
짝수 홀수 세는 함수 list에적어 

이름 count_even_odd
매개 list_number

count_even_odd([1,2,3,4,5,6,7,8,9,10])

짝5
홀5
'''




#
# def count_even_odd(numbers):
#
#     even_count = 0
#     odd_count = 0
#     for number in numbers:
#         if number % 2 == 0:
#         even_count += 1
#         else:
#         odd_count += 1
#     print(f"짝:{evem_count}\n의 홀:{odd_count}") \
# count_even_odd = [1,2,3,4,5,6,7,8,9,10]


# import calendar
#
# def print_calendar(year):
#     for month in range(1,13):
#         print(calendar.month_name[month])
#         print(calendar.month(year, month))
#
#     print_calendar(2024)
# #
scores = {
    "mike": 99, "miku":60,",oke": 22

}

max_student = max(scores.items(), key= lambda x:[1])
min_student = min(scores.items(), key= lambda x:[1])

print(f"최고 득점은 {max_student[0]}, {max_student[1]}")
print(f"최소 득점은 {min_student[0], min_student[1]}")