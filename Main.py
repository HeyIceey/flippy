# Himanish | 21 May 2023 | Final Version
# All Assets Found From Various Sites
# -----------------------------------------------------------------------------------------------------------------
# FLIPPY!
import pygame
import sys, random
print("\033c")
# Pygame Initialize
pygame.init()

# FPS
FPS = 60

# SCREEN DIMENSIONS
WIDTH, HEIGHT = 1280, 800

# BACKGROUND IMAGE + REIZE
BG = pygame.transform.scale(pygame.image.load("000 BG.png"), (WIDTH, HEIGHT))
W = pygame.display.set_mode((WIDTH, HEIGHT))

# TITLE [NAME]
pygame.display.set_caption("Flippy!")
# TOP ICON [BIRDIE]
ICON = pygame.image.load("!!!! Bird.png")
pygame.display.set_icon(ICON)

# COLORS [MAY/MAY NOT BE USED ATER]
WHITE_BG = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# MENU'S BACKGROUND IMAGE
MenuBG = pygame.transform.scale(pygame.image.load("010 Menu.png"), (WIDTH, HEIGHT))
# ----------------------------------------------------------------------------------------------------------------

# Load Pipe Images [Scaled/Transformed Later]
PipeDown1 = pygame.image.load("06 Pipe.png")
PipeUp1 = pygame.image.load("06 Pipe Down.png")

# Background position
bg_x = 0
# Bird Image & Dimensions
bird_height = 86
bird_width = 89 
bird_img = pygame.transform.scale(pygame.image.load("! Bird.png"), (bird_width, bird_height))

# Bird Dimensions
bird_x = WIDTH // 2 - bird_img.get_width() // 2
bird_y = HEIGHT // 2 - bird_img.get_height() // 2

bird_speed = 4.2 # Moving Speed [Optimzed]
jump_speed = -10.6  # Jump Speed [Somewhat Obtimized]

is_jump = False
jump_count = 22

# Pipe Dimensions
pipe_width = 250
pipe_gap = 26
pipe_x = WIDTH
pipe_speed = 6.6 # How fast pipe pass  through
pipe_height = random.randint(200, HEIGHT - pipe_gap - 200)
pipe_y = pipe_height + pipe_gap

# Pipe Images
PipeUp = pygame.transform.scale(pygame.image.load("06 Pipe Down.png"), (pipe_width, HEIGHT))
PipeDown = pygame.transform.scale(pygame.image.load("06 Pipe.png"), (pipe_width, HEIGHT))

def check_collision():
    bird_rect = bird_img.get_rect(x=bird_x, y=bird_y)
    pipe_up_rect = PipeUp1.get_rect(x=pipe_x, y=0)
    pipe_down_rect = PipeDown1.get_rect(x=pipe_x, y=pipe_y)

    if bird_rect.colliderect(pipe_up_rect) or bird_rect.colliderect(pipe_down_rect):
        return True

    if bird_x + bird_width > pipe_x and bird_x < pipe_x + pipe_width:
        if bird_y < pipe_height or bird_y + bird_height > pipe_y:
            return True

    return False


# [Initial Menu]
def menu():
    while True:
        W.blit(MenuBG, (0,0)) # BG + SIZE

        # Display menu text
        font = pygame.font.SysFont('Century Gothic', 55) # FONT & SIZE
        text = font.render("Press Spacebar To Play! Don't Touch The Pipes!", True, WHITE_BG) # TEXT
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        W.blit(text, text_rect)

        pygame.display.update() # UPDATE DISPLAY 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return


# Update Pipes, Randomizes Size
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
    W.blit(PipeUp, (pipe_x, pipe_height - HEIGHT))
    W.blit(PipeDown, (pipe_x, pipe_y))
    
    # Check collision
    if check_collision():
        # Game over logic
        print("PASS!")
        print("\n")
        

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
    
# End
pygame.quit()
print("Thanks for playing!\n")
print("Have a great day!\n")
quit()
# Bye! :D
# Finished 6 June 2023