# age = input("당신 나이 몇? >>>")
# print(type(age))
# print(f" 님 나이 내년 {age+1}이 됨") >>> 오류 발생
'''
input() 함수위 결과 값은 언제나 str입니다. --> 즉, 수학 연산을 하기 위해선 별도의 과정이 필요합니다.
이때 필요한 함수가 '형변한 함수' 입니다.
'''


# age1 = input("당신 나이?>>>")
# print(type(age1))
# age1_int = int(age1)
#
# print(type(age1_int))
# print(f"당신의 내년 나이는 {age1_int+1}이 됩니다.")

'''

'''

# temp = int(3.8)
# print(temp)
# temp2 = float(4)
# print(temp2)
# temp3 = round(3.8)
# print(temp3)
# temp4 = round(5.3491285, 2)
# print(temp4)



# height = input("당신의 키는?>>>")
# height = float(height)
# height = height / 100
# weight = input("당신의 몸무게는?>>>")
# weight = float(weight)
# bmi = weight / (height**2)
# bmi_int = int(bmi)
# bmi_round = round(bmi, 2)
# print(f" 당신의 bmi지수는 {bmi_int}입니다.")
# print(f"당신의 bmi 지수는 {bmi_round}입니다.")
#
#
#


height = float(input("당신의 키는 >>>>")) / 100
weight = float(input("당신의 몸무게는?"))
# print(f"당신의 bmi지수는 {int(weight/(height**2))}입니다.")
# print(f"당신의 bmi지수는 {round(weight/(height**2), 2)}입니다.")
bmi = round(weight/(height**2), 2)
if bmi < 18:
    print(f"당신은 저체중입니다.")
elif bmi < 23.5:
    print(f"당신은 정상입니다")
elif bmi < 25:
    print(f"당신은 과체중입니다.")
else:
    print(f"당신은 비만입니다.")



logo = '''

________  ________  
\_____  \ \_____  \ 
 /  ____/   _(__  <
/       \  /       
\_______ \/______  /
        \/       \/ 
'''
print(logo)

'''
1. chrome에서 사이트를 확인하신 후 bmi가 특정구간일떄마다
    당신의 bmi지수는 xx.xx이고 과/정/저체중 입니다
'''
