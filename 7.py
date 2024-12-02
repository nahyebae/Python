print(1==2)

x = 2
print(1<x<3)

print(True and False) # &&
print(True or False) # ||
print(not True) # !

cart = ["계란", "마늘", "콩나물", "커피"]
print("두부" in cart)
print("계란" in cart)

if 1 < 3:
    print("True")
    print("True")
else:
    print("False")

# 실습 3
a = int(input())

if a % 2 == 0:
    print("짝수")
if a % 2 != 0:
    print("홀수")

# 실습 4
score = int(input("점수: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")

score = int(input("점수: "))
if score > 100:
    print("만점은 100점입니다. 다시 입력하세요.")
elif score < 60:
    print("E")
elif score < 70:
    print("D")
elif score < 80:
    print("C")
elif score < 90:
    print("B")
else:
    print("A")

# 실습 5
age = int(input("나이를 입력하세요: "))

if age >= 75 or age < 8:
    print(f"{age}세의 요금은 무료입니다.")
elif age < 14:
    print(f"{age}세의 요금은 450원 입니다.")
else:
    pay = input("'카드' 또는 '현금'만 입력: ")

    if pay == "카드":
        if age < 20:
            fee = 720
        else:
            fee = 1200

    elif pay == "현금":
        if age < 20:
            fee = 1000
        else:
            fee = 1300
    else:
        print("다시 입력해주세요.")

    print(f"{age}세의 {pay} 요금은 {fee}원 입니다.")