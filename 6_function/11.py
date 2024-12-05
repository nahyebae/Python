# # 함수
# def f(x):
#     return x**2 + 2*x + 1

# print(f(3))

# def sayHi():
#     print("Hi")
#     print("Hi")
#     print("Hi")

# sayHi()

# # 지역변수, 전역 변수
# x = 10

# def func2():
#     print("func2", x)
#     # print(y)
    
# def func():
#     x = 20
#     y = 11 
#     print("func", x, y)
#     func2()

# func()
# print("main", x)
# # print("main", y) # 밖에서는 y 호출 안됨

# func2()

# def func3(x):
#     print("func3", x)

# func3(3)

# # 매개변수로 리스트
# def times(l):
#     l2 = [i*2 for i in l]
#     return set(l2)

# v2 = times([1,2,3,4,5])
# print(v2)

# # 2개 리턴 가능
# def sum_mul(a, b):
#     sum = a + b
#     mul = a * b
#     return sum, mul

# s, m = sum_mul(2, 3)
# print(s, m)

def oneUp():
    global x
    x = x + 1
    return x

x = 0
print(oneUp())
print(oneUp())
print(oneUp())