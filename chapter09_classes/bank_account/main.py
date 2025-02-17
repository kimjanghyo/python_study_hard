'''

은행 계좌 관리하는 BankAccount 클래스를 작성하시오 이 클래스는 계좌 소유자 이름, 계좌 번호, 잔액 인스턴스
변수로 가집니다



'''
from calendar import month


class BankAccount:
    def __init__(self, owner, account_num, balance):
        self.owner = owner
        self.account_num = account_num
        self.balance = balance
    def set_owner(self,owner):
        self.owner = owner
    def set_account_num(self, account_num):
        self.account_num = account_num
    def set_balance(self, balance):
        self.balance = balance
    def get_owner(self):
        return self.owner
    def get_account_num(self):
        return self.account_num
    def get_balance(self):
        return self.balance
    def print_account_info(self):
        print(f"이름 :{self.owner}")
        print(f"계좌 :{self.account_num}")
        print(f"잔액 :{self.balance}")
    def deposit(self, money):
        if money <= 0:
            print(f"{money}원은 입금이 불가 합니다")
            return
        self.balance += money
        print(f"{money}원을 입금하였습니다. 잔액 : {self.balance}")
    def withdraw(self, money):
        if money <= 0:
            print(f"{money}원은 출금이 불가 합니다")
            return
        if self.balance - money < 0:
            print("잔액이 부족합니다")
            return
        self.balance -= money
        print(f"{money}원을 출금하였습니다. 잔액 : {self.balance}")
account1 = BankAccount("홍길동", "123-456-789", 100000)
account2= BankAccount("심사임당", "987-654-321", 500000)


account1.print_account_info()
account2.print_account_info()

account1.withdraw(10000)
account1.withdraw(20000)

account1.withdraw(20000)
account1.print_account_info()