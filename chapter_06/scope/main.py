'''
scope: 범위

지역 변수 : 함수 내부에 정의 된 변수
전녁 변수 : 함수 외부 (main단계)에 정의된 변수

'''
from math import gamma

# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"함수 내부 적의 숫자 {enemies}입니다")
#
# increase_enemies()
# print(f"함수 내부 적의 숫자는 {enemies}입니다.")



#지역 변수 =/= 전역 변수 -> 그렇다보니깐 변수명을 서로 다르게 짓는데 혼란을 피하는 방식






#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
#
# print(potion_strength) #오류 발생
# drink_potion()          #오류 호출
#




#
# player_health = 10
# def game():
# #
# #
#     def drink_potion():
#         global player_health
#         player_health += 2
#
#         drink_potion()
#
# #이상의 코드에서 생겨날 잠재적 변수의 값이 바뀌기 때문에
# #전역 변수의 값을 정확히 알기 위해서는
# # 함수의 호출 횟수를 알아야 한다는 점이다
# #이상을 이유로 함수가 전역 변수의 값을 바꾸는 이러한 코딩 방식은
# #선호되지 않는다
# game()
# print(f"체력은 {player_health}입니다.")



game_level = 3
def creat_enemy():
    enemies = ["좀비", "스켈레톤", "크리퍼"]
    if game_level < 5:
        new_enemy = enemies[2]

    print(new_enemy)

creat_enemy()





'''
이사의 코드에서 생기는 문제점 
1. game_level 이라는 전역변수를 create_enemy()라는 함수의 정의 부분에서 사용하고 있음에도 오류발생하지 않음
2. 함수 정의 내부의 if절에서 new_enemy라는 변수를 선언했음에도 
if절 밖 new_적을 창조 했음에도 오류가 발셍 않음

    1.의 이유 게임 레벨잉라는 전역변수의 값을 바꾸는 게 아닝라 참조만 해서 서살/ 거싲만 반환하기에 오류 없음
    2.의 이유는 if while for가 같이  콜론을 기준으로 들여쓰기가 있는 모든 코드 블록들은 지역변수를 만드는 것으로 간 주되지ㅏ 안흥므
    
'''




























