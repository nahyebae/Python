# while 문
i = 0
while i < 5:
    i += 1
    print(i)
print('끝')

# 이중 for문-구구단 전체
for y in range(3):
    for x in range(2):
        print(f"y: {y}, x: {x}")
    print()

for i in range(2, 10):
    print(f'[{i} 단]')
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j}')
    print()

# 행 입력
print('*** 자리배치도 ***')
customer = int(input('고객수 입력: '))
row = int(input('좌석행 수 입력: '))

if customer % row == 0:
    column = customer // row
else:
    column = (customer // row) + 1
# print(row)

for i in range(0, row):
  for j in range(1, column + 1):
    seat = i * column + j
    if seat > customer:
      break
    print(seat, end=" ")
  print()
