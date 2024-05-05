import pygame

pygame.init()

screen = pygame.display.set_mode((540, 180))
pygame.display.set_caption("Llama run")


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        white = (255, 255, 255)
        screen.fill(white)
        clock.tick(30)


# Main Routine
main()
