class Country:
    def __init__(self):
        self.name = "나라이름"
        self.population = "인구"
        self.capital = "수도"

    def show(self):
        print("국가 클래스의 메소드")

class Korea(Country):
    def __init__(self, name):
        self.name = name

    def show(self):
        print("국가 이름:",self.name)

country = Korea("대한민국")
country.show() # 메서드 오버라이딩 부모꺼 말고 내꺼 나옴 덮어쓰기
print(country.name)
# country.show_name()

# 오버로딩
class Calculator():
    def __init__(self):
        self.value = 100

    def sub(self, value):
        self.value -= value

    # 파이썬은 메소드 오버로딩 안됨
    def sub(self):
        self.value -= 10

    # 파이썬은 메소드 오버로딩 안됨
    def sub(self, value1, value2):
        self.value = value1 - value2

    def sub(self, *args):
        self.value = args[0]

a = Calculator()
a.sub(10)
print(a.value)