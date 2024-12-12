# f = open("text.txt", "w") # w 새로 작성됨
# print(f.write("Hello World\n")) # 12
# f.close()

# f2 = open("text.txt", "r")
# print(f2.read(3)) # 숫자만큼 읽음
# f2.close()

# f3 = open("text.txt", "a") # 추가
# print(f3.write("Hello World\n")) 
# f3.close()

# f2 = open("text.txt")
# print(f2.read()) 
# f2.close()

# f3 = open("text.txt")
# print(f3.readline(), end="") # readline 한 줄씩 읽기
# print(f3.readline(), end="") # 여러번 실행하면 한 줄씩 흘러나옴
# print(f3.readline(), end="") 
# f3.close()

# f4 = open("text.txt")
# print(f4.readlines())
# f4.close()

# f5 = open("text.txt", "r+") # r+: 저장된거를 수정하기 위함
# print(f5.read())
# print(f5.tell())
# f5.seek(4) # 특정위치로 이동
# print(f5.write("8")) # 처음부터 다시 read 연어처럼 거슬러 올라감
# f5.close()

# f6 = open("text.txt", "r+") 
# str6 = f6.read()
# print(f6.tell())
# f6.seek(str6.find('5')) # find()함수로 5 찾기
# print(f6.write("8")) # 바꾼 갯수
# f6.close()

with open("text.txt", "r+") as f7:
    str6 = f7.read()
    print(f7.tell())
    f7.seek(str6.find("5"))
    print(f7.write("8")) 