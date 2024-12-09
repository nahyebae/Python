class Calculator:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def add(self):
        return self.__a + self.__b
    
    def sub(self):
        return self.__a - self.__b
    
    def mul(self):
        return self.__a * self.__b
    
    def div(self):
        if self.__b == 0:
            return "None"
        else:
            return self.__a / self.__b
        
t1 = Calculator(4,0)
print(f"add: {t1.add()}")
print(f"sub: {t1.sub()}")
print(f"mul: {t1.mul()}")
print(f"div: {t1.div()}")