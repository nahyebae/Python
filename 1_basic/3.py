song = input("너의 최애 노래는?")
print(song)
print(type(song))

a = input("1+1=?")
print(a)
print(int(a)*2) 
number = int(input())

a = 2
print(str(2)*10)
print(str(2)+"입니다")
print(2+"입니다") # 에러

print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"\`   |')
print("||_/=\\\__|")

# 실습3
name = input("이름을 입력하세요. ")
age = int(input("나이를 입력하세요. "))
print("안녕하세요! "+ name + "님 " + "(" + str(age) + "세)\n")
print("")


name = input("이름을 입력하세요. ")
birth = int(input("태어난 년도를 입력하세요. "))
year = int(input("올해 년도를 입력하세요. "))
print("올해는"+ str(year) +"년 ,"+ name +"님의 나이는"+ str(year-birth+1) + "세 입니다")
