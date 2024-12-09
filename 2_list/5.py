a = [3,4,2,1] # 숫자 정렬
a.sort()
# a.sort(reverse = True)
a.reverse()
print(a)

b = ["a", "c", "b", "d"]
b.sort()
print(b)

c = ["1","10", "2", "11"] # 문자 정렬
c.sort()
print(c)

d = ["강남", "강북", "서", "asdfd", "서","서"] 
# d.sort()
# print(d)
first = d.index("서")+1
print(first + d[first:].index("서"))
print(d.count("서"))

# 실습1
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# 1. 2번 인덱스 값 출력
print(rainbow[2])

# 2. 알파벳 순서로 정렬한 값 출력
rainbow.sort()
print(rainbow)

# 3. 좋아하는 색 맨 마지막에 추가하기
rainbow.append('pink')
print(rainbow)

# 4. 3~6번째 값 삭제하기
del rainbow[3:7]
print(rainbow)

# index, pop, count 해보기
print(rainbow.index("pink"))

rainbow.pop(2) # 요소 삭제

# count 개수 세기
print(rainbow.count("blue"))
