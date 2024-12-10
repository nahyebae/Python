# 실습 1
import random

com = random.randint(1,100)
# print("랜덤수: ", com)

min_v = 1
max_v = 100
score = 100
count = 0
while count < 10:
    try:
        count += 1
        guess = int(input(f"숫자 입력([{count}회] {min_v} ~ {max_v}): "))

        if guess < 0 or guess > 100:
            print("입력 범위를 초과했어요")
        elif com == guess:
            print("정답이에요!!")
            print(f"정답: {guess}")
            print(f"점수: {score-(count)*10}점")
            break
        elif com > guess:
            print("랜덤수보다 작아요")
            min_v = guess
        else:
            print("랜덤수보다 커요")
            max_v = guess
    except ValueError:
        print("숫자만 입력 가능합니다.")


# 실습 2. 로또 번호 뽑기
import random
lotto = []

while len(lotto) < 6:
    n = random.randint(1,45)
    if n not in lotto:
        lotto.append(n)

lotto.sort()
print(f"로또 번호: {lotto}")

# 방법 3
lotto = random.sample(range(1,46), 6)
print(sorted(lotto))