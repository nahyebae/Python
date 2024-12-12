import random

with open("word.txt","w") as f:
    word = ['sky','earth','moon','flower','tree','apple','grape','garlic','onion','potato']

    for i in word:
        f.write(i + ' ') # \n, \t, \r

with open("word.txt","r") as f: # 확인용
    data = f.read().split()
    # data = f.readlines() # /n인 경우 readlines() 사용 가능
    word = random.choice(data)
    print(word)