import pygame
import pygame.sprite

pygame.init()
game_window = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Whack A Mole")
icon = pygame.image.load("../Images/mallet.png")
pygame.display.set_icon(icon)
background = pygame.image.load("../Images/bg.jpg")

clock = pygame.time.Clock()
score = 0


# Background
def set_background():
    game_window.blit(background, (0, 0))


def display_holes():
    hole = pygame.image.load("../Images/hole.png")
    game_window.blit(hole,(250,60))
    game_window.blit(hole,(350,60))
    game_window.blit(hole, (450, 60))

    game_window.blit(hole, (250, 150))
    game_window.blit(hole, (350, 150))
    game_window.blit(hole, (450, 150))

    game_window.blit(hole, (250, 240))
    game_window.blit(hole, (350, 240))
    game_window.blit(hole, (450, 240))



# Mole Image
mole = pygame.image.load("../Images/mole1.png")
moleX = 250
moleY = 30

def hit():
    font = pygame.font.SysFont("comicsans", 30, True)
    score_text = font.render("Score: " + str(score), 1, (0, 0, 0))
    game_window.blit(score_text, (700, 10))

def display_moles(x,y):
    game_window.blit(mole, (x,y))
x = 250
y = 30
y_change = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("You pressed the left mouse button at (%d, %d)" % event.pos)
            y_change = 1.2
    y += y_change
    if y == 104:
        pygame.image.load("../Images/mole.png").convert_alpha()
    ###remove image once hit 60 coords


    set_background()
    hit()
    display_moles(x,y)
    display_holes()
    pygame.display.update()
