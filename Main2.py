import pygame
import pygame.image

llama = pygame.image.load('Llama.png')
cactus = pygame.image.load('cactus.png')
pygame.init()

font = pygame.font.SysFont("arial", 18)
screen = pygame.display.set_mode((540, 180))
pygame.display.set_caption("Llama run")


def main():
    llama_x = 80
    llama_y = 130
    jump_y = 0
    cactus_x = 540
    cactus_speed = -5
    score = 0

    run = True
    clock = pygame.time.Clock()
    jumping = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not jumping:
                    jumping = True
                    jump_y = -10

        if jumping:
            jump_y += 1
            llama_y += jump_y
            if jump_y > 50:
                jump_y = 0
            if llama_y >= 130:
                llama_y = 130
                jumping = False

        cactus_hitbox = pygame.Rect(cactus_x, 130, 22, 22)
        llama_hitbox = pygame.Rect(llama_x, llama_y, 22, 22)
        collide = pygame.Rect.colliderect(cactus_hitbox, llama_hitbox)
        if collide:
            quit()

        cactus_x += cactus_speed
        if cactus_x < -cactus.get_width():
            cactus_x = 540

        white = (255, 255, 255)
        screen.fill(white)

        score += round(clock.tick(60)/25)
        score_txt = font.render(f"Score {int(score)}", True, (0, 0, 0))
        screen.blit(score_txt, (10, 10))
        if score % 100 == 0 and cactus_speed <= 13:
            cactus_speed -= 1
        screen.blit(llama, (llama_x, llama_y))
        screen.blit(cactus, (cactus_x, 130))

        pygame.display.update()
        clock.tick(60)

# Main Routine
main()
