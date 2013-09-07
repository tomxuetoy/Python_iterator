# -*- coding: utf-8 -*-  
      
'''''Fibonacci iterator'''  
      
class Fib:  
    '''''一个可以生成Fibonacci 数列的迭代器'''  
      
    def __init__(self, max):  
        self.max = max  
      
    def __iter__(self):  
        self.a = 0  
        self.b = 1  
        return self  
      
    def next(self):  
        fib = self.a  
        if fib > self.max:  
            raise StopIteration  
        self.a, self.b = self.b, self.a + self.b  
        return fib  
