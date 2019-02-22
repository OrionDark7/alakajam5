import pygame, pytmx, time #Global Dependencies
import ui, entities #Project Libraries

pygame.init()
window = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Alakajam! 5")
running = True
mouse = [0, 0]
screen = "intro"

play = ui.button("Play Game", [10, 45])
quitbutton = ui.button("Quit Game", [10, 65])

def intro():
    window.fill([0, 0, 0])
    font = pygame.font.Font(None, 24)
    render = font.render("An Alakajam! #5 Entry", 1, [255, 255, 255])
    rect = 400 - (render.get_rect().width / 2)
    window.blit(render, [rect, 300])
    pygame.display.flip()
    time.sleep(2)

def menu():
    window.fill([255, 255, 255])
    font = pygame.font.Font(None, 48)
    render = font.render("Game Title", 1, [0, 0, 0])
    window.blit(render, [5, 5])
    play.draw(window)
    quitbutton.draw(window)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = [event.pos[0], event.pos[1]]
            if screen == "menu":
                if play.click(mouse):
                    screen = "game"
                    play.reset()
                if quitbutton.click(mouse):
                    running = False
                    quitbutton.reset()
    if screen == "intro":
        intro()
        screen = "menu"
    elif screen == "menu":
        menu()
    elif screen == "game":
        window.fill([0, 0, 0])
    pygame.display.flip()
pygame.quit()