# site_title = 'my blog'

# def blog_posts(title, *args, **kwargs):
#   print(title)
#   for a in args:
#     print(a)
#   for b_t, post in kwargs.items():
#     print(b_t, post)

# blog_posts(site_title, 'bop', 'boop', 'robot boi', blog_1='This is a blog about something',
# blog_2='Traveling during coronavirus',
# blog_3='Best cheap flights'
# )

import matplotlib.pyplot as plt

def graph_op(x, y):
  print(f'function that graphs {x} and {y}')
  plt.plot(x, y)
  plt.show()

x1 = [1, 2, 3]
y1 = [2, 3, 1]

graph_me = [x1, y1]

graph_op(*graph_me)
