class ExtendedStack(list):
    def __init__(self, lst):
        self.lst = lst
    def sum(self):
        
        self.a = self.lst.pop()
        self.b = self.lst.pop()
        self.c = self.a + self.b
        self.lst.append(self.c)
        self.a = 0
        self.b = 0
        
    def sub(self):
        
        self.a = self.lst.pop()
        self.b = self.lst.pop()
        self.c = self.a - self.b
        self.lst.append(self.c)
        self.a = 0
        self.b = 0

    def mul(self):
        
        self.a = self.lst.pop()
        self.b = self.lst.pop()
        self.c = self.a * self.b
        self.lst.append(self.c)
        self.a = 0
        self.b = 0

    def div(self):
        
        self.a = self.lst.pop()
        self.b = self.lst.pop()
        self.c = self.a // self.b
        self.lst.append(self.c)
        self.a = 0
        self.b = 0
        print(self.lst)

        
def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    print (ex_stack)
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0
    
ts = test()