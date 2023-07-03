import pygame

#setup display
pygame.init()
WIDTH, HEIGHT = 800, 500

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!")

#load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

print(images)
#setups gameloop here
FPS = 60
clock = pygame.time.Clock()

run = True

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()


