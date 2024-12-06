# def hello():
#     global n
#     n += 1
#     if n < 4:
#         print("hello")
#         hello()
# n = 0
# hello()

# # 팩토리얼
# n = 5
# factorial = 1

# for i in  range(1,n+1):
#     factorial = factorial * i

# print(factorial)

# # 실습 2. 재귀함수로 피보나치 수 구하기
# def fibo(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibo(n-2) + fibo(n-1)
    
# for i in range(5):
#     print(fibo(i), end = " ")


# # 방법 2
# memory = {1:1, 2:1}

# def fibo_memorization(n):
#     if n in memory:
#         number = memory[n]
#     else:
#         number = fibo_memorization(n-1) + fibo_memorization(n-2)
#         memory[n] = number
#     return number

# print(fibo_memorization(100))
num = int(input("원판 수: "))
def hanoi(number_of_disks_to_move, from_, to_, via_):
    if number_of_disks_to_move == 1:
        print(from_, "->", to_)
    else:
        hanoi(number_of_disks_to_move-1, from_, via_, to_)
        print(from_, "->", to_)
        hanoi(number_of_disks_to_move-1, via_, to_, from_)

hanoi(num, 'A', 'C', 'B')
