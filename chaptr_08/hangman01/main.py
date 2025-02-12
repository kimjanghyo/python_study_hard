
import random
# # word_list 내부의 요소들 중 하나의 임의로 선택하기 위해 random 모듈을 도입(import)
#
#
# numbers = [1,2,3,4,5]
# chosen_number = random.choice(numbers)

# print(chosen_number)

# word_list = ["apple", "banana", "camel"]
#todo -1 :word_list에서 단어 하나의 임의 적으로 선택하도록 random 모듈을 사용하고, 해당 단어를 chose_word라는 변수를 담으시오



#todo -2 :사용자에게 알파벳 하나 추측 해서 입력 하라고 요청하고, 이를 guess 변수에 담으시오. 그리고 대문자로 입력하는 경우를 방지 하기 위해 imput()함수 뒤에 .lower()적용

# chosen_word = random.choice(word_list)
# print(chosen_word)
#
#
# guess = input("알파벳을 입력하세요 >>>" ).lower()
# print(guess)

#todo -3 : guess에서 입력한 문자 하나가 chosen_word의 str문자열 중에 하나의 문자와 일치하는지 반복문을 통해 확인 하고 프로그램으로 작성 맞으면 정답 틀리면 오답이라고 출력 되게


'''
calem

알파벳 입력 : a
정답

알파벳 입력 : n
오답
'''
# for i in range(len(chosen_word)):
#     if guess == chosen_word[i]:
#         print("정답")
#     else:
#         print("오답")
# for letter in chosen_word:
#     if guess == letter:
#         if guess == chosen_word
#             print("정답")
#             else:
#             print("오답")