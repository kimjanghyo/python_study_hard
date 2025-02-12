import random


word_list = ["apple", "banana", "camel"]
chose_word = random.choice(word_list)
print(chose_word)


#todo -1 : 비어있는 list와 display를 만드시오 chose_word의 각 문장 개수 마다 "_"를 추가 예로 chose_word == "apple" display = ["_"],["_"],["_"],["_"]]가 되어야 한다

display = []
for _ in range(len(chose_word)): #변수가 사용되지 않음 i가 아니라 _로 표시
    display.append("_")
print(display)



for letter in chose_word:
    display.append("_")
print(display)



#todo -2: chosen_words의 각 문자들을 반복시키세요 만약 그 문자의 guess가 일치 하면 해당 위치에 display에서 해당 문자를 고개 하세요 ex) 사용자가 p 를 입력했고 chose_words가 사과면 display '_'. 'p' 'p' '-' '-'로 바뀌어야 ㅎ나다


# numbers = [1,2,3,4,5]
# print(numbers)
# numbers[0] = 100
# print(numbers)

guess = input("알파벳 입력>>>>>").lower()


for _ in range(len(chose_word)):
    if chose_word[_] == guess:
        display[_] = guess
print(display)
