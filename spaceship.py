import pygame
from constant import *


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


        self.x=screen_width / 2
        self.y= screen_height / 2
        self.player_pos = pygame.Vector2(self.x,self.y)
        self.rotation=0
        #self.postion=pygame.Vector2(self.x,self.y)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * player_radius / 1.5
        a = self.player_pos + forward * player_radius
        b = self.player_pos - forward * player_radius - right
        c = self.player_pos - forward * player_radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"red",self.triangle(),width=2)
        # pygame.draw.circle(screen,"red",self.player_pos,player_radius)
    
    def rotate(self,dt):
        self.rotation+=player_turn_speed*dt

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.player_pos += forward * player_speed * dt

    def update(self,dt):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            # self.player_pos.y-=300*dt
            self.move(dt)

        # if keys[pygame.K_s]:
        #     # self.player_pos.y+=300*dt
        #     self.move(-dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)
            # self.player_pos.x-=300*dt
            
        if keys[pygame.K_d]:
            self.rotate(dt)
            # self.player_pos.x+=300*dt