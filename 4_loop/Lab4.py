# 실습. 홀수 출력
num = 0
while num < 10:
    num = num + 1
    if num % 2 == 0:
        continue
    print(num)

# 실습 1. for
n = int(input("어디까지 계산할까요? "))
sum = 0
sum_odd = 0
for i in range(1, n+1):
    sum += i
    if i % 2 != 0: # 홀수의 합
        sum_odd += i
print(sum)
print(sum_odd)

# 실습 2.
n = int(input("몇 초?: "))
for i in range(n,0,-1):
    print(i, end=" ")
print("발사!!")

# 실습 3. 구구단 만들기
n = int(input("몇 단을 출력할까요? "))
for i in range(1,10):
    print(f"{n} * {i} = {n*i}")

a = [10, 20, 30]
print(sum(a)/len(a)) # 평균 구하기
sum = 0
for i in a:
    sum+=1
print(sum)

a = [1, 2, 3, 4, 5]
a2 = []
a3 = []
a4 = []

a3 = [i * 3 for i in a]
print(a3)

a4 = [i*3 for i in a if i % 2 == 0] # 짝수만
print(a4)

# 실습 4
n = int(input("몇 줄? "))
for i in range(n):
        print("*"* (i+1))

n = int(input("몇 줄? "))
for i in range(n):
        print(" "* (n-(i+1)) + "*"* (i+1))

n = int(input("몇 줄? "))
for i in range(n):
        print(" "* ((n-1)-i) + "*" * (2*i+1))

# 실습 5. 리스트 평균 구하기
n = input("숫자 여러 개 입력 > ").split()
n_list = []
for i in n:
    n.append(int(i))
print(n)

n_max = max(n)
n_min = min(n)

print(f"가장 큰 값: {n_max}")
print(f"가장 작은 값: {n_min}")

n.remove(n_max)
n.remove(n_min)

avg = sum(n)/len(n)
print(f"나머지 값의 평균: {avg}")

# a = list(i for i in range(5))
# b = list(map(int, input().split()))