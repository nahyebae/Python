# 조건에 맞게 수열 변환하기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181882
def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 ==0:
            answer.append(i/2)
        elif i < 50 and i % 2 == 1:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer

# x 사이의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/181867
def solution(myString):
    answer = []
    a = myString.split("x")
    for i in a:
        answer.append(len(i))
    return answer

# 부분 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181842
def solution(str1, str2):
    if str1 in str2:
        return  1
    else:
        return  0

# 나누어 떨어지는 숫자 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/12910?language=python3
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer

# 두개 뽑아서 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=python3
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i]+ numbers[j])
                answer.sort()
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/120880?language=python3

# 하샤드 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=python3
def solution(x):
    l = sum(list(map(int, str(x))))
    if x % l == 0: 
        answer = True
    else:
        answer = False
    return answer

# 문자열 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12917?language=python3
def solution(s):
    l = list(s)
    l.sort()
    l.reverse()
    answer = ''.join(l)
    return answer

# 추억 점수
# https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        result = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                result += yearning[name.index(photo[i][j])]
        answer.append(result)
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/120956?language=python3

# 크기가 작은 부분문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3
def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        l = t[i:len(p)+i]
        print(l)

        if l <= p:
            answer += 1
    return answer

# 콜라츠 수열만들기 
# https://school.programmers.co.kr/learn/courses/30/lessons/181919
answer = []
def solution(n):
    if n == 1:
        print(1)
        return answer.append(1)
    
    elif n % 2 == 0:
        answer.append(int(n))
        print(n, "짝수")
        n = n / 2
        solution(n)
        return answer

    elif n % 2 != 0:
        answer.append(int(n))
        print(n, "홀수")
        n = 3 * n + 1
        solution(n)

    return answer
solution(10)

# 다른 방법 
def solution(n):
    answer = []

    def collat(x):
        answer.append(x)
        if x == 1:
            return
        elif x%2==0:
            collat(x/2)
        else:
            collat(x*3+1)
    collat(n)
    return answer

# 특이한 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/120880?language=python3
def solution(numlist, n):
    answer = []
    d = {}
    for i in numlist:
        d[i] = abs(i-n)
    d1 = sorted(d.items(), key = lambda items:(items[1], - items[0]))
    print(d.items())
    print(d1)
    
    for i in d1:
        answer.append(i[0])
    return answer

# 옹알이 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/120956?language=python3
def solution(babbling):
    answer = 0
    
    can = ["aya","ye","woo","ma"]
    
    for i in babbling:
        for j in can:
            idx = i.find(j)
            if idx > -1:
                print(idx, i, j)
                i = i.replace(j, '_')
                print(idx, i, j)
        i = i.replace('_','')
        if len(i) == 0:
            answer += 1
    return answer

# 하노이 탑
# https://school.programmers.co.kr/learn/courses/30/lessons/12946
def solution(n):
    answer = []

    def hanoi(n, f, t, v):
        if n == 1:
            answer.append([f,t])
        else:
            hanoi(n-1,f,v,t)
            answer.append([f,t])
            hanoi(n-1,v,t,f)

    hanoi(n, 1, 3, 2)

    return answer