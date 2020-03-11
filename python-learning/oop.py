import pygame
import random
from blob import Blob
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

START_BLUE = 10
START_RED = 3
START_GREEN = 6

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

class BlueBlob(Blob):
  def __init__(self, x_bound, y_bound):
    super().__init__(BLUE, x_bound, y_bound)

  def __add__(self, o_blob):
    logging.info(f'blob add op {str(self)} + {str(o_blob)}')
    if o_blob.color == (255, 0, 0):
      self.size -= o_blob.size
      o_blob.size -= self.size
    elif o_blob.color == (0, 255, 0):
      self.size += o_blob.size
      o_blob.size = 0
    elif o_blob.color == (0, 0, 255):
      pass
    else:
      raise Exception('tried to combine one or multiple blobs of unsupported colors')

class RedBlob(Blob):
  def __init__(self, x_bound, y_bound):
    super().__init__(RED, x_bound, y_bound)

class GreenBlob(Blob):
  def __init__(self, x_bound, y_bound):
    super().__init__(GREEN, x_bound, y_bound)


def handle_collisions(b_list):
  blues, reds, greens = b_list
  for blue_id, blue_blob in blues.copy().items():
    for o_blobs in blues, reds, greens:
      for o_b_id, o_b in o_blobs.copy().items():
        logging.debug(f'checking if blobs are touching {str(blue_blob)} + {str(o_b)}')
        if blue_blob == o_b:
          pass
        else:
          if is_touching(blue_blob, o_b):
            blue_blob + o_b
            if o_b.size <= 0:
              del o_blobs[o_b_id]
            if blue_blob.size <= 0:
              del blues[blue_id]
  return blues, reds, greens

def is_touching(b1, b2):
  return np.linalg.norm(np.array([b1.x, b1.y])-np.array([b2.x, b2.y])) < (b1.size + b2.size)

def draw_env(b_list):
  blues, reds, greens = handle_collisions(b_list)
  game_display.fill(WHITE)
  for blobs in b_list:
    for b_id in blobs:
      blob = blobs[b_id]
      pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
      blob.move()
      blob.constrain()
  pygame.display.update()
  return blues, reds, greens
  
def main():
  blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for i in range(START_BLUE)]))
  red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for i in range(START_RED)]))
  green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(START_GREEN)]))
  while True:
    try:
      for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
          pygame.quit()
          quit()
    except Exception as e:
      logging.critical(str(e))
      pygame.quit()
      quit()
      break

    blue_blobs, red_blobs, green_blobs = draw_env([blue_blobs, red_blobs, green_blobs])
    clock.tick(60)

if __name__ == '__main__':
  main()
