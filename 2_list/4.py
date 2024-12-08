a = [] # 0부터 시작
b = [1,2,3,4]
c = ["카리나", "윈터"]
d = [1, "에스파"]

print(len(c))
print(c[0]) # 카리나
print(c[1]) # 윈터
c[0] = "아이유"
print(c)
del c[0]
print(c)
c.append("asdf") # append 추가
print(c)

print(b[-1]) # 뒤에서 첫번째 마이너스는 뒤에서 역순
print(b[-2])
print(type(b))

# 리스트 슬라이싱 n-1까지
seasons = ["봄", "여름", "가을", "겨울"]
print(seasons[0:1])
print(seasons[0:2])
print(seasons[:2])
print(seasons[1:])
print(seasons[2:])
print(seasons[1:3])
print(seasons[:]) 
print(seasons[::2]) # 가을
print(seasons[::-1]) # 뒤집기

seasons2 = ["봄", "여름", "가을", "겨울", [1,2,3,4]]
print(seasons2[-1][0])

abcd = "abcd"
abc = ['a','b','c','d']
print(len(abcd))
print(len(abc))

# a를 이용해서 짝수만 뽑은 리스트 만들기
a = [1,2,3,4,5,6,7,8,9,10]
even = a[1::2]
print(even)