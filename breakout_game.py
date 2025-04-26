import pygame

# Khởi tạo Pygame
pygame.init()

# Cài đặt cửa sổ game
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

lives = 3 

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRICK_COLOR = (255, 100, 100)
PADDLE_COLOR = (0, 200, 255)
BALL_COLOR = (255, 255, 0)

# Cấu hình paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 7

# Cấu hình bóng
BALL_RADIUS = 8
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_dx = 4
ball_dy = -4

# Cấu hình gạch
BRICK_ROWS = 5
BRICK_COLS = 8
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 25

bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 40, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
        bricks.append(brick)

# Phông chữ
font = pygame.font.SysFont("Arial", 24)
score = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Điều khiển paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Di chuyển bóng
    ball.x += ball_dx
    ball.y += ball_dy

    # Va chạm với tường
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1

    # Va chạm với paddle
    if ball.colliderect(paddle):
        ball_dy *= -1

    # Va chạm với gạch
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1
            score += 10
            break

    # Game over nếu bóng rơi xuống
    if ball.bottom > HEIGHT:
        lives -= 1
        if lives > 0:
            # Reset bóng và paddle
            ball.x, ball.y = WIDTH // 2, HEIGHT // 2
            ball_dx, ball_dy = 4, -4
            paddle.x = WIDTH // 2 - PADDLE_WIDTH // 2
        else:
            text = font.render("Game Over! Press R to Restart", True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            lives = 3
                            # Reset game
                            ball.x, ball.y = WIDTH // 2, HEIGHT // 2
                            ball_dx, ball_dy = 4, -4
                            paddle.x = WIDTH // 2 - PADDLE_WIDTH // 2
                            score = 0
                            bricks = []
                            for row in range(BRICK_ROWS):
                                for col in range(BRICK_COLS):
                                    brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 40, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
                                    bricks.append(brick)
                            waiting = False

    # Vẽ paddle và bóng
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)
    pygame.draw.ellipse(screen, BALL_COLOR, ball)

    # Vẽ gạch
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    # Hiển thị điểm
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (560,475))
    screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))

    pygame.display.flip()

pygame.quit()
