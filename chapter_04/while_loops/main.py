'''
형식

while 조건문:
    실행문

'''
#무한 루프의 개념
# num = 1
# while num > 0:
#     print(num)

'''
while문 고려항ㄹ 점 
특정 조건식이 False가 될 수 있도록 사전에 미리 지정해둬야함 
아닐 경우 무한 루프에 빠지게 됨


'''
# num = 1
# while num < 11:
#     print(num)
#     num += 1

'''
if문과 비교:
    if문의 경우 조건식이 참일떄 실행문이 한번 실행하지만
    while문의 경우 조건식이 참일 떄 실행문이 반복 실행되기 때문에
    특정 조건이 맞을 경우가 아닌 경우에 대한 고민이 필요한 편
    

    


'''
# num = 10
# while num > 0:
#     print(num)
#     num -= 1

# num = 10
# while num > 1:
#     num -= 1
#     print(num)

'''
중첩 while문

ex) 5일 동안 3시간 씩 수업
매일 1일차 1교시부터 5일차 3교시 나오게
 
'''
# day = 0
# while day < 5:
#     day += 1
#     hour = 0
#     while hour < 3:
#         hour += 1
#         print(f"{day}일차 {hour}교시입니다.")
#
#
# day = 1
# while day < 6:
#     hour = 1
#     while hour < 4:
#         print(f"{day}일차 {hour}교시입니다.")
#         hour += 1
#     day += 1



'''
구구단 2단 부터 9단 까지
2 x 1 = 2 
...
9 x 8 = 72 
9 x 9 = 81 
'''

# dan = 2
# while dan < 10:             #값이 있으면 True로 취급함
#     number = 1
#     while number < 10:
#         total = dan * number
#         print(f"{dan} x {number} = {total} ")
#         number += 1
#     dan += 1


# n = 1
# while n <= 100:
#     print(f"{n} {n+1} {n+2} {n+3} {n+4} {n+5} {n+6} {n+7} {n+8} {n+9}")
#     n += 10


#이상의 코드의 경우에는 반복을 10번 돌리는 경우였습니다.
#모든 편견을 가지고 코드를 억지로 작성하게 되면 즉, 반복을 100먼 돌리게 됬을 경우 상용

# n2 = 1
# while n2 < 101:
#     print(n2, end=" ")
#     if n2 % 10 == 0:
#         print()
#     n2 += 1
