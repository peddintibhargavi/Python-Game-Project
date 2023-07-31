import pygame
import time

# initialize pygame
pygame.init()

# set window size
window_size = (800, 800)

# create the window
window = pygame.display.set_mode(window_size)

# set the window title
pygame.display.set_caption("Square")

# set the background color
background_color = (0, 0, 0)

# set the square size
square_size = 100

autoclicker_size = 100

# set the square color
square_color = (255, 0, 0)

autoclicker_color = square_color
autoclicker = False
# set the square position
square_x = window_size[0] // 2 - square_size // 2
square_y = window_size[1] // 2 - square_size // 2

autoclicker_x = window_size[0] - window_size[0] + 1
autoclicker_y = window_size[0] - window_size[0] + 1


# initialize the count to 0
count = 0

# keep track of whether the mouse was clicked
mouse_clicked = False

# run the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if square_x <= mouse_x <= square_x + square_size and square_y <= mouse_y <= square_y + square_size:
               square_size -= 10
               square_x += 5
               square_y += 5


            if autoclicker_x <= mouse_x <= autoclicker_y + autoclicker_size and autoclicker_y <= mouse_y <= autoclicker_y + autoclicker_size:
                if autoclicker == False:
                    autoclicker_color = (0, 255, 0)
                    autoclicker = True
                    
                else:
                    autoclicker_color = (255, 0, 0)
                    autoclicker = False
                    
                      
                         
        elif event.type == pygame.MOUSEBUTTONUP:
            square_size = 100
            if count >= 25 and count < 50:
                square_color = (0, 255, 0)
            elif count >= 50 and count < 75:
                square_color = (0, 0, 255) 
            elif count >= 75 and count < 100:
                square_color = (255, 255, 255)
            elif count >= 100:
                square_color = (0, 0, 0)
                background_color = (255, 255, 255)
            square_x = (window_size[0] - square_size) / 2
            square_y = (window_size[1] - square_size) / 2

    # clear the screen
    window.fill(background_color)

    # draw the square
    pygame.draw.rect(window, square_color, (square_x, square_y, square_size, square_size))
    pygame.draw.rect(window, autoclicker_color, (autoclicker_x, autoclicker_y, autoclicker_size, autoclicker_size))

    # increment the count if the mouse was clicked on the square
    if mouse_clicked:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if square_x <= mouse_x <= square_x + square_size and square_y <= mouse_y <= square_y + square_size:
            count += 1
        mouse_clicked = False

    # display the count
    font = pygame.font.Font(None, 36)
    text = font.render(str(count), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (square_x + square_size // 2, square_y + square_size // 2 - 100)
    window.blit(text, text_rect)

    # autoclicker text
    font = pygame.font.Font(None, 20)
    text = font.render(str('Autoclicker'), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (autoclicker_x + autoclicker_size // 2, autoclicker_y + autoclicker_size // 2)
    window.blit(text, text_rect)

    # count text
    font = pygame.font.Font(None, 20)
    text = font.render(str('0 - red     25 - green      50 - blue       75 - white      100 - Secret'), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (autoclicker_x + autoclicker_size // 2 + 300, autoclicker_y + autoclicker_size // 2)
    window.blit(text, text_rect)


    while autoclicker == True:
        count += 1
        time.sleep(0.1)
        break

    # update the screen
    pygame.display.update()

# quit pygame
pygame.quit()