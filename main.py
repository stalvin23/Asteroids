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
    from circleshape import CircleShape
    from shot import Shot
    from score import ScoreDisplay

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score = pygame.sprite.Group()
    score_manager = ScoreDisplay(initial_score=0)

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    score_manager.containers = (score, drawables)

    Player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    AsteroidField()

    number = 1
    clock = pygame.time.Clock()
    dt = 0

    while number != 0:
        number += 1
        dt = clock.tick(60) / 1000
                
        #exits game when clicking the "X" in screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

            # Update all sprites
        for sprite in updatables:
            sprite.update(dt)
        
        for asteroid_instance in asteroids:
            if asteroid_instance.checkcollision(Player) == True:
                print("Game Over!")
                print(score_manager.score)
                exit()

        for asteroid_instance in asteroids:
            for shot in shots:
                if asteroid_instance.checkcollision(shot) == True:
                    asteroid_instance.split()
                    shot.kill()
                    score_manager.add_points(10)
        
        # Draw all sprites
        for sprite in drawables:
            sprite.draw(screen)
        
        score_manager.draw(screen)
        pygame.display.flip() 
        screen.fill("black", rect=None, special_flags=0)

        

if __name__ == "__main__":
    main()
