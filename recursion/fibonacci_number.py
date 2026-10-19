
class solution:
    def func(self, num):
        if num ==1 or num==0:
            return num
        return self.func(num-1) + self.func(num-2)

    def fib (self, n:int):
     anwser = self.func(n)
     return anwser

s = solution()
print(s.fib(34))

