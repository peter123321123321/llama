import pygame
import pygame.image

llama = pygame.image.load('Llama.png')
pygame.init()

screen = pygame.display.set_mode((540, 180))
pygame.display.set_caption("Llama run")


def main():
    llama_x = 80
    llama_y = 130
    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        white = (255, 255, 255)
        screen.fill(white)
        screen.blit(llama, (llama_x, llama_y))
        pygame.display.update()
        clock.tick(30)


# Main Routine
main()
