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
profit = 0
resources = {"물": 300,
             "우유" : 200,
             "커피" : 100,

}

def is_resources_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다. {item}이 부족합니다.")
            return False
        return True

def process_coins():
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
    elif choice in ["에스프레소", "라떼", "카푸치노"]:
        drink = MENU[choice]
        if is_resources_enough(drink["재료"]) and is_transaction_successful(process_coins(), drink["가격"]):
            make_coffee(choice, drink["재료"])
    else:
        print(f"잘못 입력하셨습니다.")