import datetime

now = datetime.datetime.today()

print(now)
print(now.year, now.month)

print(f"{now.hour}시 {now.minute}분 {now.second}초")

today = datetime.date.today()
print(today.year)
# print(today)
# today.hour 안됨

# age = int(input("나이 입력 : "))

# result = today.year + (100 - age)
# print("100세 되는 해는 "+ str(result)+"년 입니다.")

# 지나온 날짜 계산하기
import datetime

print("지금까지 몇 일?")
first_day = datetime.date(2000, 8, 12)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today - first_day
print(passed_time)
print(f"개강 이후 {passed_time.days}일 지났습니다.")