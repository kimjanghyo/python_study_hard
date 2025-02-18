
MENU = {
    "에스프레소": {
        "재료": {"물": 50 , "커피" : 18,},
        "가격" : 1.5,},
"라떼" : {
    "재료" : {"물" : 200, "우유" :150, "커피" : 24,},
    "가격" : 2.5,},
"카푸치노" : {"재료":
              {"물": 250, "우유": 100, "커피" : 224,},
          "가격":  3.0}
}

# print(MENU)
# print(MENU["라떼"]["재료"]["우유"] + 1)
# print(MENU["라떼"]["가격"])


# 카푸치노 가격 출력
# 에스프레소 물 양 출력
#
#
# print(MENU["카푸치노"]["가격"])
# print(MENU["에스프레소"]["재료"]["물"])

profit = 0
resources = {"물": 300,
             "우유" : 200,
             "커피" : 100,

}
#resources에서 에스프레소 두 잔을 뽑았을때, 남는 물, 우유, 커피랑 영산 하고 그 결과콘솔로 출력하시오.
#
# resources["물"] -= MENU["에스프레소"]["재료"]["물"]
# print(resources)
# resources["물"] -=  MENU["에스프레소"]["재료"]["물"] * 2
# resources["커피"] -= MENU["에스프레소"]["재료"]["커피"] * 2
# print(resources)


# profit += MENU["에스프레소"]["가격"] * 2
# print(profit)


# choice = input("어떤 음료를 드시겠습까?")
# print(MENU[choice]["재료"])
def is_resources_enough(order_ingredients):
    """DocString: 함수/클래스/메서드가 어떤 작동을 하는지 ' 사람들에게 ' 설명 해주는 기능
    주문 받은 음료들 resources 에서 재료 차감 하고 난 후 음료 만들기가 가능 하면 True 아니면 False 반환
    :param: order_ingredients
    :return: True/ False"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다. {item}이 부족합니다.")
            return False
        return True

def process_coins():
    #쿼터, 다임, 니켈, 페니 4종류 동전
    #쿼터 = 0.25달러
    #다임 = 0.1달러
    #니켈 = 0.05달러
    #베니 = 0.01달러
    #quarters, dimes,  nickels, pennies


    # quarters = int(input("쿼터 동전을 몇개 넣으시겠습니까?")) * 0.25
    # dimes = int(input("다임 동전을 몇개 넣으시겠습니까?")) * 0.1
    # nickels = int(input("니켈 동전을 몇개 넣으시겠습니까?")) * 0.05
    # pennies = int(input("페니 동전을 몇개 넣으시겠습니까?")) * 0.01
    #
    # return quarters + dimes + nickels + pennies
    total = 0.0
    total += int(input("쿼터 동전을 몇개 넣으시겠습니까?")) * 0.25
    total += int(input("다임 동전을 몇개 넣으시겠습니까?")) * 0.1
    total += int(input("니켈 동전을 몇개 넣으시겠습니까?")) * 0.05
    total += int(input("페니 동전을 몇개 넣으시겠습니까?")) * 0.01

    return total

def is_transaction_successful(money_received, drink_cost):
    charge = money_received - drink_cost
    if charge >= 0:
        global profit
        profit += drink_cost
        print(f"잔돈 ${charge}를 반환합니다.")
        return True
    elif charge < 0:
        print(f"coin is enough. receiving ${money_received}")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"{drink_name}가 나왔습니다. 맛있개 드세요.")

is_on = True
while is_on:
    choice = input("어떤 음료를 드시겠습까?>>> ")
    if choice == "off":
        is_on = False
        print("종료")
    elif choice == "report":
        print(f" 물 : {resources["물"]}ml")
        print(f" 우유 : {resources["우유"]}ml")
        print(f" 커피 : {resources["커피"]}g")
        print(f" 돈 : ${profit}")


    elif choice in ["에스프레소", "라떼", "카푸치노"]:   #에스프레소/ 라떼 / 카푸치노 중 하나를 입력했을때 다음 단계로 넘어가는 부분
        drink = MENU[choice]
        if is_resources_enough(drink["재료"]):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink["가격"]):
                # resources["물"] -= drink["재료"]["물"]
                # resources["우유"] -= drink["재료"]["우유"]
                # resources["커피"] -= drink["재료"]["커피"]
                # print(f"{choice}가 나왔습니다. 맛있개 드세요.")
                make_coffee(choice, drink["재료"])
    else:
        print(f"잘못 입력하셨습니다.")

