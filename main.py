# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    from player import Player
    from asteroid import Asteroid
    from asteroidfield import AsteroidField
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    AsteroidField()

        
    number = 1
    clock = pygame.time.Clock()
    dt = 0

    while number != 0:
        number += 1
        frame_rate = clock.tick(60)
        dt = (frame_rate / 1000)
        updatables.update(dt)
        #player.update(dt)
                
        #exits game when clicking the "X" in screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black", rect=None, special_flags=0)
        #player.draw(screen)
        for thing in drawables:
            thing.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
