import random

stages = '''
====
=
====
   =
====
''' '''
   =
  ==
 = =
====
   =
''' '''
====
   =
====
   =
====
''' '''
====
   =
====
=
====
''' '''
=
=
=
=
=
'''














end_of_game = False
lives = 6
word_list = ["apple","banana", "camel"]
chose_word = random.choice(word_list)
print(f"테스트 코드 : {chose_word}")
display = []
for _ in range(len(chose_word)):
                display.append("_")



while not end_of_game:
    print(stages[lives])
    guess = input("알파벳 입력>>>>>").lower()

    for _ in range(len(chose_word)):
        if chose_word[_] == guess:
            display[_] = guess
        # else:
        #     lives -= 1
        #     print(f"당신의 기회는 {lives}번 남았습니다")
        #     if lives == 0:
        #         print("모든 기회를 잃었습니다.")
        #         end_of_game = True

        #이렇게 치면 알파벳 하나 입력시 모든 단어를 한번씩 다 확인 함으로 한번만 입력해도 여러번 - 됨
    if guess not in chose_word:
        lives -= 1
        print(f"당신의 기회는 {lives}번 남았습니다")
        end_of_game = True
        print(f"정답은 {chose_word}입니다")
        if "_" not in display:
            print("정답입니다!!:")
            end_of_game = True
    print(display)
    print(" ".join(display))
# 1.로고
# 2.word_list가 부족
#3.테스트 해 보고 유지 보수 확인할 필요거있음



