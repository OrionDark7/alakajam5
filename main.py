import pygame, time, random #Global Dependencies
import ui, entities, objects #Project Libraries

#Juicy Zesty Bitter Sweet - Copyright (c) 2019 Orion Williams

#VARIABLE DECLARATIONS
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode([800, 600])
pygame.display.set_caption("juicyZESTYbitterSWEET")
running = True
mouse = [0, 0]
screen = "intro"
player = entities.player([380, 280])
play = ui.button("Play Game", [349, 505])
howto = ui.button("How to Play", [344, 535])
quitbutton = ui.button("Quit Game", [350, 565])
juicy = ui.button("Juicy", [50, 100])
zesty = ui.button("Zesty", [50, 160])
bitter = ui.button("Bitter", [50, 220])
sweet = ui.button("Sweet", [50, 280])
cookbutton = ui.bigbutton("Cook 'n Cast!", [283, 550])
back = ui.button("Back", [5, 5])
nextday = ui.button("Next Day", [356, 400])
replayday = ui.button("Replay Day", [345, 430])
reset = ui.button("Reset Spells", [10, 340])
mainmenu = ui.button("Main Menu", [346, 460])
nextday.color([255, 255, 255])
replayday.color([255, 255, 255])
mainmenu.color([255, 255, 255])
food = {"burger":[3, 1, 1, 0], "tacos":[3, 2, 0, 1], "fries":[2, 3, 1, 0], "cupcake":[0, 0, 0, 4], "sushi":[2, 3, 1, 1]}
foodimages = {"burger":pygame.image.load("./images/food/burger.png"),"tacos":pygame.image.load("./images/food/taco.png"),"fries":pygame.image.load("./images/food/fries.png"),"cupcake":pygame.image.load("./images/food/cupcake.png"),
              "sushi": pygame.image.load("./images/food/sushi.png")}
currentfood = {"name":None,"recipe":[0, 0, 0, 0]}
background = pygame.mixer.Channel(0)
sounds = [pygame.mixer.Sound("./sfx/backgroundnoise.wav"), pygame.mixer.Sound("./sfx/3peopletalking.wav"), pygame.mixer.Sound("./sfx/morebackgroundnoise.wav"), pygame.mixer.Sound("./sfx/peopletalking.wav")]
recipe = [0, 0, 0, 0]
dinerphotos = [pygame.image.load("./images/diner-photos/IMG_1775.JPG"), pygame.image.load("./images/diner-photos/IMG_1777.JPG"), pygame.image.load("./images/diner-photos/IMG_1781.JPG")]
dinerphoto = pygame.transform.scale(random.choice(dinerphotos), [800, 600])
seats = [False, False, False, False]
order = None
data = {"rating":None}
currentorder = None
comment = None
currenttable = 0
gametime = 9
day = 1
money = 100
goal = 50
goals = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
profit = 0
pos = [0, 0]
titlebox = pygame.image.load("./images/titlebox.png")
logo = pygame.image.load("./images/logo.png")
potion = pygame.image.load("./images/potion.png")
potion = pygame.transform.scale(potion, [40, 40])
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
    global data, mouse, currentorder, money, goal, profit
    if action == "serve":
        data = {"order": currentorder, "food": currentfood, "table": currenttable, "seats":seats, "rating":None, "tip":None, "comment":None}
    else:
        data = {"order": None, "seats":seats, "tip":None, "rating":None}
    customers.update(str(action), mouse, data)
    if not data["tip"] == None:
        money += data["tip"]
        profit += data["tip"]
        goal -= data["tip"]

def intro():
    window.fill([0, 0, 0])
    font = pygame.font.Font("./font/Lobster_1.3.otf", 24)
    render = font.render("An Alakajam! #5 Entry", 1, [255, 255, 255])
    rect = 400 - (render.get_rect().width / 2)
    window.blit(render, [rect, 300])
    pygame.display.flip()
    time.sleep(2)

def menu():
    window.fill([0, 0, 0])
    window.blit(dinerphoto, [0, 0])
    window.blit(titlebox, [0, 2])
    window.blit(logo, [45, -133])
    window.blit(infobox, [220, 500])
    font = pygame.font.Font("./font/Lobster_1.3.otf", 24)
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
    render = font.render("Money: $" + str(money) + " - Goal: Earn $" + str(goal), 1, [0, 0, 0])
    window.blit(render, [135, 10])
    if gametime < 12:
        render = font.render("Time: " + str(gametime) + ":00 AM - Day " + str(day), 1, [0, 0, 0])
    elif gametime == 12:
        render = font.render("Time: 12:00 PM - Day " + str(day), 1, [0, 0, 0])
    else:
        render = font.render("Time: " + str(gametime - 12) + ":00 PM - Day " + str(day), 1, [0, 0, 0])
    window.blit(render, [135, 40])
    if not currentorder == None:
        render = font.render(currentorder.capitalize() + " for Customer #" + str(currenttable), 1, [0, 0, 0])
        window.blit(render, [135, 70])
    elif currentorder == None and not comment == None:
        render = font.render("Customer says: " + str(comment), 1, [0, 0, 0])
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
    window.fill([200, 200, 200])
    table = pygame.surface.Surface([800, 200])
    table.fill([163, 77, 0])
    window.blit(table, [0, 400])
    window.blit(potion, [5, 80])
    juicy.draw(window)
    window.blit(potion, [5, 140])
    zesty.draw(window)
    window.blit(potion, [5, 200])
    bitter.draw(window)
    window.blit(potion, [5, 260])
    sweet.draw(window)
    back.draw(window)
    cookbutton.draw(window)
    reset.draw(window)
    if not currentorder == None:
        window.blit(foodimages[currentorder], [380, 100])
    for i in range(recipe[0]):
        window.blit(spellcounter, [(i * 75) + 110, 75])
    for i in range(recipe[1]):
        window.blit(spellcounter, [(i * 75) + 110, 160 - 25])
    for i in range(recipe[2]):
        window.blit(spellcounter, [(i * 75) + 110, 220 - 25])
    for i in range(recipe[3]):
        window.blit(spellcounter, [(i * 75) + 110, 280 - 25])

def endScreen():
    global window, day
    bigfont = pygame.font.Font("./font/Lobster_1.3.otf", 48)
    font = pygame.font.Font("./font/Lobster_1.3.otf", 24)
    render = bigfont.render("Day " + str(day) + " Completed!", 1, [255, 255, 255])
    position = 400 - (render.get_rect().width/2)
    window.blit(render, [position, 100])
    if goal == 0:
        render = font.render("Goal Completed!", 1, [255, 255, 255])
    else:
        render = font.render("Goal Failed...", 1, [255, 255, 255])
    position = 400 - (render.get_rect().width / 2)
    window.blit(render, [position, 150])
    render = font.render("Today's Profit: $" + str(profit), 1, [255, 255, 255])
    position = 400 - (render.get_rect().width / 2)
    window.blit(render, [position, 190])
    render = font.render("Overall Cash: $" + str(money), 1, [255, 255, 255])
    position = 400 - (render.get_rect().width / 2)
    window.blit(render, [position, 220])
    if goal == 0:
        nextday.draw(window)
    replayday.draw(window)
    mainmenu.draw(window)

def night():
    global time
    if gametime > 15:
        surface = pygame.surface.Surface([800, 600])
        surface.fill([0, 0, 0])
        surface.set_alpha((100 * i) - 1500)
        window.blit(surface, [0, 0])

def countCustomers():
    global seats
    customercount = 0
    if seats[0]:
        customercount += 1
    if seats[1]:
        customercount += 1
    if seats[2]:
        customercount += 1
    if seats[3]:
        customercount += 1
    return customercount

def backgroundNoise():
    global background, sounds
    if not background.get_busy():
        if countCustomers() > 0 and countCustomers() <= 2:
            background.play(sounds[0])
        elif countCustomers() == 3:
            background.play(sounds[random.randint(1, 2)])
        elif countCustomers() == 4:
            background.play(sounds[3])

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
                    if howto.click(mouse):
                        screen = "how-to"
                        back.color([255, 255, 255])
                        howto.reset()
                elif screen == "how-to":
                    if back.click(mouse):
                        screen = "menu"
                        back.color([0, 0, 0])
                        back.reset()
                        dinerphoto = pygame.transform.scale(random.choice(dinerphotos), [800, 600])
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
                            if not data["comments"] == None:
                                comment = data["comments"]
                            currenttable = 0
                            pygame.time.set_timer(pygame.USEREVENT + 1, 3000)

                    if stove.click(mouse) and not currentorder == None:
                        screen = "cook"
                        recipe = [0, 0, 0, 0]
                    elif board.click(mouse) and not currentorder == None:
                        screen = "cook"
                        recipe = [0, 0, 0, 0]
                    elif oven.click(mouse) and not currentorder == None:
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
                    elif reset.click(mouse):
                        recipe = [0, 0, 0, 0]
                        reset.reset()
                elif screen == "day-end":
                    if replayday.click(mouse):
                        screen = "game"
                        goal = goals[day - 1]
                        profit = 0
                        gametime = 9
                        customers.empty()
                        newCustomer()
                        replayday.reset()
                    if nextday.click(mouse) and goal == 0:
                        screen = "game"
                        day += 1
                        gametime = 9
                        goal = goals[day - 1]
                        profit = 0
                        customers.empty()
                        newCustomer()
                        nextday.reset()
                    if mainmenu.click(mouse):
                        screen = "menu"
                        gametime = 9
                        goal = goals[day - 1]
                        profit = 0
                        customers.empty()
                        mainmenu.reset()
                        dinerphoto = pygame.transform.scale(random.choice(dinerphotos), [800, 600])
            if pressed[2]:
                if screen == "game":
                    update("click")
                    if not data["order"] == None:
                        order = data["order"]
                        customerpos = data["pos"]
                        pygame.time.set_timer(pygame.USEREVENT + 1, 3000)

        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if screen == "game":
                if pressed[pygame.K_ESCAPE]:
                    print "pause menu goes here"
                elif pressed[pygame.K_x]:
                    currentorder = None
                    currenttable = 0
        if event.type == pygame.USEREVENT and bool(screen == "game" or screen == "cook"):
            newCustomer()
        if event.type == pygame.USEREVENT + 1:
            order = None
            update("leave")
            comment = None
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
        if goal <= 0:
            goal = 0
            screen = "day-end"
            background.fadeout(1000)
        drawObjects()
        player.draw(window)
        showOrder()
        if not data["rating"] == None:
            showRating()
        night()
        backgroundNoise()
    elif screen == "cook":
        window.fill([255, 255, 255])
        cookScreen()
        backgroundNoise()
    elif screen == "day-end":
        window.fill([0, 0, 0])
        endScreen()
    elif screen == "how-to":
        window.fill([0, 0, 0])
        back.draw(window)
    pygame.display.flip()
pygame.quit()