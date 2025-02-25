'''
chapter14_exception
main

1. 예외 처리의 필요성
    1) 예외 vs. 오류
        예외(exception) : 개발자가 직접 처리할 수 있는 문제
        오류(error) : 개발자가 처리할 수 없는 문제

    2) 예외 처리의 목적 :
        어떤 문제가 발생했을 때 그 문제를 해결해 주는 것이 아니라,
        발생된 문제로 인해 프로그램이 비정상적으로 종료되는 것을 막고,
        사용자에게 발생한 문제에 대해 정보를 전달하기 위함.
'''

# 2 / 0
'''
    2 / 0
    ~~^~~
ZeroDivisionError: division by zero

와 같은 방식으로 프로그램이 정상적으로 종료되지 않으며, 보기에 좋지도 않기 때문에,
예외를 처리하면 좋다.

2. 예외 처리
    1) 고전적인 예외 처리
'''
# a = int(input("나누는 수를 입력하세요 >>> "))
# b = int(input("나누어 지는 수를 입력하세요 >>> "))
# if a == 0:
#     print("0으로 나눌 수 없습니다.")
# else:
#     print(f"b / a = {b/a}")
'''
어떤 값이든 0으로 나눌 수 없기 때문에 if a == 0 을 통해 0으로 나누는 것을 아예 시도할 수
없도록 예외 처리를 함.

여기서 생각할 수 있는 잠재적인 문제는 :
    1) 어떤 문제가 발생할 지 예상할 수 있어야 미리 대비할 수 있다.
    2) 어떤 문제가 발생할 지 예상할 수 있더라도 대비할 수 없는 경우가 있다.
    

3. 예외의 종류

+------+---------------------+---------------------------------------------+
| 순번 |     예외 클래스     |                     의미                    |
+------+---------------------+---------------------------------------------+
|  1   |    BaseException    |              최상위 예외 클래스             |
|  2   |      Exception      |       대부분 예외 클래스의 슈퍼 클래스      |
|  3   |   ArithmeticError   |          산술 연산에 문제가 있을 때         |
|  4   |    AttributeError   |           잘못된 속성을 참조할 때           |
|  5   |       EOFError      | 파일에서 더 이상 읽어 들일 데이터가 없을 때 |
|  6   | ModuleNotFoundError |           import할 모듈이 없을 때           |
|  7   |  FileNotFoundError  |           존재하지 않는 파일일 때           |
|  8   |      IndexError     |          잘못된 인덱스를 사용할 때          |
|  9   |      NameError      |        잘못된 이름(변수)을 사용할 때        |
|  10  |     SyntaxError     |               문법이 틀렸을 때              |
|  11  |      TypeError      |   계산하려는 데이터의 유형이 잘못되었을 때  |
|  12  |      ValueError     |    계산하려는 데이터의 값이 잘못되었을 때   |
+------+---------------------+---------------------------------------------+ 
4. 예외 처리 방식
    1) 모든 예외를 처리하는 방식 -> try / except 문
    
    형식 :
try :
    코드 작성 영역
except :
    예외 발생 시 처리 영역
'''
# try :
#     a = int(input("나누는 수를 입력하세요 >>> "))
#     b = int(input("나누어지는 수를 입력하세요 >>> "))
#     print(f"b / a = {b/a}")
# except :
#     print("예외가 발생했습니다.")
'''
기본 예제

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램입니다.
try / except 문을 사용하여 "예외가 발생하였습니다."를 출력할 수 있도록 작성하세요.
'''
# try:
#     height = input("키를 입력하세요 >>> ")     # 결과값이 str
#     height = round(height)                  # str을 round처리할 수가 없기 때문에 예외 발생
#     print(f"입력하신 키는 {height}cm로 처리됩니다.")
# except:
#     print("예외가 발생하였습니다.")
'''
        2) 특정 예외만 처리하는 방식
            try / except 문을 사용하면 기본적으로 예외의 종류에 상관없이 모든 예외가 처리됨.
            하지만 이상에서 본 것처럼 0으로 나누는 경우와, 정수가 아닌 값을 입력한 경우에
            서로 다른 메시지를 출력한다면, 개발자에게 예외를 처리할 수 있을만한 정보를
            제공할 수 있음(아까 전까지의 예시는 예외 발생 후에 개발자가 어떤 코드에 문제가 있었는지
            스스로 확인해야했다는 점에서 편의성 개선 측면으로 볼 수 있음).
            
            2)-1. 0으로 나누려고 하는 경우 -> 0으로 나눌 수 없습니다.
            2)-2. 정수가 아닌 값을 입력하는 경우 -> 정수만 입력할 수 있습니다.
            로 특정 예외에 따른 서로 다른 안내문을 제시한다고 할 때,
            except 문 뒤에 처리하고자 하는 예외를 모두 명시하면 됩니다.
'''
# try:
#     a = int(input("나누는 수를 입력하세요 >>> "))
#     b = int(input("나누어지는 수를 입력하세요 >>> "))
#     print(f"b / a = {b/a}")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except ValueError:
#     print("정수만 입력할 수 있습니다.")
'''
ZeroDivisionError
ValueError
'''
# try :
#     a = int(float(input("나누는 수(정수만)를 입력하세요 >>> ")))
#     b = int(float(input("나누어지는 수(정수만)를 입력하세요 >>> ")))
#     print(f"b / a = {b/a}")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
'''
        거의 모든 예외는 Exception 클래스의 서브 클래스입니다. 따라서 모든 예외는 Exception의
        인스턴스가 됩니다. 다음과 같이 마지막에 작성하는 except문 뒤에 Exception을 명시하면
        예상하지 못한 예외들도 모두 처리할 수 있게 됩니다.
        
형식 :

try :
    코드 작성 영역
except 예외클래스1:
    예외메시지1
except 예외클래스2:
    예외메시지2
...
except Exception:
    예외메시지n                  # 맨마지막에는 위의 except들이 처리하지 못하는 예상 못한 예외를 처리하기 위해
                                # Exception으로 마무리

4. 예외 메시지 처리하기
    지금까지는 직접 예외 메시지를 만들어서 사용했지만 기본적으로 예외 메시지를 이미 가지고 있는 경우도 있습니다.
    디폴트 에러 메시지를 출력하는 방식에 대해서 학습합니다.
    
형식 :
try :
    코드 작성 영역
except 예외클래스 as 예외메시지:
    예외 발생 시 처리 영역
'''
# z = [10, 20, 30, 40, 50]
#
# try:
#     print(z[10])
# except IndexError as e:
#     print(e)
'''
5. else / finally 문
    try / except 문에 추가로 else와 finally문을 사용할 수 있음.
    else : 예외가 발생하지 않으면 처리되는 구문
    finally : 예외 발생 여부와 관계없이 맨 마지막에 항상 처리되는 구문
    
형식 :
try :
    코드 작성 영역
except :
    예외 발생 시 처리 영역
else :
    예외가 없을 시 처리 영역
finally :
    언제나 실행되는 영역
'''
# try :
#     a = int(input("나누어 지는 수를 정수로 입력하세요 >>> "))
#     b = int(input("나누는 수를 정수로 입력하세요 >>> "))
#     result = b / a
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else :
#     print(f"b / a = {result}")
# finally:
#     print("프로그램이 종료되었습니다.")
'''
6. 강제로 예외 발생시키기
    어떤 사람이 나이를 정수로 입력 받는 프로그램이 있다고 가정했을 때,
    컴퓨터 상으로는(그리고 파이썬 상으로는) -1000이 정수이기 때문에 예외가 발생하지 않습니다
    하지만 -1000살이 될 수 없기 때문에 직접 예외를 발생시켜서 처리해야만 합니다.
    
    -> raise문

형식 :
raise 예외클래스()               # 이건 사용자가 정의하는겁니다

또는

raise 예외클래스(예외메시지)

raise는 강제로 예외를 발생시킨다는 점에서 주로 사용되는 예외 클래스는 Exception입니다.
'''
# age = int(input("나이를 입력하세요 >>> "))      # -1000 살 입력했을 때 예외가 발생하지 않음.
# print(f"당신의 나이는 {age}살입니다.")            # 파이썬 상에서는 문제가 없지만 현실 세계에서 생기는 예외

# try :
#     age = int(input("나이를 입력하세요 >>> "))
#     raise Exception("강제로 발생시킨 예외입니다")   # 이 경우 멀쩡한 숫자를 입력해도 예외가 발생합니다.
# except Exception as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)

'''
7. 사용자 정의 예외 클래스

    음수를 입력받을 때 강제로 예외를 발생시키는 예외 클래스를 정의
'''
# class NegativeAgeError(Exception):          # 클래스명(부모클래스) -> 상속 개념
#     """사용자 정의 예외 클래스 : 나이가 음수일 때 발생"""
#     pass    # 예외를 발생시키기만 하면 되기 때문에 따로 코드 작성할 필요 없음
#             # -> Exception 클래스를 상속 받았기 때문에 메서드 사용 가능
#
# class TooManyAgeError(Exception):
#     pass
#
# try :
#     age = int(input("나이를 입력하세요 >>> "))
#     if age < 0:
#         raise NegativeAgeError("나이는 음수일 수 없습니다.")
#     # 200 초과일 때 확인하는 조건문 작성
#     if age > 200:
#         raise TooManyAgeError("불가능한 나이 입력입니다.")
# except NegativeAgeError as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
# except TooManyAgeError as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f"당신의 나이는 {age}살입니다.")
# finally:
#     print("프로그램이 종료되었습니다.")

'''
나이를 200 초과 입력했을 때 '강제로 TooManyAgeError를 발생시키고' '불가능한 나이 입력입니다'를
출력하는 예외 클래스를 정의하고 이상의 코드에 추가하시오.
나이를 실수로 입력했을 때 나타는 예외를 처리하고 default 에러 메시지를 출력하시오.
예상할 수 없는 예외가 발생했을 때 처리하는 예외 구문을 작성하시오.
else 문을 통해 정상적으로 처리되었을 때 당신의 나이는 __살입니다.가 출력되도록 작성하시오.
finally 구문을 통해 프로그램이 종료되었습니다. 가 출력되도록 작성하시오.



과제

사용자의 점수를 0 이상 100 이하로 입력 받아서 점수가 80점 이상이면 합격, 아니면 불합격을 출력하는
프로그램을 작성하는데, 0 이상 100 이하의 유효한 값이 아니라면 예외를 발생시키고
'점수는 0이상 100이하입니다'라는 예외 메시지를 출력하시오 -> 사용자 정의 예외 클래스를 정의해야하겠죠.
ScoreOutOfRangeError 클래스를 정의해서 사용하겠습니다.

입력 받는데 예를 들어 백점이라고 입력하면 '점수는 숫자로 입력해야합니다'라는 메시지를 출력하세요.
실수로 입력하면 '정수로 입력해야 합니다'라는 메시지를 출력하세요.

예상할 수 없는 예외가 발생시 Exception을 적용하여 디폴트 에러 메시지를 출력하세요.

프로그램이 종료되었다는 메시지를 맨 마지막에 작성하세요.
'''
# class ScoreOutOfRangeError(Exception):
#     """0 미만 100 초과의 점수값이 입력되었을 때 발생하는 Error 클래스입니다."""
#     pass
#
# try :
#     score = int(input("점수를 정수로 입력하세요 >>> "))
#     if score < 0 or score > 100:
#         raise ScoreOutOfRangeError("점수는 0이상 100이하입니다")
# except ScoreOutOfRangeError as e:
#     print(e)
# except ValueError as e:
#     print("점수는 숫자로 입력해야합니다.")
#     print(e)
# except Exception as e:
#     print(e)
# else :
#     if score >= 80:
#         print("합격")
#     else :
#         print("불합격")
# finally:
#     print("프로그램이 종료되었습니다.")
'''
사용자로부터 숫자를 입력 받아 해당 숫자로 100을 나누는 값을 출력하는 프로그램을 작성하시오.
만약 사용자가 0을 입력하거나 숫자가 아닌 값을 입력하면 적절한 예외 메시지를 출력하시오.

지시 사항
1. 사용자로부터 숫자를 입력 받는다.
2. 입력 받은 숫자로 100을 나누어 결과를 출력한다.
3. 입력 값이 0일 경우 적절한 예외를 처리하여 '0으로 나눌 수 없습니다'라는 메시지를 출력한다.
4. 입력 값이 숫자가 아닌 경우 적절한 예외를 처리하여 '숫자만 입력할 수 있습니다'라는 메시지를 출력한다.
5. 예외가 발생하지 앟는 경우 '정상적으로 처리되었습니다.'라는 메시지를 출력하고, 결과도 출력한다.
6. 프로그램 종료 메시지를 출력한다.
'''
# try:
#     num = int(input("숫자를 입력하세요 >>> "))
#     result = 100 / num
#
# except ZeroDivisionError as e:
#     print("0으로 나눌 수 없습니다.")
#     print(e)
#
# except ValueError as e:
#     print("숫자만 입력할 수 있습니다.")
#     print(e)
# except Exception as e:
#     print(e)
#
# else :
#     print("정상적으로 처리되었습니다.")
# #     print(f"100 / {num} = {100/num}")     # else로 넘어와서 0으로 연산을 하려고 하면 예외 발생함.
#     print(f"100 / {num} = {result}")        # 이상을 이유로 result라는 중간단계를 거쳐서 작성함.
# finally:
#     print("프로그램이 종료되었습니다.")

'''
사용자로부터 라스트의 인덱스를 입력받아 값을 출력하는 프로그램 작성하시오
만약 잘못된 인덱스를 입력하면 적절한 예외 메시지를 출력하시오

지시사항
1.미리 정의된 리스트가 있다
2. 사용자로 부터  리스트의 인덱스를 입력받는다
3.입력받은 인덱스를 사용하여 리스트의 값을 출력한다 
인덱스 리스트가 리스트의 범위를
'''
# class NegativeNumIndexError(Exception):
#     pass
# my_list = [10, 20, 30, 40, 50]
#
# try:
#     index_num = input("indexnum :")
#     index_num = int(index_num)
#     if index_num < 0 :
#         raise NegativeNumIndexError("마이너스 인덱스 적용 x")
#     chosen_element = my_list[index_num]
#
# except NegativeNumIndexError as e:
#     print(e)
# except ValueError as e:
#     print("정수만 입력")
#     print(e)
# except IndexError as e:
#     print("list의 범위를 벗어났습니다.")
#     print(e)
# except TypeError as e:
#     print("자료형이 잘못 되었습니다.")
#     print(e)
# except Exception as e:
#     print("예측할 수 없는 예외가 발생 했습니다.")
#
# else:
#     print(f"{index_num} 위치에 있는 값은 {my_list[index_num]}입니다.")
# finally:
#     print("종료")
'''
사용자로부터 속성명을 입력받아 객체의 해당 속성을 출력하는 프로그램 작성
만약 잘못되면 적절한 예외 처리 메시지 출력


'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        person1 = Person(name="Jone", age=30)
#
# try:
#     attribute1 = input(":")
# except AttributeError as e:
#     print("존재하지 않는 속성명")
#     print(e)
# except Exception as e:
#     print("예측할 수 없는 예외가 발생")
#     print(e)
# else:
#     print("정상")
#     print(getattr(person1, attribute1))
# finally:
#     print("end")

# '''
# getattr(객체명, 속성명) 함수:

# '''

# attribute = input("출력할 속성명을 입력하세요.>>>")
#         print(person1.name)
#         print(getattr(person1, attribute))
# person1 = Person
# profile = vars(person1)
# try:
#     attribute2 = input(":")
#     if attribute2 in profile:
#         print("정상 출력이 가능 합니다")
#     else:
#         raise KeyError("존재하지 않는 속성입니다.")
# except KeyError as e:
#     print(e)
#     print("존재하지 않는 속성입니다.")
# except Exception as e:
#     print(e)
#     print("예측할 수 없는 예외가 발생 하였습니다.")
# else:
#     print(f"{attribute2}의 값은 : {profile[attribute2]}입니다.")
# finally:
#     print("end")

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def eat(self, food):
#             print(f"{self.name}이 {food}를 먹었습니다.")
# class Student(Person):
#     def __init__(self, name, school):
#         super().__init__(name)
#         self.school = school
#     def study(self):
#         print(f"{self.name}은 {self.school}에서 공부합니다.")
# potter = Student(name="해리포터", school="호그와트")
# potter.eat("감자")
# potter.study()
#
#
# print(isinstance(potter, Student))
# print(isinstance(potter, Person))
#
# class Car:
#     max_oil = 50
#     def __init__(self, oil):
#         self.oil = oil
#     def add_oil(self, oil):
#         if oil <= 0:
#             return
#         self.oil += oil
#         if self.oil > Car.max_oil:
#             self.oil = Car.max_oil
#     def car_info(self):
#         print(f"현재 주유 상태 : {self.oil}")
# class Hybrid(Car):
#     def __init__(self, oil, amount):
#         super().__init__(oil)
#         self.amount = amount
#     def charge(self):
#         if self.amount < 0:
#             return
#         self.amount += amount
#         if self.amount > Hybrid.max_amount
#     def hybrid_info(self):
#         # print(f"현재 주유 상태 : {self.oil}")
#         super().car_info()
#         print(f"현재 충전 상태 : {self.amount}")
# car = Hybrid(oil=0, amount=0)
# # car.add_oil(100)
# # car.charge(50)
# car.hybrid_info()