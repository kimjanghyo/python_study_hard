#while 반복문
'''while 다음에 나오는 조건문이 참이라면 이하의 실행문이  실행됨.

형식:
    while 조건문:
    시행문
'''
#num1 = 1
#while num1 > 0:
#   print(num1)

#예를 들어 1을 10번 실행하고  싶으면
#num2  =  10
#while num2 >0:
    #print(1)
    #num2 -= 1

    #특정 조건하에 while 조건문이
    #False가 되도록 하는 중요한 부분

'''
항상 False가 되는 부분을 준비해야하는 점을 근거로,
while문의 경우는 특정 조건을 만족해서 수행하는 코드를 작성할 때 사용
반면 for문은 정확한 반복횟수가 고정될 때 사용
'''
'''
if 조건문"
    실행문
    
while 조건문
    (반복) 실행문
    
기본  예제 
1 ~ 10 까지  출력하는   while문
'''
#num3 = 1
#while num3 < 11:
    #num3 += 1


'''
중첩 while문 : 내부에 ehilw문 내부에 while문이 나타나는 것 ->  중첩 의무문
'''
#day = 1
#while day < 6:
   # hour = 1
   # while hour < 4:
     #   print(f"{day}일 차 {hour}교시입니다.")
     #   hour  += 1
  #  day += 1

'''ctrl + / 누러서 주석 처리  
ctrl + z 실행 취소
한영키 영어
'''

# num = 2
# while num < 10:
#     number = 1
#     while number < 10:
#         print(f"{num} x {number} = {num*number}")
#         number += 1
#     num += 1

'''
응용 예제

1부터 100 사이의 모든 정수를 한줄에 10개씩  출력하는  프로그램

'''

# n = 1
# while n < 101:
#     print(f"{n} {n+1} {n+2} {n+3} {n+4} {n+5} {n+6} {n+7} {n+8} {n+9}")
#     n += 10

# n = 1
# while n < 1000:
#     nu = 1
#     while nu < 1000:
#         print(f"{n} x {nu} = {n*nu}")
#         nu += 1
#     n += 1

