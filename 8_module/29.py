# time 모듈
import time

# a = time.time()
# time.sleep(2) # 2초 쉬기
# b = time.time()
# print(b-a)

print(time.localtime())
time_str = time.localtime()
print(time_str.tm_year)

print(time.ctime())
# print(time.ctime(a))
# print(time.ctime(b))

# 1970년 1월 1일 기준
year = time.time()/(365*24*60*60) # 1년을 초로 바꾼 것
print(year)
day = time.time()/(24*60*60)
print(day)

start = time.time()

for i in range(10):
    print(i)
    time.sleep(1)

end = time.time()
print(f"수행 시간 : {end-start}초")

# 함수로 만들기
def check_time(func):
    start = time.time()
    func()
    end = time.time()
    print(f"수행 시간 : {end-start}초")

def a():
     for i in range(10):
        print(i)
        time.sleep(1)

def b():
     for i in range(100):
        print(i)
        time.sleep(0.5)

# check_time(a)
check_time(b)