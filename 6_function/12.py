# 함수 매개변수
def pr_str(txt, count = 1, count2 = 1): # 디폴트가 무조건 앞에 있어야 함
    for i in range(count):
        print(txt)
        print(count2)

pr_str("Hello", 3, 2)
print()
pr_str("Hello", 3)
print()
pr_str("Hello")
print()
# pr_str() # txt = '12'
# l = []
# l.pop()

print(1,2,3,4)

pr_str("234", count2 = 1)

def calc_avg(*numbers): # 튜플(수정 못하게 하려고 사용)
    print(type(numbers))
    print(numbers)
    return sum(numbers)/len(numbers)

print(calc_avg(1,2))
print(calc_avg(1,2,3,4,5))

# # *없을 경우
# print(calc_avg({1,2}))
# print(calc_avg({1,2,3,4,5}))

def a():
    return 1,2 # 두개 리턴하면 튜플로 출력

print(a())

# 가변 키워드 매개변수
def intro(**kw):
    print(type(kw))
    for k, v in kw.items(): # items key랑 value 같이 얻기
        print(f"{k}: {v}")
    for i in kw:
        print(f"{i}")
        
intro(name = "Alice", age = 25, city = "NY")

list = [2,4,1,4,5,6]
list.sort() # 원본 변환
print("list", list)
list2 = [2,4,1,4,5,6]
print("sorted list2", sorted(list2)) # 리턴값이 리스트, 원본을 변환시키지 않는다
print("list2", list2)

# 세번째로 작은 값의 인덱스를 구하라
# 정렬하고 그 값은 원본에서 찾으면 됨
print(sorted(list2)[2])

print(eval("1+2*2")) # 계산기 

print(int(4.6+0.5)) # 함수 안쓰고 반올림
print(int(4.4+0.5))
print(round(4.5)) # banker's round
print(int(4.5+0.5))

print(round(2.547)) # 
print(round(2.547, 1)) # 
print(round(2.547, 2)) # 
print(round(127, -1)) # 1의 자리 반올림
print(round(127, -2)) # 2의 자리 반올림
print(round(127)) 

print(2**3)
print(pow(2,3))