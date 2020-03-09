names = ['person', 'name', 'paul', 'sammy']

for name in names:
  print(f'Hello there {name}') # template string

x = [i for i in range(5)] # same as commented below

# for i in range(5):
#   x.append(i)

# generator - much quicker to generate since it doesn't get stored in memory
# takes longer to iterate over than something in memory however
y = (i for i in range(5))
print(y)
for i in y:
  print(i)

in_list = [2, 4, 5, 7774, 33324, 3565, 335, 5555]

# returns true if divisible by 5
def div_by_fiv(num):
  return not num % 5

xyz = (i for i in in_list if div_by_fiv(i))

for i in xyz:
  print(i)

# enumerate
ex = ['one', 'two', 'blue', 'red']
for i, j in enumerate(ex):
  print(i, j)

di = dict(enumerate(ex))
[print(i,j) for i, j in enumerate(di)]
