'''
사전 준비
'''
# age = input("당신의 나이는 몇 살입니까? >>> ")
# print(f"제 나이는 {age}살입니다.")
# print(type(age))            # <class 'str'>
'''
input() 함수의 결과값은 언제나 str입니다. -> 즉 수학 연산을 하기 위해서는 별도의 과정이 필요하다는 뜻입니다.

이때 필요한 함수가 형변환 함수입니다.
형식 :

int("37")과 같은 방식으로 사용 가능
'''
# print(f"내년에는 {age+1}살이 됩니다.")   # 여기서는 오류가 발생합니다.
# age = int(age)      # 이제 이런 코드 라인 해석할 수 있어야 합니다.
#                     # 4번 라인에서 작성된 string 타입의 데이터 age를 int로 변환시켜
#                     # age 변수에 다시 대입했다는 의미
# print(f"내년에는 {age+1}살이 됩니다.")
'''
자주 쓰이는 형 변환 함수 목록
1. int() -> str 혹은 float을 int로 변경
2. float() -> str 혹은 int를 float으로 변경
'''
# num1 = "100"
# print(f"num1의 값은 현재 {num1}입니다. 1을 더하면 {int(num1) + 1}이 됩니다.")
# print(f"num1의 값은 현재 {num1}입니다. 1을 더하면 {float(num1) + 1}이 됩니다.")
# num2 = 30
# num2 = float(30)
# print(num2)
# num3 = 99.9
# num3 = int(num3)            # 소수점이 전부 버림처리됩니다.
# print(num3)
'''
BMI 계산기를 작성합니다.

1. 키(cm)를 입력 받아(input()를 쓰라는 의미) 변수 height에 저장합니다.
2. 몸무게(kg)을 입력 받아 변수 weight에 저장합니다.
3. 몸무게 / (키(m)의 제곱) 을 계산하면 bmi지수가 나옵니다.
4. bmi 지수를 int로 출력되게끔 하세요.

실행 예

로고 출력하세요
당신의 키는 몇 cm입니까? >>> 173.2
당신의 몸무게는 몇 kg입니까? >>> 70
당신의 BMI 지수는 23입니다.
'''
height: float = float(input("당신의 키는 몇 cm입니까? >>> ")) / 100
print(height)

height: float(input("172"))
weight: float(input("70"))
print
height = input("172")
weight = input("70")
bmi = (weight / height)
print({input(bmi)})




