import pygame
import pygame.image
import random

llama = pygame.image.load('Llama.png')
cactus = pygame.image.load('cactus.png')
pygame.init()

font = pygame.font.SysFont("arial", 18)
screen = pygame.display.set_mode((540, 180))
pygame.display.set_caption("Llama run")

def generate_cacti():
    cactus_x = 540
    return cactus_x, -5


def main():
    llama_x = 80
    llama_y = 130
    jump_y = 0
    score = 0
    cacti = generate_cacti()

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

        for cactus_data in cacti[:]:
            cactus_x, cactus_speed = cactus_data
            cactus_hitbox = pygame.Rect(cactus_x, 130, 22, 22)
            llama_hitbox = pygame.Rect(llama_x, llama_y, 22, 22)
            collide = pygame.Rect.colliderect(cactus_hitbox, llama_hitbox)
            if collide:
                quit()

            cactus_x += cactus_speed
            if cactus_x < -cactus.get_width():
                cacti.remove(cactus_data)

        white = (255, 255, 255)
        screen.fill(white)

        score += round(clock.tick(60)/25)
        score_txt = font.render(f"Score {int(score)}", True, (0, 0, 0))
        screen.blit(score_txt, (10, 10))
        if score % 200 == 0 and len(cacti) < 3:  # Max 3 cacti
            cacti.append(generate_cacti())

        screen.blit(llama, (llama_x, llama_y))
        for cactus_x, _ in cacti:
            screen.blit(cactus, (cactus_x, 130))

        pygame.display.update()
        clock.tick(60)

# Main Routine
main()
