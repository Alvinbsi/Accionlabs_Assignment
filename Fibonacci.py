class Fibonacci:
  def fib_self(self):
    self.a, self.b = 0, 1
  def fib_even(self, count):
    total, num = 0, 0
    while count > 0:
      self.a, self.b = self.b, self.a + self.b
      if self.a %2 == 0:
        total += self.a
        count -= 1
    return total
  
fib = Fibonacci()
print(fib.fib_even(3))
