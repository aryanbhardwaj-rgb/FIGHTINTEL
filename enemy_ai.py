import pygame
import random
from ai_model import AIMovePredictor

class EnemyAI:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 100)
        self.color = (255, 0, 0)
        self.health = 100
        self.is_punching = False
        self.is_kicking = False
        self.vel_y = 0
        self.gravity = 1
        self.on_ground = True

        self.ai = AIMovePredictor()
        self.attack_cooldown = 0
        self.ml_enabled = True  # Toggle ML learning

        self.learned_patterns = []
        self.replay_pattern = []
        self.replay_index = 0

    def think(self, player_moves, screen_width, player_x):
        self.is_punching = False
        self.is_kicking = False

        # Move toward player unless too close
        min_gap = 40
        if player_x < self.rect.x - min_gap:
            self.rect.x -= 3
        elif player_x > self.rect.x + min_gap:
            self.rect.x += 3

        # Prevent out of bounds
        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))

        # Learn from player
        if self.ml_enabled and len(player_moves) >= 4:
            last_pattern = player_moves[-4:]
            if last_pattern not in self.learned_patterns:
                self.learned_patterns.append(last_pattern)
                print("\U0001F9E0 AI learned a new combo:", last_pattern)

        # Execute learned combo
        if self.replay_pattern:
            move = self.replay_pattern[self.replay_index]

            if move == "PUNCH":
                self.is_punching = True
            elif move == "KICK":
                self.is_kicking = True
            elif move == "JUMP" and self.on_ground:
                self.vel_y = -15
                self.on_ground = False

            self.replay_index += 1
            if self.replay_index >= len(self.replay_pattern):
                self.replay_index = 0
                self.replay_pattern = []
                self.attack_cooldown = 40
            return

        # Decide to use a learned combo
        if self.attack_cooldown <= 0 and self.learned_patterns:
            if random.random() < 0.3:
                self.replay_pattern = random.choice(self.learned_patterns)
                self.replay_index = 0
                print("\U0001F916 AI using learned combo:", self.replay_pattern)
                return

        # Basic random attack
        if self.attack_cooldown <= 0:
            if random.random() < 0.04:
                self.is_punching = random.choice([True, False])
                self.is_kicking = not self.is_punching
                self.attack_cooldown = 30

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        self.apply_gravity()

    def apply_gravity(self):
        self.rect.y += self.vel_y
        self.vel_y += self.gravity
        if self.rect.y >= 300:
            self.rect.y = 300
            self.vel_y = 0
            self.on_ground = True

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

        if self.is_punching:
            pygame.draw.rect(win, (150, 0, 0), (self.rect.left - 20, self.rect.y + 20, 20, 10))
        if self.is_kicking:
            pygame.draw.rect(win, (150, 100, 0), (self.rect.left - 20, self.rect.y + 80, 20, 10))

        pygame.draw.rect(win, (255, 0, 0), (self.rect.x, self.rect.y - 10, 50, 5))
        pygame.draw.rect(win, (0, 255, 0), (self.rect.x, self.rect.y - 10, 50 * (self.health / 100), 5))