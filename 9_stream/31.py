# f = open("text.txt", "w") # w 새로 작성됨
# print(f.write("Hello World\n")) # 12
# f.close()

# f2 = open("text.txt", "r")
# print(f2.read(3)) # 숫자만큼 읽음
# f2.close()

# f3 = open("text.txt", "a") # 추가
# print(f3.write("Hello World\n")) 
# f3.close()

f2 = open("text.txt")
print(f2.read()) 
f2.close()

f3 = open("text.txt")
print(f3.readline(), end="") # readline 한 줄씩 읽기
print(f3.readline(), end="") # 여러번 실행하면 한 줄씩 흘러나옴
print(f3.readline(), end="") 
f3.close()