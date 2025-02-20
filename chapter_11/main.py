'''
클래스 변수

인스턴스 변수 : 인스턴스마다 서로 다른 값을 지니느 변수
클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수

인스턴스 변수:
목적 - 인스턴스 마다 서로다른 값을 저장
-클래스 접근(x)

클래스 변수:
목적 - 인스턴스가 공유하는 값을 저장
접근 방식 - 인스턴스 접근 가능
클래스 접근 가능


'''
from itertools import count

# class Korean:
#     country = "한국"
#     def __init__(self,name,age,address):
#         self.name =name
#         self.age = age
#         self.address =address
#
#
# man = Korean("kjh", 21, "Busan")
# print(man.name)
# print(man.age)
# print(man.address)
# print(man.country)
# print(Korean.country)

'''
객체명.클래스 변수를 통해 클래스 변수에 접근이 가능 하지만 클래스 내부의 코드를 들여다 보기 전까지 country 라는 변수가 클래스 인지 인스턴스 변수 인지 확인이 불가능 하다는 문제가 존재
이상의 이유로 클래스 변수를 확인 하고자 할떄는 객체명.클래스 변수명 으로 참조 하기 보다는 클래스. 클래스 변수 명을 통해 참조 하는 것이 바람직하다.
'''
'''
클래스 메서드 : 클래스 변수를 사용하는 변수

'''
# class Korean2:
#     country = "대한민국"
#
#     @classmethod
#     def trip(cls, travelling_site): #self가 아닌 cls가 작동
#         if cls.country == travelling_site:
#             print("국내 여행 입니다.")
#         else:
#             print("해외 여행입니다.")
#
# Korean2.trip("대한민국")
# Korean2.trip("미국")
#
# man2 = Korean2()
# man2.trip("일본")
# 인스턴스인지 메서드인지 구분할 수 없어 권장하지 않음


'''
클래스 메서드
클래스 변수를 사용하는 메서드 
인스턴스 또는 클레스로 호출 하지만 클래스 변수와 마찬가지로 클래스 호출하는 것이 권장
생성된 인스턴스가 없어도 호출 가능 
@classmethod 데코레이터(decorator)를 표기하고 작성
매개변수 self를 쓰지 암ㄶ고 cls를 사용 셀프는 개체르르의미하기 때문에 인스턴스에 사용

호출 방식 
클래스명.메서드명() -> 셀프를 사용하지 않기에 인스턴스 변ㅅ에 접근이 불가
cls를 통해 클래스 변수 접근 가능

정적 메서드 
정적 메서드 또한 셀프 사용하지 않기 떄문에 인스턴스 변수에 접근하여 사용하는 것이 불가 
클래스 메서드와의 공통점
인스턴스 생성하지 않고 사용 가능 클래스 메서드와의 공통점 2


특징 
인스턴스 또는 클래스로 호출이 가능 클래스 메서드와의 공통점

'''
# class Korean3:
#     country = "한국"
#     @staticmethod
#     def slogan():
#         print("Imagine Your Korea")
#     @staticmethod
#     def slogan2(str_example):
#         print("Imagine Your Korea" + str_example)
#
# Korean3.slogan()
# Korean3.slogan2("근데 너무 춥다")



'''
기본 예제 

가방을 만들때 마다 현재 만들어진 가방이 몇개인지 계산 할 수 있는 bag 클래스를 정의 합니다

'''

# class Bag:
#
#     count = 0
#
#     def __init__(self):
#         Bag.count += 1
#         print({"가방이 생성되었습니다."})     #class명. 클래스변수명으로 접근함
#
#     @classmethod
#     def sell(cls):
#         print("가방이 팔렸습니다.")
#         cls.count -= 1                              #클래스 메서드가 클래스 변수에 접근하기 때문에 Bag.count가 아니라 cla.count입니다.
#     @classmethod
#     def remain_bag(cls):
#         return cls.count
# print(f"현재 가방 재고 : {Bag.count}")
# print(f"현재 가방 재고 : {Bag.remain_bag()}")
#
# bag1 = Bag()
# print(f" 현재 가방 재고 : {Bag.remain_bag()}")
# bag2 = Bag()
# bag3 = Bag()
# print(f" 현재 가방 재고 : {Bag.remain_bag()}")
# bag1.sell()
# print(f" 현재 가방 재고 : {Bag.remain_bag()}")
# Bag.sell()
# print(f" 현재 가방 재고 : {Bag.remain_bag()}")


'''
이상의 코드에서 보면 예시이기 때문에 적합하다고 보기가 힘든데 
인스턴스 명.sell()로 작성한다면 특정한 가방 인스턴스가 팔렸다고 볼수 있기 때문에 가독성이 더 높은 반면 
Bag.sell()로 작성하게 되면 어떤 가방이 팔렸는지는 모르고 그냥 가방 카운트 변수 하나 줄었습니다.

저희는 코딩을 할때 변수 / 메서드를 인스턴스 수준으로 작성할지 혹은 클래스 수준으로 작성할지에 대한 고민이 선행되어야 합니다.


응용 예제 
다음 지시 사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 작성하시오
man = Person("안근수")
woman = Person("안근순")

man과woman은 인스턴스가 생성되면 다음과 같으 메시지를 출력할 수 있도록 작성하시오
안근순이 태어남
안근수가 태어남

print(f" 전체 인구 수 : {Person.get_population()}
ㅇdel man

man이 삭제되면 RIP 안근수가 나오도록




'''

# class Person:
#
#     population = 0
#
#     def __init__(self,name):
#         self.name = name
#         Person.population += 1
#         print(f"{self.name}이 태어났습니다")
#
#     @classmethod
#     def get_population(cls):
#         return cls.population
#
#     def __del__(self):
#         Person.population -= 1
#         print(f"RIP{self.name}")
#
#
#
#
# man = Person("안근수")
# print(f"전체 인구 수 : {Person.get_population()}")
# woman = Person("안근순")
# print(f"전체 인구 수 : {Person.get_population()}")
#
# del man
#
# print("프로그램이 종료 되었습니다.")



# class Shop:
#     total = 0
#     menu_list = {"떡볶이" : 3000}, {"순대" : 4000}, {"튀김" : 500}, {"김밥" :  2000}
#     menus = {
#         "떡볶이" : 3000,
#         "순대" : 4000,
#         "튀김" : 500,
#         "김밥" : 2000
#     }
#     @classmethod
#     def sales2(cls, menu_key, account):
#         # for key in cls.menus:
#         #     if key == menu_key:
#         if menu_key in cls.menus:
#             cls.total += cls.menus[menu_key] * account
#
#
#
#     @classmethod
#     def get_total(cls):
#         return cls.total
#     #
#     #
#     # @classmethod
#     # def sales(cls, menu_name, quantity):
#     #     for menu_dict in cls.menu_list:
#     #         if menu_name in menu_dict:
#     #             cls.total += menu_dict[menu_name] * quantity
#     #             print(f"{menu_name}을(를) {quantity}개 판매")
#
#
# Shop.sales2("떡볶이", 1)
# Shop.sales2("순대", 2)
# Shop.sales2("튀김", 5)
# Shop.sales2("김밥", 1)
# print(f"매출 : {Shop.get_total()}원")



