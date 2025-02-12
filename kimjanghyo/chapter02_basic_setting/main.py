'''if문
if문은 조건이 참(True)일 떄만 해당 블록의 코드를 실행합니다.
'''
from operator import truediv

age = 20
if age >=19:
    print("성인입니다.")
'''
if문에서 신경써야하는 점:
1) if와 같은 라인에 작성된 코드는 참/거짓으로 구분할 수있어야만 함
2) if와 같은 라인에 있는 조건문이 끝낚을 떄 콜론(:)으로 끝남
3) 
'''
age = 17

if age >= 19:
    print("성인 입니다.")
else:
    print("성인이 아닙니다.")
'''
print()
if-else는 서로 반대이기 때문에 else절에서는 조건식을 명시하지 않음)

3. if-elif-else 문
여러 조건을 동시에 검사하기 위해서 사용하는 구조.
'''
score = 85

if score >= 90:
    print("성취도는 A입니다.")
elif score >= 80:
    print("성취도는 B입니다.")
else:
    print("다시하세요.")
'''
이상의 코드에서 확인할 수 있는 점
1) 첫 번째 조건은 false 이지만,
2) 두 번째 조건은 true이므로 41번 라인이 실행 됨)
3) 이후 조건들은 확인하지 않고 조건문이 종료 됨)

if문 조건식1:
실행문1
(elif 조건식2:)
(실행문2)
elif 조건식 3:)
(실행문3)
(else:)
(실행문4)

4.중첩 if문(nesed if)
 조건문 내부에 또 다른 조건문을 사용할 수 없음)

'''
age = 25
has_ticket = True

if age >= 19:
    if has_ticket:
        print("영화관 입장이 가능합니다.")
    else:
        print("티켓을 구매하세요.")
else:
    print("미성년자는 입장할 수 없습니다.")
'''
5. 조건문에서 자주 쓰이는  연산자
비교 연산자 :
== : 같다
!: : 같이 않다
> : 초과
< :미만
>= : 이상
<= : 이하
논리 연산자
and : Aand B -> a와 b 모두 실행문 실행
or : A or B -> A 혹 B wnd gksk  ckadlfEo
not : if not A -> A가 False일때 
'''


