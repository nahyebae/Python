dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}


print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")
if word in dic:
    print(f'{word}: {dic[word]}')
else:
    print("정의된 단어가 없습니다.")

# 실습 1. set 사용
N, M = map(int, input().split())
# S = set()
# S = list()
S = dict()

for i in range(N):
    # S.add(input())
    # S.append(input())
    S[input()] = True

count = 0

for i in range(M):
    str = input()
    if str in S:
        count += 1

print(count)

# 실습 2. 딕셔너리 사용
score = dict()
score = {'Alice':85,'Bob':90,'Charlie':95}
print(dict)

score['David'] = 80 # 학생 추가
score['Alice'] = 88 # 점수 수정
print(dict)

del(score['Bob']) # 학생 삭제
# a = dict.pop("Bob")
# print("Bob", a)

# 전체 출력
for i in score.keys(): 
    print(i, score.get(i))

# 3단
three = [[3,1], [3,2], [3,3], [3,4], [3,5],
         [3,6], [3,7], [3,8], [3,9]]

for x, y in three:
    print(f"{x} x {y} = {x*y}")

for i in three:
    print(f"{i[0]} x {i[1]} = {i[0]*i[1]}")