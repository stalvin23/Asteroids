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
    from game import GameState
    from game import Game

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

    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    game = Game(screen)
    running = True
    while running:
        dt = clock.tick(60) / 1000
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game.state == GameState.START:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        game.menu_index = (game.menu_index - 1) % 2
                    elif event.key == pygame.K_s:
                        game.menu_index = (game.menu_index + 1) % 2
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        if game.menu_index == 0:
                            game.start_new_game(updatables, drawables, asteroids, shots, score, score_manager)
                            game.state = GameState.PLAYING  # Start the game
                        elif game.menu_index == 1:
                            running = False
            elif game.state == GameState.GAME_OVER:
                game.draw_game_over_screen(score_manager)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or pygame.K_SPACE:
                        game.state = GameState.START
        
        #print(f"Game state: {game.state}")  
        if game.state == GameState.START:
            game.draw_title_screen()   
        elif game.state == GameState.PLAYING:
            # Update all sprites
            for sprite in updatables:
                sprite.update(dt)
            for asteroid_instance in asteroids:
                if asteroid_instance.checkcollision(game.player) == True:
                    print("Game Over!")
                    print(score_manager.score)
                    game.state = GameState.GAME_OVER
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
            #.fill("black", rect=None, special_flags=0)
        elif game.state == GameState.GAME_OVER:
            game.draw_game_over_screen(score_manager)
            
        pygame.display.flip()
    
if __name__ == "__main__":
    main()
