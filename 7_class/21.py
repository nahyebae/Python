class MyAdd:
    __a = 1
    __b = 2

    #######메소드 구현
    def set_a(self,a):
        self.__a = a
    
    def sum(self):
        return self.__a + self.__b
    
        
a = MyAdd()
print(a.sum()) # 3
# a 값 3으로 변경
a.set_a(3) 
print(a.sum()) # 5