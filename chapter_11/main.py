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
class Korean2:
    country = "대한민국"

    @classmethod
    def trip(cls, travelling_site): #self가 아닌 cls가 작동
        if cls.country == travelling_site:
            print("국내 여행 입니다.")
        else:
            print("해외 여행입니다.")

Korean2.trip("대한민국")
Korean2.trip("미국")