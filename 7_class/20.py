class Movie:
    count = 0

    def __init__(self, title, audience):
        self.__title = title
        self._audience = audience
        Movie.count += 1

    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title

    def get_audience(self):
        return self._audience

movie1 = Movie("파묘", 100)
# print(movie1.__title)
print(movie1.get_title())
# movie1.__title = "오겜"
# print(movie1.get_title())
# print(movie1.__title) # private
# print(Movie.count)
movie1.set_title("해리포터")
print(movie1.get_title())
print(movie1._audience)
print(movie1.get_audience())


