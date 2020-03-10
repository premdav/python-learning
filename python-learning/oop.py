import pygame
import random
from blob import Blob

START_BLUE = 10
START_RED = 3

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

class BlueBlob(Blob):
  def __init__(self, color, x_bound, y_bound):
    super().__init__(color, x_bound, y_bound)
    self.color = BLUE

  def move_fast(self):
    self.x += random.randrange(-6, 7)
    self.y += random.randrange(-6, 7)


def draw_env(b_list):
  game_display.fill(WHITE)
  for blobs in b_list:
    for b_id in blobs:
      blob = blobs[b_id]
      pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
      blob.move_fast()
      blob.constrain()
  pygame.display.update()
  
def main():
  blue_blobs = dict(enumerate([BlueBlob(BLUE, WIDTH, HEIGHT) for i in range(START_BLUE)]))
  red_blobs = dict(enumerate([BlueBlob(RED, WIDTH, HEIGHT) for i in range(START_RED)]))
  while True:
    for evt in pygame.event.get():
      if evt.type == pygame.QUIT:
        pygame.quit()
        quit()

    draw_env([blue_blobs, red_blobs])
    clock.tick(60)

if __name__ == '__main__':
  main()
