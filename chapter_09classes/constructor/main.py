'''
생성자 (constructor)
'''
from multiprocessing.reduction import send_handle


# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def display_info(self):
#         print(f" 사탕의 모양은 {self.shape}이고 색은 {self.color}입니다.")
# sating = Candy()
# sating.set_info("구형", "갈색")
# sating.display_info()
#

'''
sating 인스턴스 생성과정
값이 없는 인스턴스 생성
값을 저장 할수 있는 베서드 호출


-> __init__() 라는 메서드

__init__()메서드(생성자)는 인스턴스가 생성될 떄 ' 자동으로 호출되기 때문에 인스턴스 변수의 '초기화' 용도로 사용
즉 값이 있는 인스턴스를 생성할 수 있다는 의미 입니다
'객체 생성과 동시에' 생성자가 호출됨 -> 초기 값 작성할 떄 사용

형식 
class 명:
    def __init__(self, shape, color):
        self.shape = shape
        self.solor = color
        
'''
# class Candy2():
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#     def display_info(self):
#         print(f" 사탕의 모양은 {self.shape}이고 색은 {self.color}입니다.")
# satang2 = Candy2("정육면체", "흰색")
# satang2.display_info()


'''
소멸자 Destructor
__del__()
'''
# class Sample:
#     def __init__(self):
#         print(f"인스턴스가 생성되었습니다.")
#     def __del__(self):
#         print(f"인스턴스가 소멸되었습니다.")
#
# sample = Sample()
#
# del sample
#
# print("프로그램이 종료되었습니다")


'''
1.클래스 USB를 정의 할 것
2. 생성자를 정의하여 매개변수로 capacity를 받을 것
deg_info()메서그 사용

'''
# class USB:
#     def __init__(self, capacity):
#
#         self.capacity = capacity
#
#     def get_info(self):
#         print(f"{self.capacity}GB USB")
#
# usb = USB(64)
# usb.get_info()

# class Service:
#     def __init__(self, service):
#         self.service = service
#         print(f"{self.service}를 시작")
#
#     def __del__(self):
#         print(f"{self.service}를 종료")
# s = Service("길 안내")
# print("프로그램이 종료되는 시점")
# del s

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is born")
#
#     def __del__(self):
#
#         print(f"{self.name} is dead")
# man = Person("james")
# woman = Person("emily")
# del man
#
# print("프로그램이 종료합니다")



''''
예제 1 
학생들의 성적을 관리하는 Student 클래스를 작성하시오 이 클래스는 학생의 이름 학번 성적을 인스턴스 변수로 갖습니다

student 클래스를 정의하고 생성자를 통해 name, student_id, grape을 초기화 하시오
학생의 프로필을 출력하는 인스턴스 메서드 print_grade
'''
# class Student:
#     def __init__(self, name):
# student1 = Student

#
# class Student:
#     def __init__(self, name, student_id, grade):
#         self.name = name
#         self.student_id = student_id
#         self.grade = grade
#     def print_profile(self):
#         print(f"학생 이름 : {self.name}")
#         print(f"학번 : {self.student_id}")
#         print(f"학점 : {self.grade}")
#
#
#
#     # 이사의 코드는 콘솔애 찍히기만 할 뿐 연산이 불가능하기 때문에 getter는 call1() 유형으로
#     def set_grade(self, grade):
#         if grade not in ["A","A+","B","B+","C+","C","D+","D","F"]:
#             print(f"{grade}는 불가능한 점수 입력입니다")
#             return
#         self.grade = grade
#
# student1 = Student("kfk", 20250001, "A")
# student1.print_profile()
# print(student1.set_grade("A+"))
#
# student2 = Student("sdd", 20260001, "B")
# student2.print_profile()
# print(student2.set_grade("A"))
#
# student3 = Student("wta", 20270001, "C")
# student3.print_profile()
# print(student3.set_grade("B+"))
# 이상의 이유로 인스턴스 변수에 값을 대입할 때 제약을 걸기 위해 method를 경유하여 값을 대입하도록 권장함
# setter(call2()유형)/ getter(call3()유형)
# student1.print_profile()
# student2.print_profile()
# student3.print_profile()

# 1.Setter / Getter란?
# 1)stter : 객체의 속성 값(인스턴스 변수)를 변경하는 메서드
# 1)stter : 객체의 속성 값(인스턴스 변수)를 조회하는 메서드
#
# 사용 이유
# 데이터 보호 및 무결성 유지
# 속성 값을 직접 변경하는 경우, 잘못된 값이 입력될 가능성이 높음
# setter를 사용하면 특정 조건을 만족하는 값만 속성 댜입 가능
# 객체의 캡슈화 실현
# 객체의 내부 데이터를 외부에서 직접 수정하는 것을 방지
# 메서드를 통해 접근하도록 제한하여 보안성 높임
# 추후 유지 보수 및 확장성 용이
# setter/ getter를 사용하면 특정 속성 로직을 쉽게 변셩 가능

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def set_name(self, name):
            self.name = name
    def set_age(self, address):
            self.address = address
    def set_age(self, age):
        if age< 0 or age>200:
            self.age =age
    def get_name(self):
            return self.name
    def get_address(self):
            return self.address
    def get_age(self):
            return self.age
person1 = Person("kjh", 21, "busan")
print(f"my name is {person1.get_name()}")
print(f"age is {person1.get_age()}, {person1.get_age() - 2}")
print(f"now live in {person1.get_address()}")

person1.set_age(-30)


