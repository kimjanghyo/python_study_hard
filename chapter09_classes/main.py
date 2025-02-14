''''
메개변수 6재 중 하나 저의


'''
from calendar import month

# def student_info(name, department, professor, phone, address, grade):
#     print(name)
#     print(department)
#     print(professor)
#     print(phone)
#     print(address)
#     print(grade)

#
# name1 = "kjh"
# department1 = "student"
# professor1 = "david"
# phone1 = "010-1234-1234"
# address1 = "busan"
# grade1 = "A"
# student_info(name1, department1, professor1, phone1, address1, grade1)
# student_info(1,1,1,1,1,1)

# student_info(grade="B", address="seoul", phone="010-5678-5678", professor="jone", department="adut", name= "hjk")


#name2, .... grape2라는 변수 선언하고


# name2 = "kjh"
# department2 = "student"
# professor2 = "david"
# phone2 = "010-1234-1234"
# address2 = "busan"
# grade2 = "A"
#
#
# student_info("kjh", "student",
# "david","010-1234-1234","busan","A")
# student_info(name=name2, department=department2, professor=professor2, phone=phone2, address=address2, grade=grade2)

'''
이상의 상황들 변수에 각각 데이터를 대입 한 후 함수의 agrument를 사용하거나, 혹은 데이터를 직접 argument에 등록을 벗어나기 위해 클래스와 객체 개념을 도입

class란? 객체를 만드는 도구 - 설걔도 틀 청사진


자동차 설계도 = 클래스
설계도를 통해 만든 자동차들 = 객체

같은 설께도로 만든 자동차라 하더라도서로 다른 옵션을 가질수 있음
마찬가지로 같은 클래스로 만든 객체라 하더라도 서로다른 값을 가질 수 있음


인스턴스 역시 클래스를 이용해서 생성한 객체 
바라보는 관점 차이로 볼 수 맀음
차 설계도로 만든 자동차는 객체
자동차는 설계도의 인스턴스

클래스를 정의
클래스 작서하는 것을 클래스 정의라고 합니다.
함수 정의를 생각하면 됩니다.



혛식:

calss 클래스 명 (대문자):
본문
-----------------------
객체 생성형식:                        함수 호출을 생각하시면 비슷합니다.
객체 이름 = 클래스 명
'''
# # class WaffleMachine:
# #     pass
# #
# # waffle = WaffleMachine()
# # print(waffle)
'''
print(waffle)을 시켰을떄 < __main__.WaffleMachine object at 0x00001D3D89AE180>에서 object라고 표기하느 점을 미루어 보아 walffle은 WalffleNachine의 객체임

클래스 기본 구성 

객체를 만들어 내는 클래스는 개체가 가텨야 할 구성 요소를 지닙니다.
객체를 생성하기 우;해 클래스 객ㅊ체가 가져야 할 값과 기능을 넣어야 하 
값= 속성
기능은 메서드


클래스 변수 클래스 기반으로 생성된 인스턴스
인스턴스 변수 인스턴스 들이 개별적으로 이루어진 변수



메서드 특징 
클레스 메서드
정적 메서드 
인스턴스 메서드

'''
# class Person:
#     def set_info(self, name, age, tel, address):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         self.address = address
#
#     def display_info(self):
#         print(f"이름 : {self.name}")
#         print(f"나이 : {self.age}")
#         print(f"전화번호 : {self.tel}")
#         print(f"주소 : {self.address}")

    # #객체 생성
    #
    #
    # person1 = Person()
    # print(person1)
    # person1.set_info("kjh", 38, "010-1234-1234", "Busan")
    # print(person1.display_info())

#     def display_info2(self):
#         return f"제 이름은 {self.name}이고, {self.age}살이며, \n전화번호는 {self.tel}이며,  주소는 {self.address}입니다."
#
#
# person2 = Person()
# person2.set_info("kjh", 21, "010-5678-5678", "Korea")
# print(person2.display_info())
                                    #self는 인스턴스 메서드에 항상 있었야 하기에 아직 인스턴슬르 생성하지 않았기 때문에 인스턴스 이름이 없습니다.
                                    #추후 인스턴스 생성하게 된다면 인스턴스 명 .name 등으로 시작합니다.
'''
으용ㅇ 예제 

다음 지시상황을 읽고 책 제목과 저자 정보를 저장할 수 있는 book 클래스 생성하세요
객체 생성 ㅅ;ㄹ행 예를 구하시오

book1 = Book()
book2 = Book()

set_info(self, title, author)을 통해 책 제목 입력하세요.
display_info()를 통해 실행 예와 같이 출렷하세요



'''

# class Book:
#     def self_info(self, title, author, stock):
#         self.title = title
#         self.author = author
#         self.stock = stock
#
#     def display_info(self):
#         print(f"책 제목 : {self.title}")
#         print(f"저자 : {self.author}")
#         print(f" 권 수 : {self.stock}")
#     def display_info2(self):
#         return f" 책 이름은 {self.title}\n저자는 {self.author}입니다 그리고 {self.stock}권 입니다.."
#
# book1 = Book()
# book1.self_info("파이썬", "민경태", 3)
# book2 = Book()
# book2.self_info("어린왕자", "생텍쥐페리", 10)
# print(book1.display_info())
# print(book2.display_info())
#
# print(book1.title)
# print(book1.stock +2)