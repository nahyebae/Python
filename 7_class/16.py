a = dict()
a = set()

class b: # 붕어빵 틀
    pass

bb1 = b() # 붕어빵
bb2 = b()
bb3 = b()

class Movie:
    title = "범죄도시4"

movie1 = Movie()
movie2 = Movie()

print(movie1.title)
print(movie2.title)

movie1.title = "나홀로집에"
print(movie1.title)
print(movie2.title)

movie1.score = "1" # 가능
print(movie1.score)
# print(movie2.score) # 1에만 score가 만들어져서 에러남