import pygame
import random

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

class Blob:
  def __init__(self, color):
    self.x = random.randrange(0, WIDTH)
    self.y = random.randrange(0, HEIGHT)
    self.size = random.randrange(4, 8)
    self.color = color

  def move(self):
    self.move_x = random.randrange(-1, 2)
    self.move_y = random.randrange(-1, 2)
    self.x += self.move_x
    self.y += self.move_y

    if self.x < 0: self.x = 0
    elif self.x > WIDTH: self.x = WIDTH

    if self.y < 0: self.y = 0
    elif self.y > HEIGHT: self.y = HEIGHT


def draw_env(b_list):
  game_display.fill(WHITE)
  for blobs in b_list:
    for b_id in blobs:
      blob = blobs[b_id]
      pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
      blob.move()
  pygame.display.update()
  
def main():
  blue_blobs = dict(enumerate([Blob(BLUE) for i in range(START_BLUE)]))
  red_blobs = dict(enumerate([Blob(RED) for i in range(START_RED)]))
  while True:
    for evt in pygame.event.get():
      if evt.type == pygame.QUIT:
        pygame.quit()
        quit()

    draw_env([blue_blobs, red_blobs])
    clock.tick(60)
    # print(red_blob.x, red_blob.y)

if __name__ == '__main__':
  main()
