# 실습 1
def f(x,y):
    if x == y:
        print(f"결과(곱): {x*y}")   
    else:
        print(f"결과(합): {x+y}")   

f(2, 2)
f(2, 3)    

# 실습 2
def f2(price, quantity):
    order_price = price * quantity 
    if order_price < 20000:
        order_price += 2500 # 배송비
    return order_price

print(f"상품1 가격: {f2(15000,2)}원")
print(f"상품2 가격: {f2(15000,1)}원")

# 실습 3. 자판기 프로그램 함수화
vending_machine = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']

# 남은 음료수를 확인하는 함수
def check_machine():
    print(f"남은 음료수: {vending_machine}\n")

# 음료수가 있는지 확인하는 함수
def is_drink():
    if drink in vending_machine:
        print(f"{drink} 드릴게요")
    else:
        print("없음")

# 음료수를 추가하는 함수
def add_drink():
    drink = input("추가할 음료? ")
    vending_machine.append(drink)
    vending_machine.sort()
    print("추가완료")

# 음료수를 제거하는 함수
def remove_drink():
    if drink in vending_machine:
        vending_machine.remove(drink)
        print("삭제완료")
    else:
        print("없음")

check_machine()
user = input("사용자 종류를 입력하세요: \n1.소비자\n2.주인\n")

if user == "1" or user == "소비자": # 소비자
    drink = input("마시고 싶은 음료? ")
    is_drink()
    remove_drink()
    check_machine()

elif user == "2" or user == "주인": # 주인
    master = input("할 일 선택: \n1.추가\n2.삭제\n")

    if master == "1" or master == "추가": # 추가
        check_machine()
        add_drink()
        check_machine()

    elif master == "2" or master == "삭제": # 삭제
        check_machine()
        drink = input("삭제할 음료? ")
        remove_drink()
        check_machine()
    else:
        print("잘못된 값입니다.")
else:
    print("잘못된 값입니다.")


# 실습 4. 스택
import sys
n = int(sys.stdin.readline())
stack = []

def push(p):
    stack.append(p)

def pop():
    if len(stack) != 0:
        a = stack.pop()
        print(a)
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) != 0:
        print(stack[-1])
    else:
        print(-1)

for i in range(n):
    s = sys.stdin.readline().split()

    if s[0] == "push":
        push(s[1])
    elif s[0] == "pop":
        pop()
    elif s[0] == "size":
        size()
    elif s[0] == "empty":
        empty()
    elif s[0] == "top":
        top()

for i in range(n):
    s = sys.stdin.readline().split()

    match s[0]:
        case "push":
            push(s[1])
        case "pop":
            pop()
        case "size":
            size()
        case "empty":
            empty()
        case "top":
            top()

# 실습 5
def get_times(n):
    global count
    for i in range(1,31):
        if i % n == 0:
            print(i, end = " ")
            count = count + 1

count = 0
n = 3
get_times(n)
print(f'\n{n}의 배수의 개수: {count}')