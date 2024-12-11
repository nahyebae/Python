# # 실습 2 슈퍼마켓
# class Supermarket:
#     count = 0
#     def __init__(self,location, name, product, customer):
#         self.__location = location
#         self.__name = name
#         self.__product = product
#         self.__customer = customer
#         Supermarket.count += 1

#     def print_location(self):
#         print(f"위치 : {self.__location}")
    
#     def change_category(self, product):
#         self.__product = product

#     def show_list(self):
#         print(f"구매 가능 : {self.__product}")
    
#     def enter_customer(self):
#         self.__customer += 1

#     def show_info(self):
#         print(f"가게 이름: {self.__name}\n위치: {self.__location}\n파는 물건: {self.__product}\n손님 수: {self.__customer}")
    
#     def show_supermarket_count():
#         print(f"인스턴스 수: {Supermarket.count}") 
    
# super1 = Supermarket("대구","이마트","딸기",200)
# super2 = Supermarket("마포","홈플러스","포도",100)

# super1.print_location()  
# super1.show_list()   
# super1.change_category("시리얼")     
# super1.enter_customer()    
# super1.show_info()   
# Supermarket.show_supermarket_count()

# 실습 3
class Calculator():
    def __init__(self):
        self.value = 100

    def sub(self, value):
        self.value -= value

class MinLinitCalculator(Calculator):
    def sub(self,value):
        self.value -= value
        if self.value < 0:
            self.value = 0

cal = MinLinitCalculator()
cal.sub(20)
cal.sub(90)
print(cal.value)