import pygame, time, random #Global Dependencies
import ui, entities, objects #Project Libraries

#Juicy Zesty Bitter Sweet - Copyright (c) 2019 Orion Williams

#VARIABLE DECLARATIONS
pygame.init()
window = pygame.display.set_mode([800, 600])
pygame.display.set_caption("juicyZESTYbitterSWEET")
running = True
mouse = [0, 0]
screen = "intro"
player = entities.player([380, 280])
play = ui.button("Play Game", [10, 60])
howto = ui.button("How to Play", [10, 90])
quitbutton = ui.button("Quit Game", [10, 120])
juicy = ui.button("Juicy", [10, 100])
zesty = ui.button("Zesty", [10, 160])
bitter = ui.button("Bitter", [10, 220])
sweet = ui.button("Sweet", [10, 280])
cookbutton = ui.bigbutton("Cook 'n Cast!", [283, 550])
back = ui.button("Back", [5, 5])
food = {"burger":[3, 1, 1, 0], "tacos":[3, 2, 0, 1], "fries":[2, 3, 1, 0], "cupcake":[0, 0, 0, 4], "sushi":[2, 3, 1, 1]}
foodimages = {"burger":pygame.image.load("./images/food/burger.png"),"tacos":pygame.image.load("./images/food/taco.png"),"fries":pygame.image.load("./images/food/fries.png"),"cupcake":pygame.image.load("./images/food/cupcake.png"),
              "sushi": pygame.image.load("./images/food/sushi.png")}
currentfood = {"name":None,"recipe":[0, 0, 0, 0]}
recipe = [0, 0, 0, 0]
seats = [False, False, False, False]
order = None
data = {"rating":None}
currentorder = None
currenttable = 0
gametime = 15
money = 100
pos = [0, 0]
bkg = pygame.image.load("./images/floor.png")
infobox = pygame.image.load("./images/infobox.png")
infobox = pygame.transform.scale(infobox, [360, 100])
spellcounter = pygame.image.load("./images/counter.png")
spellcounter = pygame.transform.scale(spellcounter, [50, 50])
bubble = pygame.image.load("./images/speech-bubble.png")
bubble = pygame.transform.scale(bubble, [100, 100])
pygame.time.set_timer(pygame.USEREVENT, 20000)
pygame.time.set_timer(pygame.USEREVENT + 2, 30000)

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
    global data, mouse, currentorder, money
    if action == "serve":
        data = {"order": currentorder, "food": currentfood, "table": currenttable, "seats":seats, "rating":None, "tip":None}
    else:
        data = {"order": None, "seats":seats, "tip":None, "rating":None}
    customers.update(str(action), mouse, data)
    if not data["tip"] == None:
        money += data["tip"]

def intro():
    window.fill([0, 0, 0])
    font = pygame.font.Font("./font/Lobster_1.3.otf", 24)
    render = font.render("An Alakajam! #5 Entry", 1, [255, 255, 255])
    rect = 400 - (render.get_rect().width / 2)
    window.blit(render, [rect, 300])
    pygame.display.flip()
    time.sleep(2)

def menu():
    window.fill([255, 255, 255])
    font = pygame.font.Font("./font/Lobster_1.3.otf", 48)
    render = font.render("juicy ZESTY bitter SWEET", 1, [0, 0, 0])
    window.blit(render, [5, 5])
    play.draw(window)
    quitbutton.draw(window)
    howto.draw(window)

def drawObjects():
    global counter, counter2, chairs, stove, board, oven, customers, money
    window.blit(bkg, [0, 0])
    chairs.draw(window)
    counter.draw(window)
    counter2.draw(window)
    stove.draw(window)
    board.draw(window)
    oven.draw(window)
    customers.draw(window)
    font = pygame.font.Font("./font/Lobster_1.3.otf", 24)
    window.blit(infobox, [125, 2])
    render = font.render("Money: $" + str(money), 1, [0, 0, 0])
    window.blit(render, [135, 10])
    if gametime < 12:
        render = font.render("Time: " + str(gametime) + ":00 AM", 1, [0, 0, 0])
    elif gametime == 12:
        render = font.render("Time: 12:00 PM", 1, [0, 0, 0])
    else:
        render = font.render("Time: " + str(gametime - 12) + ":00 PM", 1, [0, 0, 0])
    window.blit(render, [135, 40])
    if not currentorder == None:
        render = font.render(currentorder.capitalize() + " for Customer #" + str(currenttable), 1, [0, 0, 0])
        window.blit(render, [135, 70])

def newCustomer():
    global seats, customers
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
    if not order == None and seats[((customerpos[1] - 37)/120)]:
        image = pygame.transform.scale(foodimages[order], [50, 50])
        window.blit(bubble, (customerpos[0] + 80, customerpos[1] - 20))
        window.blit(image, (customerpos[0] + 110, customerpos[1]))

def showRating():
    global data, customerpos
    window.blit(bubble, (customerpos[0] + 80, customerpos[1] - 20))
    font = pygame.font.Font("./font/Lobster_1.3.otf", 18)
    if len(str(int(data["rating"]))) == 2:
        render = font.render(str(float(data["rating"]))[0:2] + "/10", 1, [0, 0, 0])
    elif len(str(int(data["rating"]))) == 1:
        render = font.render(str(int(data["rating"])) + "/10", 1, [0, 0, 0])
    else:
        render = font.render(str(float(data["rating"]))[0:3] + "/10", 1, [0, 0, 0])
    if not data["tip"] == None and not data["tip"] == 0:
        window.blit(render, (customerpos[0] + 110, customerpos[1] + 5))
    else:
        window.blit(render, (customerpos[0] + 110, customerpos[1] + 20))
    if not data["tip"] == None and not data["tip"] == 0:
        render = font.render("+ $" + str(data["tip"]), 1, [0, 128, 0])
        window.blit(render, (customerpos[0] + 110, customerpos[1] + 35))

def cookScreen():
    global window, spellcounter
    table = pygame.surface.Surface([800, 200])
    table.fill([163, 77, 0])
    window.blit(table, [0, 400])
    juicy.draw(window)
    zesty.draw(window)
    bitter.draw(window)
    sweet.draw(window)
    back.draw(window)
    cookbutton.draw(window)
    if not currentorder == None:
        window.blit(foodimages[currentorder], [370, 100])
    for i in range(recipe[0]):
        window.blit(spellcounter, [(i * 75) + 75, 75])
    for i in range(recipe[1]):
        window.blit(spellcounter, [(i * 75) + 75, 160 - 25])
    for i in range(recipe[2]):
        window.blit(spellcounter, [(i * 75) + 75, 220 - 25])
    for i in range(recipe[3]):
        window.blit(spellcounter, [(i * 75) + 75, 280 - 25])

def night():
    global time
    if gametime > 15:
        surface = pygame.surface.Surface([800, 600])
        surface.fill([0, 0, 0])
        surface.set_alpha(1500) #(100 * i) -
        window.blit(surface, [0, 0])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = [event.pos[0], event.pos[1]]
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                if screen == "menu":
                    if play.click(mouse):
                        screen = "game"
                        play.reset()
                        newCustomer()
                    if quitbutton.click(mouse):
                        running = False
                        quitbutton.reset()
                elif screen == "game":
                    if currentorder == None:
                        update("click")
                        if not data["order"] == None:
                            order = data["order"]
                            customerpos = data["pos"]
                            pygame.time.set_timer(pygame.USEREVENT + 1, 3000)
                            currentorder = data["order"]
                            currenttable = data["table"]
                    else:
                        update("serve")
                        if not data["rating"] == None:
                            currentfood = {"name": None, "recipe": [0, 0, 0, 0]}
                            currentorder = None
                            currenttable = 0
                            pygame.time.set_timer(pygame.USEREVENT + 1, 3000)

                    if stove.click(mouse) and not currentorder == None:
                        screen = "cook"
                        recipe = [0, 0, 0, 0]
                    if board.click(mouse) and not currentorder == None:
                        screen = "cook"
                        recipe = [0, 0, 0, 0]
                    if oven.click(mouse) and not currentorder == None:
                        screen = "cook"
                        recipe = [0, 0, 0, 0]
                elif screen == "cook":
                    if back.click(mouse):
                        screen = "game"
                        back.reset()
                    elif juicy.click(mouse) and recipe[0] < 4:
                        recipe[0] += 1
                        juicy.reset()
                    elif zesty.click(mouse) and recipe[1] < 4:
                        recipe[1] += 1
                        zesty.reset()
                    elif bitter.click(mouse) and recipe[2] < 4:
                        recipe[2] += 1
                        bitter.reset()
                    elif sweet.click(mouse) and recipe[3] < 4:
                        recipe[3] += 1
                        sweet.reset()
                    elif cookbutton.click(mouse):
                        currentfood["name"] = currentorder
                        currentfood["recipe"] = recipe
                        screen = "game"
                        cookbutton.reset()
                        print currentfood
            if pressed[2]:
                if screen == "game":
                    update("click")
                    if not data["order"] == None:
                        order = data["order"]
                        customerpos = data["pos"]
                        pygame.time.set_timer(pygame.USEREVENT + 1, 3000)
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
        if event.type == pygame.USEREVENT and bool(screen == "game" or screen == "cook"):
            newCustomer()
        if event.type == pygame.USEREVENT + 1:
            order = None
            update("leave")
        if event.type == pygame.USEREVENT + 2:
            gametime += 1
            if gametime == 21:
                screen = "day-end"

    if screen == "intro":
        intro()
        screen = "menu"
    elif screen == "menu":
        menu()
    elif screen == "game":
        window.fill([255, 255, 255])
        drawObjects()
        player.draw(window)
        showOrder()
        if not data["rating"] == None:
            showRating()
    elif screen == "cook":
        window.fill([255, 255, 255])
        cookScreen()
    elif screen == "day-end":
        window.fill([0, 0, 0])
        night()
    pygame.display.flip()
pygame.quit()