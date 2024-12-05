# 튜플
t1 = (10, 20, 30)
print(type(t1))
print(t1)
print(t1[0])

# del t1[0] 특정 원소 삭제 안됨
# t1[0] = 3 튜플 요소 변경 안됨
del t1

t2 = (10)
t3 = (10,)
t4 = 10, 20, # 콤마 있으면 튜플
print(type(t4))

# 셋(set)
set1 = {1, 2, 3, 3}
print(set1)
set2 = set([1, 2, 3, 3])
print(set2)

set2.add(4)
print(set2)

while len(set2) > 0:
    a = set2.pop()
    print(a)
 
l1 = [1, 2, 3, 4]
while len(l1) > 0:
    a= l1.pop()
    print(a)

set3 = set("apple")
print(set3)
while len(set3) > 0:
    a= set3.pop()
    print(a)

# set 응용 - 중복이름 찾기
name = ["1","2","3","2"]
a = []
for i in range(len(name)):
    if a.count(name[i]) < 1:
        # print(name[i])
        # name.remove(name[i]) # 반복중에 range 바꾸면 에러남
        a.append(name[i])
print(a) 

# name_set = set(name)
# print(name_set)
# name_list= list(name_set)
# name_list.sort()
# print(name_list)

# 딕셔너리
a = {} 
print(type(a)) # dictionary
b = {1}
print(type(b)) # set
c = dict()
c = {1:'a', 'b':'b'}
print(c)
c[2] ='c'
c['c'] = 2
print(c)
del c[2]
del c['b']
print(c)
# print(c[2]) # 에러
print(c.get(2)) # None
print(c.keys()) # 키값
print(c.values()) # 값

for i in c.keys():
    print(i, c.get(i))

# for i in c.values():
#     print(i, c.get(i))

print('c' in c) # print('c' in c.keys())
print('c' in c.values())

# 2차원 리스트
d = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(d)
print(d[0][0])
d.append([70,80])
print(d)
d[0][0] = 90
print(d)

# d[1].pop(1)
# del(d[1][1])
print(d)
# print(d[1][1])
print(len(d))
print(len(d[0]))

for i in range(0,len(d)):
    for j in range(0,len(d[i])):
        print(d[i][j], end = " ")
    print()

for x, y in d:
    print(x, y)