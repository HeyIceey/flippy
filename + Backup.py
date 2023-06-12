# Himanish | 21 May 2023 | Final Version
# FLIPPY!
import pygame
import sys, random

# Pygame Initialize
pygame.init()

# Variables
FPS = 60

# DIMENSIONS
WIDTH, HEIGHT = 1280, 720

# BG + WINDOW SIZE
BG = pygame.transform.scale(pygame.image.load("000 BG.png"), (WIDTH, HEIGHT))
W = pygame.display.set_mode((WIDTH, HEIGHT))
# TITLE
pygame.display.set_caption("Flippy: Night City")

ICON = pygame.image.load("!! Bird.png")
pygame.display.set_icon(ICON)

# COLORS
WHITE_BG = (255, 255, 255)
BLACK = (0, 0, 0)

# Menu's Background Variable
MenuBG = pygame.transform.scale(pygame.image.load("08 Menu.png"), (WIDTH, HEIGHT))
# ATTEMPT  -----------------------------------------------------------------------------------------------------------------


# Load Pipe Images
PipeDown = pygame.image.load("06 Pipe.png")
PipeUp = pygame.image.load("06 Pipe Down.png")

# Background position
bg_x = 0

# Bird image
bird_height = 86
bird_width = 90  # Adjust the width as desired
bird_img = pygame.transform.scale(pygame.image.load("00 Bird.png"), (bird_width, bird_height))

bird_x = WIDTH // 2 - bird_img.get_width() // 2
bird_y = HEIGHT // 2 - bird_img.get_height() // 2
bird_speed = 3.89 # Adjust the speed as desired
jump_speed = -7.25  # Adjust the jump speed as desired

is_jump = False
jump_count = 10


# Pipes
pipe_width = 88 
pipe_gap = 80
pipe_x = WIDTH
pipe_speed = 5
pipe_height = random.randint(200, HEIGHT - pipe_gap - 200)
pipe_y = pipe_height + pipe_gap


# [Initial Menu]
def menu():
    while True:
        W.blit(MenuBG, (0,0))

        # Display menu text
        font = pygame.font.SysFont('comicsansms', 50)
        text = font.render("Press Spacebar To Play! Don't Touch The Pipes!", True, WHITE_BG)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        W.blit(text, text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return



def update_pipes():
    global pipe_x, pipe_height, pipe_y

    pipe_x -= pipe_speed

    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_height = random.randint(200, HEIGHT - pipe_gap - 200)
        pipe_y = pipe_height + pipe_gap

def draw_window():
    global bg_x, bird_y, is_jump, jump_count

    # Scroll the background image horizontally
    bg_x -= bird_speed
    if bg_x < -WIDTH:
        bg_x = 0

    W.fill(WHITE_BG)
    W.blit(BG, (bg_x, 0))
    W.blit(BG, (bg_x + WIDTH, 0))  # Draw a second copy to create a seamless loop

    # Handle bird jumping
    if is_jump:
        if jump_count >= -8:
            bird_y += jump_speed
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8

    # Update bird position
    bird_y += bird_speed

    # Draw the bird image
    W.blit(bird_img, (bird_x, bird_y))

    # Update and draw the pipes
    update_pipes()
    pygame.draw.rect(W, WHITE_BG, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(W, WHITE_BG, (pipe_x, pipe_y + pipe_gap, pipe_width, HEIGHT - (pipe_y + pipe_gap)))

    pygame.display.update()

clock = pygame.time.Clock()
menu()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jump:
                is_jump = True
                jump_count = 10

    draw_window()
    clock.tick(FPS)

pygame.quit()
