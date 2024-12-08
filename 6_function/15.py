# l = ["p","y","t","h","o","n"]
# print("".join(l)) # join: 여러개의 스트링을 합침 <-> split랑 반대 


# print(list(map(lambda x:3*x, [1,2,3,4])))
# print(list(map(int, input().split()))) # 1 2 3 4 5

# print(1 if 1>0 else 0)
# print("abc" if 1<0 else "bcd")

# if 1<0:
#     print("abc")
# else:
#     print("bcd")

# # https://school.programmers.co.kr/learn/courses/30/lessons/181882
# # 조건에 맞게 수열 변환하기 1
# def solution(arr):
#     answer = []
#     for i in arr:
#         if i >= 50 and i % 2 ==0:
#             answer.append(i/2)
#         elif i < 50 and i % 2 == 1:
#             answer.append(i*2)
#         else:
#             answer.append(i)
#     return answer

# # https://school.programmers.co.kr/learn/courses/30/lessons/181867
# # x 사이의 개수
# def solution(myString):
#     answer = []
#     a = myString.split("x")
#     for i in a:
#         answer.append(len(i))
#     return answer

# # https://school.programmers.co.kr/learn/courses/30/lessons/181842
# def solution(str1, str2):
#     answer = 0
#     if str1 in str2:
#         answer = 1
#     else:
#         answer = 0
#     return answer

# # https://school.programmers.co.kr/learn/courses/30/lessons/12910?language=python3
# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
#             answer.sort()
#     if len(answer) == 0:
#         answer.append(-1)
#     return answer

# # https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=python3
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)-1):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] + numbers[j] not in answer:
#                 answer.append(numbers[i]+ numbers[j])
#                 answer.sort()
#     return answer

# # https://school.programmers.co.kr/learn/courses/30/lessons/120880?language=python3

# # https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=python3
# def solution(x):
#     l = sum(list(map(int, str(x))))
#     if x % l == 0: 
#         answer = True
#     else:
#         answer = False
#     return answer

# # https://school.programmers.co.kr/learn/courses/30/lessons/12917?language=python3
# def solution(s):
#     l = list(s)
#     l.sort()
#     l.reverse()
#     answer = ''.join(l)
#     return answer

# # https://school.programmers.co.kr/learn/courses/30/lessons/176963
# def solution(name, yearning, photo):
#     answer = []
#     for i in range(len(photo)):
#         result = 0
#         for j in range(len(photo[i])):
#             if photo[i][j] in name:
#                 result += yearning[name.index(photo[i][j])]
#         answer.append(result)
#     return answer

# # https://school.programmers.co.kr/learn/courses/30/lessons/120956?language=python3

# # https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3
# def solution(t, p):
#     answer = 0
#     for i in range(len(t)-len(p)+1):
#         l = t[i:len(p)+i]
#         print(l)

#         if l <= p:
#             answer += 1
    
#     return answer


# # 콜라츠 수열만들기 https://school.programmers.co.kr/learn/courses/30/lessons/181919
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


# # Zip 쓰는 법
# a = [1,2,3,4]
# b = ["a","b","c","d"]
# c = list(zip(a,b))
# print(c)
# d = dict(zip(a,b))
# print(d)