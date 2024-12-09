class Movie:
    name = ''
    def print_msg(msg):
        print(msg)
    def modify(self, movie):
        self.name = movie
    def print_name(self):
        print(self.name) 

movie1 = Movie()
movie2 = Movie()

Movie.print_msg("print하기")
# Movie.modify(movie1,"print하기2")
movie1.modify("프린트하기3") # self는 자동 할당
movie1.print_name()
movie2.modify("프린트하기4")
print("movie2.name", movie2.name)