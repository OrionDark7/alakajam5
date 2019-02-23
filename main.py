import pygame, pytmx, time, random #Global Dependencies
import ui, entities, objects #Project Libraries

#Juicy Zesty Bitter Sweet - Copyright (c) 2019 Orion Williams

#VARIABLE DECLARATIONS
pygame.init()
window = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Alakajam! 5")
running = True
mouse = [0, 0]
screen = "intro"
player = entities.player([380, 280])
play = ui.button("Play Game", [10, 45])
quitbutton = ui.button("Quit Game", [10, 65])
juicy = ui.button("Juice Powder", [10, 500])
zesty = ui.button("Zest Potion", [10, 520])
bitter = ui.button("Bitter Curse", [10, 540])
sweet = ui.button("Sweet Tooth Spell", [10, 560])
back = ui.button("Back", [5, 5])
food = {"burger":[3, 1, 1, 0], "tacos":[3, 2, 0, 1], "fries":[2, 3, 1, 0], "cupcake":[0, 0, 0, 4], "sushi":[2, 3, 1, 1]}
foodimages = {"burger":pygame.image.load("./images/food/burger.png"),"tacos":pygame.image.load("./images/food/taco.png"),"fries":pygame.image.load("./images/food/fries.png"),"cupcake":pygame.image.load("./images/food/cupcake.png"),
              "sushi": pygame.image.load("./images/food/sushi.png")}
recipe = [0, 0, 0, 0]
seats = [False, False, False, False]
order = None
pos = [0, 0]
bubble = pygame.image.load("./images/speech-bubble.png")
bubble = pygame.transform.scale(bubble, [100, 100])
pygame.time.set_timer(pygame.USEREVENT, 10000)

#OBJECT CREATION
counter = objects.counter([0,0])
counter2 = objects.counter([500, -100])
stove = objects.tools([0, 80], "stove")
board = objects.tools([30, 290], "cutting board")
oven = objects.tools([20, 440], "oven")
customers = pygame.sprite.Group()
chairs = pygame.sprite.Group()
for i in range(4):
    chairs.add(objects.chair([600, (i * 120) + 25]))

def update(action):
    global data, mouse
    data = {"order":None}
    customers.update(str(action), mouse, data)

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
    render = font.render("juicy ZESTY bitter SWEET", 1, [0, 0, 0])
    window.blit(render, [5, 5])
    play.draw(window)
    quitbutton.draw(window)

def drawObjects():
    global counter, counter2, chairs, stove, board, oven, customers
    chairs.draw(window)
    counter.draw(window)
    counter2.draw(window)
    stove.draw(window)
    board.draw(window)
    oven.draw(window)
    customers.draw(window)

def newCustomer():
    global seats, customers
    if random.randint(1, 10) < 8:
        if not seats[0] or not seats[1] or not seats[2] or not seats[3]: #Check if No Open Seats
            allseats = [0, 1, 2, 3]
            seat = random.choice(allseats)
            while seats[seat]: #While seat picked is still taken
                seat = random.choice(allseats)
            allseats.remove(seat)
            seats[seat] = True
            order = random.choice(food.keys())
            positions = [37, 157, 277, 397]
            customer = entities.customer([612, positions[seat]], order)
            customers.add(customer)

def showOrder():
    global order, customerpos
    if not order == None:
        image = pygame.transform.scale(foodimages[order], [50, 50])
        window.blit(bubble, (customerpos[0] + 80, customerpos[1] - 20))
        window.blit(image, (customerpos[0] + 110, customerpos[1]))

def cookScreen():
    global window
    table = pygame.surface.Surface([800, 200])
    table.fill([163, 77, 0])
    window.blit(table, [0, 400])
    juicy.draw(window)
    zesty.draw(window)
    bitter.draw(window)
    sweet.draw(window)
    back.draw(window)

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
            elif screen == "game":
                update("click")
                if not data["order"] == None:
                    order = data["order"]
                    customerpos = data["pos"]
                    pygame.time.set_timer(pygame.USEREVENT + 1, 3000)
                if stove.click(mouse):
                    screen = "cook"
                if board.click(mouse):
                    screen = "cook"
                if oven.click(mouse):
                    screen == "cook"
            elif screen == "cook":
                if back.click(mouse):
                    screen = "game"
                    back.reset()
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
        if event.type == pygame.USEREVENT and bool(screen == "game" or screen == "cook"):
            newCustomer()
        if event.type == pygame.USEREVENT + 1:
            order = None

    if screen == "intro":
        intro()
        screen = "menu"
    elif screen == "menu":
        menu()
    elif screen == "game":
        window.fill([255, 255, 255])
        player.draw(window)
        drawObjects()
        showOrder()
    elif screen == "cook":
        window.fill([255, 255, 255])
        cookScreen()
    pygame.display.flip()
pygame.quit()