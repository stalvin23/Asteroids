import pygame
from constants import *

class ScoreDisplay:
    def __init__(self, initial_score=0):
        self.score = initial_score

    def add_points(self, points):
        self.score += points

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))
