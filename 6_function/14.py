add = lambda x, y : x+y
print(type(add))
print(add(1,2))

def add2(x,y):
    return x+y

add3 = add2
print(add2(1,2))
print(add3(1,3))

def call_3(func):
    for i in range(3):
        func()

call_3(lambda:print("hi"))
call_3(lambda:print("hello"))

def download(staredCallback, endedCallback):
    staredCallback()
    # download
    print("download 중")
    ###
    ###
    endedCallback()

download(lambda:print("다운로드 시작"), lambda:print("완료되었습니다."))

# map()
list(map(int, ["1","2","3","4"]))

result = map(lambda x:3*x, [1,2,3,4])
print(list(result))

# filter() True 값만 출력
li = [-5,1,2,-11,76]

value = list(filter(lambda x:x<0,li)) 
print(value) # [-5, 11]

value = list(filter(lambda x:x>10,li)) 
print(value) # [76]

print(list(filter(lambda x:x >= 3, map(lambda x : 2*x,li))))
