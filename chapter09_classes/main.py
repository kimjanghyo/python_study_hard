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
class WaffleMachine:
    pass

waffle = WaffleMachine()
print(waffle)
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