# x = (i for i in range(5))

# next(x) # moves selector one position at a time manually
# x.__next__() # valid method of x
# print(dir(x)) # shows methods on the x object
# for i in x:
#   print(i)

# class range_ex:
#   def __init__(self, end, step=1):
#     self.current = 0
#     self.end = end
#     self.step = step
  
#   def __iter__(self):
#     return self

#   def __next__(self):
#     if self.current >= self.end:
#       raise StopIteration()
#     else:
#       return_val = self.current
#       self.current += self.step
#       return return_val

# for i in range_ex(4):
#   print(i)

# x = range_ex(3)
# print(dir(x))


def range_gen(end):
  current = 0
  while current < end:
    yield current
    current += 1

for i in range_gen(5):
  print(i)

x = range_gen(3)
print(dir(x))
