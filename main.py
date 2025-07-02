import pygame
from player_module import Player
from enemy_ai import EnemyAI

pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Fighting Game")

FPS = 60
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)

# Create Player and AI Opponent
player = Player(100, 300)
enemy = EnemyAI(600, 300)

def draw_window():
    WIN.fill(WHITE)
    player.draw(WIN)
    enemy.draw(WIN)
    pygame.display.update()

def show_game_over_screen(winner):
    font = pygame.font.SysFont("arial", 48)
    small_font = pygame.font.SysFont("arial", 24)
    run = True

    while run:
        WIN.fill((0, 0, 0))
        text = font.render(f"{winner} Wins!", True, (255, 255, 255))
        replay_text = small_font.render("Press R to Replay or Q to Quit", True, (255, 255, 255))

        WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))
        WIN.blit(replay_text, (WIDTH // 2 - replay_text.get_width() // 2, HEIGHT // 2 + 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                    run = False
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()
                    run = False
                    return

def main():
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH)
        enemy.think(player.last_moves, WIDTH, player.rect.x)

        # Player hits AI
        if player.rect.colliderect(enemy.rect):
            if player.is_punching:
                enemy.health -= 4
                print("Enemy hit by punch! Health:", enemy.health)
            if player.is_kicking:
                enemy.health -= 6
                print("Enemy hit by kick! Health:", enemy.health)

        # AI hits Player
        if enemy.rect.colliderect(player.rect):
            if enemy.is_punching:
                damage = 15 if enemy.replay_pattern else 10
                player.health -= damage
                print(f"\U0001F4A5 Player hit by punch! Damage: {damage}, Health: {player.health}")
            if enemy.is_kicking:
                damage = 20 if enemy.replay_pattern else 12
                player.health -= damage
                print(f"\U0001F4A5 Player hit by kick! Damage: {damage}, Health: {player.health}")

        # End the game if someone loses
        if player.health <= 0 or enemy.health <= 0:
            winner = "Player" if player.health > 0 else "AI"
            show_game_over_screen(winner)
            return

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()