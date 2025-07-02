import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 100)
        self.color = (0, 0, 255)
        self.speed = 5
        self.jump_speed = -15
        self.gravity = 1
        self.vel_y = 0
        self.on_ground = True

        self.health = 100
        self.last_moves = []
        self.is_punching = False
        self.is_kicking = False

    def move(self, keys, screen_width):
        self.is_punching = False
        self.is_kicking = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.log_move("LEFT")
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.log_move("RIGHT")

        # Prevent moving out of screen
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width

        if keys[pygame.K_UP] and self.on_ground:
            self.vel_y = self.jump_speed
            self.on_ground = False
            self.log_move("JUMP")

        if keys[pygame.K_p]:
            self.is_punching = True
            self.log_move("PUNCH")

        if keys[pygame.K_k]:
            self.is_kicking = True
            self.log_move("KICK")

        self.apply_gravity()

    def apply_gravity(self):
        self.rect.y += self.vel_y
        self.vel_y += self.gravity

        if self.rect.y >= 300:  # Ground level
            self.rect.y = 300
            self.vel_y = 0
            self.on_ground = True

    def log_move(self, move):
        self.last_moves.append(move)
        if len(self.last_moves) > 5:
            self.last_moves.pop(0)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

        # Draw arms if attacking
        if self.is_punching:
            pygame.draw.rect(win, (0, 0, 150), (self.rect.right, self.rect.y + 20, 20, 10))
        if self.is_kicking:
            pygame.draw.rect(win, (0, 150, 0), (self.rect.right, self.rect.y + 80, 20, 10))

        # Health bar
        pygame.draw.rect(win, (255, 0, 0), (self.rect.x, self.rect.y - 10, 50, 5))
        pygame.draw.rect(win, (0, 255, 0), (self.rect.x, self.rect.y - 10, 50 * (self.health / 100), 5))