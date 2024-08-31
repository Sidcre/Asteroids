import pygame
from constant import *

def main():
    screen=pygame.display.set_mode((screen_width,screen_height))
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()


if __name__=="__main__":
    main()
