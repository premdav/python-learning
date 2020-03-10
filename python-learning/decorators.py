from functools import wraps

def wrapping_style(style):
  def add_wrapping(item):
    @wraps(item)
    def wrapped_item():
      return f'a {style} wrapped box of {str(item())}'
    return wrapped_item
  return add_wrapping

@wrapping_style('horribly')
@wrapping_style('beautifully')
def new_gpu():
  return 'a new RTX 2080ti'

print(new_gpu())