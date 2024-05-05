import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1000, 750))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("The Snak")

# colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)
yellow = (255, 255, 0)

score_font = pygame.font.SysFont("snake chan.ttf  ", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

clock = pygame.time.Clock()


def load_high_score():
    try:
        hi_score_file = open("HI_score.txt", 'r')
    except IOError:
        hi_score_file = open("HI_score.txt", 'w')
        hi_score_file.write("0")
    hi_score_file = open("HI_score.txt", 'r')
    value = hi_score_file.read()
    hi_score_file.close()
    return value


def update_high_score(score, high_score):
    if int(score) > int(high_score):
        return score
    else:
        return high_score


def save_high_score(high_score):
    high_score_file = open("HI_score.txt", 'w')
    high_score_file.write(str(high_score))
    high_score_file.close()


def player_score(score, score_colour, hi_score):
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (800, 20))

    display_high_score = score_font.render(f"High score: {hi_score}", True,
                                           score_colour)
    screen.blit(display_high_score, (10, 10))


def message(msg, txt_colour):
    txt = msg_font.render(msg, True, txt_colour)

    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)


def draw_snake(snake_list):
    print(f"Snake list: {snake_list}")
    for i in snake_list:
        pygame.draw.rect(screen, red, [i[0], i[1], 20, 20])


def game_loop():
    high_score = int(load_high_score())
    quit_game = False
    game_over = False

    snake_x = 480
    snake_y = 340

    snake_x_change = 0
    snake_y_change = 0
    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 720 - 20) / 20) * 20

    while not quit_game:
        while game_over:
            save_high_score(high_score)
            screen.fill(white)
            message("You DIED! Press 'Q' or 'A' to play again.",
                    black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = "Exit: X to quit, Space to resume, R to Reset"
                message(instructions, black)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                end = True, game_loop()

                            if event.key == pygame.K_SPACE:
                                end = True

                            if event.key == pygame.K_x:
                                screen.fill(green)
                                confirm_quit = "Are you sure you want to quit [Y/N]"
                                message(confirm_quit, black)
                                pygame.display.update()
                                if event.key == pygame.K_y:
                                    quit_game = True
                                    end = True
                                if event.key == pygame.K_n:
                                    end = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -20
                    snake_y_change = 0
                if event.key == pygame.K_RIGHT:
                    snake_x_change = 20
                    snake_y_change = 0
                if event.key == pygame.K_UP:
                    snake_x_change = 0
                    snake_y_change = -20
                if event.key == pygame.K_DOWN:
                    snake_x_change = 0
                    snake_y_change = 20

        if snake_x >= 1000 or snake_x <= 0 or snake_y >= 720 or snake_y <= 0:
            game_over = True

        print(snake_x, snake_y)
        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_snake(snake_list)

        score = snake_length - 1
        player_score(score, black, high_score)

        high_score = update_high_score(score, high_score)

        if score > 5:
            speed = score
        else:
            speed = 5

        food = pygame.Rect(food_x, food_y, 20, 20)
        apple = pygame.image.load('apple_3.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        screen.blit(resized_apple, food)
        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 720 - 20) / 20) * 20

            high_score = load_high_score()
            print(f"high_score test: {high_score}")
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()


# Main Routine
game_loop()
