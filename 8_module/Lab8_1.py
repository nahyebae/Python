import random
import time
import os

# word = ['sky','earth','moon','flower','tree','apple','grape','garlic','onion','potato']

# if os.path.exists("word.txt"): # txt파일이 없을 경우 
#     with open("word.txt","r") as f: 
#         word = f.read().split() # 지역변수 아님
# else:
#     word = ['sky','earth','moon','flower','tree','apple','grape','garlic','onion','potato']

with open("word.txt","r") as f: 
        word = f.read().split() # 지역변수 아님

try:
    n = 1 # 문제 번호

    input("[타자 게임] 준비되면 엔터!")
    start = time.time() # 시작 시간

    while n < 11:
        print("문제", n)
        question = random.choice(word)
        print(question) # 문제 출제
        user = input()
        if question == user:
            print("통과!!")
            n += 1 # 다음 문제
        else:
            print("오타! 다시 도전하세요")

    end = time.time() # 종료 시간
    et = end - start
    print(f"타자시간 : {et: .2f}초") # 소수점 둘째자리까지 표시

except:
    print("파일을 찾을 수 없습니다.")