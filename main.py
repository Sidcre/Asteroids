import pygame
from constant import *
from spaceship import *


def main():
    pygame.init()
    screen=pygame.display.set_mode((screen_width,screen_height))

    updateable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()

    Spaceship.containers=(updateable,drawable)

    clock=pygame.time.Clock()
    spaceship=Spaceship()
    dt=0
    running=True
    while(running):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.fill("black")
    
        # spaceship.draw(screen)
    
        for i in drawable:
            i.draw(screen)
    
        for i in updateable:
            i.update(dt)
        # spaceship.update(dt)

        # pygame.draw.circle(screen,"red",player_pos,40)
        # keys=pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     player_pos.y-=300*dt
        # if keys[pygame.K_s]:
        #     player_pos.y+=300*dt
        # if keys[pygame.K_a]:
        #     player_pos.x-=300*dt
        # if keys[pygame.K_d]:
        #     player_pos.x+=300*dt

        pygame.display.flip()
        dt=clock.tick(60)/1000
    pygame.quit()

if __name__=="__main__":
    main()