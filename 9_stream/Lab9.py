# # 실습 1. 회원 명부 작성하기
# with open("member.txt","w") as f:
#     for i in range(3):
#         name = input("이름 : ")
#         password = int(input("비밀번호: "))
#         f.write(f"{name} {password}\n")

# with open("member.txt","r") as f:      
#     print(f.read())

# # 실습 2. 회원 명부를 이용한 로그인 기능
# name = input("이름을 입력하세요.\n")
# password = input("비밀번호를 입력하세요.\n")
# with open("member.txt","r") as f:
#     for i in f:
#         a, b = i.split()
#         if a == name and b == password:
#             print("로그인 성공")
#             break
#         else:
#             print("로그인 실패")
#             break

# # 딕셔너리 풀이
# dic = {}

# with open("member.txt","r") as f:
#     for line in f:
#         n, p = line.split()
#         dic[n] = p
# print(dic)

# name = input("이름을 입력하세요.\n")
# pw = input("비밀번호를 입력하세요.\n")

# if pw == dic.get(name):
#     print('로그인 성공')
# else:
#     print('로그인 실패')

# 실습 3. 로그인 성공 시 전화번호 저장하기
dic = {}

with open("member.txt","r") as f:
    for line in f:
        n, p = line.split()
        dic[n] = p
print(dic)

name = input("이름을 입력하세요.\n")
pw = input("비밀번호를 입력하세요.\n")

if pw == dic.get(name):
    print('로그인 성공')
    number = input("전화번호를 입력하세요.\n")
    
    if name in f:
        with open("member_tel.txt","a") as f2:
            f2.write(number)
    else:
        with open("member_tel.txt","w") as f2:
            f2.write(name)
            f2.write(number)
else:
    print('로그인 실패')


name = input("이름을 입력하세요.\n")
password = input("비밀번호를 입력하세요.\n")
with open("member.txt","r") as f:
    for i in f:
        a, b = i.split()
        if a == name and b == password:
            print("로그인 성공")
            number = input("전화번호를 입력하세요.\n")
            if name in f:
                with open("member_tel.txt","a") as f2:
                    f2.write(number)
            else:
                with open("member_tel.txt","w") as f2:
                    f2.write(name)
                    f2.write(number)

    else:
        print("로그인 실패")

