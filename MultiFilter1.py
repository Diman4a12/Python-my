def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]



class multifilter:
    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if self.pos >= neg:
            return self.i
        self.pos = 0	
        self.neg = 0
    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if self.pos >= 1:
            return self.i
        self.pos = 0	
        self.neg = 0
    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if self.neg == 0:
            return self.i
        self.pos = 0	
        self.neg = 0	
    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.i = 0
        self.funcs = mul2(self.iterable[self.i]), mul3(self.iterable[self.i]), mul5(self.iterable[self.i])
        self.pos = 0
        self.neg = 0
    def __next__(self):
        if self.funcs is True:
            self.pos +=1
        else:
            self.neg +=1
        self.i +=1
    



print(list(multifilter(a, mul2, mul3, mul5))) 
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]   

    
