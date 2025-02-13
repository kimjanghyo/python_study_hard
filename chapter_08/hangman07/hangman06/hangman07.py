# from random import choice
#
# from hangman_arts import logo, stages
#
# from hangaman_word_list import word_list
# '''
#
# import 문 학습
# import문을 단독으로 쓸 경우에는 모듈.변수명  혹은 모듈명.메서드명()
# from - import문을 쓰게 될 경우 모듈명 생략
#
# from - import의 경우
# from a import a,b,c의 경우 그나마 낫지만
# * 개념과 합쳐졌을때는 가독성이 매우 떨어진다는 단점
#
#
# 마찬가지로
# from rnandom import choice의 경우에도 해당 메서드 하나만 창조했기 때문에 별 문제가 없지만
# '''
# end_of_game = False
# lives = 6
#
# chosen_word = choice(word_list)
# print(f"테스트 코드 : {chosen_word}")
# display = []
#
# for letter in chosen_word:
#     display.append("_")
#
# print(logo)
# while not end_of_game:
#
#     guess = input("알파벳 입력하세요 >>> ").lower()
#
#     for i in range(len(chosen_word)):
#         if chosen_word[i] == guess:
#             display[i] = guess
#
#     if guess not in chosen_word:
#         lives -= 1
#         print(f"당신의 기회는 {lives}번 남았습니다.")
#         if lives == 0:
#             print("모든 기회를 잃었습니다.")
#             end_of_game = True
#             print(f"정답은 {chosen_word}입니다.")
#
#     if "_" not in display:
#         print("정답입니다:)")
#         end_of_game = True
#
#     print(" ".join(display))
#     print(stages[lives])
