class Movie:
    count = 0

    def __init__(self, title, audience):
        self.title = title
        self.audience = audience
        Movie.count += 1
    
movie1 = Movie("파묘", 100)
print(Movie.count)
movie2 = Movie("파묘2", 100)

print(movie1.count)
print(movie2.count)
print(Movie.count)
Movie.count += 1  # 클래스 변수
print(movie1.count)
print(movie2.count)
print(Movie.count)
movie1.count += 1 # 인스턴스 변수
print(movie1.count)
print(movie2.count)
print(Movie.count)
Movie.count += 1
print(movie1.count)
print(movie2.count)
print(Movie.count)