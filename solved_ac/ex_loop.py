# 2741
n = int(input())

for i in range(n):
    i += 1
    print(i)

# 10872
n = int(input())
p = 1
for i in range(1,n+1):
    p = i * p
print(p)

# 10950
t = int(input())

for i in range(t):
    a, b = map(int,input().split())
    print(a+b)

# 10952
a, b = map(int,input().split())

while a != 0 and b != 0:
    print(a+b)
    a, b = map(int,input().split())

# 2739
n = int(input())

for i in range(1,10):
    d = n * i
    print(f"{n} * {i} = {d}")

# 2438
n = int(input())

for i in range(1,n+1):
    print("*"*i)

# 10951
while True:
    try:
        a, b = map(int,input().split())
        print(a+b)
    except:
        break