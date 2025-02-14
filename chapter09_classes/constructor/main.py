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

class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is born")

    def __del__(self):

        print(f"{self.name} is dead")
man = Person("james")
woman = Person("emily")
del man

print("프로그램이 종료합니다")



''''
예제 1 
학생들의 성적을 관리하는 Student 클래스를 작성하시오 이 클래스는 학생의 이름 학번 성적을 인스턴스 변수로 갖습니다

student 클래스를 정의하고 생성자를 통해 name, student_id, grape을 초기화 하시오
학생의 프로필을 출력하는 인스턴스 메서드 print_grade

git hub에서 받아 쓰기
'''