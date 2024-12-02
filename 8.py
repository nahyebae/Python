# # 과제 2. 자판기 프로그램
# vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
# drink = input("마시고 싶은 음료? ")

# if drink in vending_machine:
#     print(f"{drink} 드릴게요\n")
# else:
#     print(f"{drink}는 지금 없네요\n")


# 과제 3. 자판기 프로그램 응용
vending_machine = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']
print(f"남은 음료수: {vending_machine}\n")
user = input("사용자 종류를 입력하세요: \n1.소비자\n2.주인\n")

if user == "1" or user == "소비자": # 소비자
    drink = input("마시고 싶은 음료? ")
    if drink in vending_machine:
        vending_machine.remove(drink)
        print(f"{drink} 드릴게요")
        print(f"남은 음료수: {vending_machine}")
    else:
        print("없음")
elif user == "2" or user == "주인": # 주인
    master = input("할 일 선택: \n1.추가\n2.삭제\n")
    if master == "1" or master == "추가": # 추가
        print(f"남은 음료수: {vending_machine}\n")
        drink = input("추가할 음료? ")
        vending_machine.append(drink)
        vending_machine.sort()
        print("추가완료")
        print(f"남은 음료수: {vending_machine}")

    elif master == "2" or master == "삭제": # 삭제
        print(f"남은 음료수: {vending_machine}\n")
        drink = input("삭제할 음료? ")
        if drink in vending_machine:
            vending_machine.remove(drink)
            print("삭제완료")
            print(f"남은 음료수: {vending_machine}")
        else:
            print(f"{drink}는 지금 없네요")
    else:
        print("잘못된 값입니다.")
else:
    print("잘못된 값입니다.")
    