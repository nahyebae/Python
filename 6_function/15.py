l = ["p","y","t","h","o","n"]
print("".join(l)) # join: 여러개의 스트링을 합침 <-> split랑 반대 


print(list(map(lambda x:3*x, [1,2,3,4])))
print(list(map(int, input().split()))) # 1 2 3 4 5

print(1 if 1>0 else 0)
print("abc" if 1<0 else "bcd")

if 1<0:
    print("abc")
else:
    print("bcd")

# Zip 쓰는 법
a = [1,2,3,4]
b = ["a","b","c","d"]
c = list(zip(a,b))
print(c)
d = dict(zip(a,b))
print(d)