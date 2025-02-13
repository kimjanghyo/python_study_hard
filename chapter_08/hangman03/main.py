import random

#특정 모듈 사용한다는 것을 맨 처음에 명시합니다.

'''
"".join(반복가능객체) method: .앞에 있는 문자열을 기준으로 반복 가능 한 객체로 묘소들을 합쳐서 str로 변환함



'''


# temp = ["안","녕","하","세","요"]
# hello = "".join(temp)
# print(hello)
# print("/".join(temp))
# print(" ".join(temp))




word_list = ["apple","banana", "camecl"]
chose_word = random.choice(word_list)



#todo -1 "_"가 적용된 display 구현

#todo -2 사용자가 추측을 반복할 수 없도록 while 반복문을 작성합니다. 즉, display에 더 이상 "_"가 없을때 반복문이 멈추도록 작성합니다. 반복문 종료 후 ptrint(정답)을 출력


display = []

for _ in range(len(chose_word)):
    display.append("_")
while "_" in display:
    guess = input("알파벳 입력>>>>>").lower()

    for _ in range(len(chose_word)):
        if chose_word[_] == guess:
            display[_] = guess
        print(display)
print(" ".join(display))
print("정답입니다!!:")

