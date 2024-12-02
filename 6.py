print("오늘은 12월 %d일 입니다." % 2)
print("오늘은 %d월 %d일 입니다." % (12,2))
print("오늘은 %d%s %d일 입니다." % (12,'월',2))
print(f"오늘은 {12}{'월'} {2}일 입니다.")
print("오늘은 " +str(12)+"월 "+str(2)+"일 입니다.")
print("오늘은 ",12,"월 ",2,"일 입니다.",sep="")

print("Hello".upper())
print("Hello".lower())

friends = "고찬국 김다운 김민창"
a = friends.split("김") # '김' 기준으로 나누어짐
print(a)

sentence = "{1}월 {0}일".format(12,2) # {}안에 숫자 넣으면 순서 조절 가능
print(sentence)

b = "   111   222   "
print(b.strip()) # strip() 좌우 공백 제거
print(b.split())
print(b.replace("111","222"))


# 실습 2
a =  int(input())
b =  input()
print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))
