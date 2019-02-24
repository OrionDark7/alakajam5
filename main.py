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
juicy = ui.imagebutton("spells/juicy-solution.png", [110, 425])
zesty = ui.imagebutton("spells/zestful-potion.png", [270, 425])
bitter = ui.imagebutton("spells/bitter-curse.png", [430, 425])
sweet = ui.imagebutton("spells/sweet-spell.png", [590, 425])
juicys = ui.button("Buy!", [750, 275])
zestys = ui.button("Buy!", [750, 325])
bitters = ui.button("Buy!", [750, 375])
sweets = ui.button("Buy!", [750, 425])
back = ui.button("Back", [5, 5])
next = ui.bigbutton("Next Section", [285, 550])
returntogame = ui.button("Return to Game", [328, 505])
nextday = ui.button("Next Day", [356, 400])
replayday = ui.button("Replay Day", [345, 430])
resetbutton = ui.button("Reset Spells", [282, 5])
resetbutton.color([200, 0, 0])
castbutton = ui.button("Cast Spells", [405, 5])
castbutton.color([150, 0, 200])
shopbutton = ui.button("The Magic Shop", [327, 460])
mainmenu = ui.button("Main Menu", [346, 490])
nextday.color([255, 255, 255])
replayday.color([255, 255, 255])
shopbutton.color([255, 255, 255])
mainmenu.color([255, 255, 255])
buygenerosity = ui.bigbutton("Buy!", [150, 210])
buyattraction = ui.bigbutton("Buy!", [150, 385])
buyenergized = ui.bigbutton("Buy!", [150, 535])
food = {"burger":[3, 1, 1, 0], "tacos":[3, 2, 0, 1], "fries":[2, 3, 1, 0], "cupcake":[0, 0, 0, 4], "sushi":[2, 3, 1, 1]}
foodimages = {"burger":pygame.image.load("./images/food/burger.png"),"tacos":pygame.image.load("./images/food/taco.png"),"fries":pygame.image.load("./images/food/fries.png"),"cupcake":pygame.image.load("./images/food/cupcake.png"),
              "sushi": pygame.image.load("./images/food/sushi.png")}
currentfood = {"name":None,"recipe":[0, 0, 0, 0]}
background = pygame.mixer.Channel(0)
sounds = [pygame.mixer.Sound("./sfx/backgroundnoise.wav"), pygame.mixer.Sound("./sfx/3peopletalking.wav"), pygame.mixer.Sound("./sfx/morebackgroundnoise.wav"), pygame.mixer.Sound("./sfx/peopletalking.wav")]
cooking = [pygame.mixer.Sound("./sfx/chopping.wav"), pygame.mixer.Sound("./sfx/chopping2.wav"), pygame.mixer.Sound("./sfx/waterboiling.wav"), pygame.mixer.Sound("./sfx/waterboiling2.wav")]
coins = [pygame.mixer.Sound("./sfx/sounds/coins1.wav"), pygame.mixer.Sound("./sfx/sounds/coins2.wav"), pygame.mixer.Sound("./sfx/sounds/coins3.wav")]
potionsounds = [pygame.mixer.Sound("./sfx/sounds/pouring1.wav"), pygame.mixer.Sound("./sfx/sounds/pouring2.wav")]
spellsounds = [pygame.mixer.Sound("./sfx/sounds/burner1.wav"), pygame.mixer.Sound("./sfx/sounds/burner2.wav")]
customerEnters = pygame.mixer.Sound("./sfx/sounds/bell.wav")
recipe = [0, 0, 0, 0]
dinerphotos = [pygame.image.load("./images/diner-photos/IMG_1775.JPG"), pygame.image.load("./images/diner-photos/IMG_1777.JPG"), pygame.image.load("./images/diner-photos/IMG_1781.JPG")]
dinerphoto = pygame.transform.scale(random.choice(dinerphotos), [800, 600])
howtoplay = [pygame.image.load("./images/howtoplay/HOWTOPLAY1(1).png"), pygame.image.load("./images/howtoplay/HOWTOPLAY2(1).png"), pygame.image.load("./images/howtoplay/HOWTOPLAY3(1).png"),
             pygame.image.load("./images/howtoplay/HOWTOPLAY4(1).png"), pygame.image.load("./images/howtoplay/HOWTOPLAY5(1).png"), pygame.image.load("./images/howtoplay/HOWTOPLAY6(1).png"),]
seats = [False, False, False, False]
spells = {"generosity":False, "attraction":False, "energized":False, "juicy":False, "zesty":False, "bitter":False, "sweet":False}
order = None
data = {"rating":None}
currentorder = None
comment = None
currenttable = 0
gametime = 9
day = 1
money = 10
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
spellcounter = pygame.transform.scale(spellcounter, [30, 30])
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
    global data, mouse, currentorder, money, goal, profit, spells
    if action == "serve":
        data = {"order": currentorder, "food": currentfood, "table": currenttable, "seats":seats, "rating":None, "tip":None, "comments":None}
    else:
        data = {"order": None, "seats":seats, "tip":None, "rating":None}
    customers.update(str(action), mouse, data, spells)
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
    customers.draw(window)
    counter.draw(window)
    counter2.draw(window)
    stove.draw(window)
    board.draw(window)
    oven.draw(window)
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
        positions = [25, 145, 265, 385]
        customer = entities.customer([600, positions[seat]], order)
        customers.add(customer)
        if screen == "game":
            customerEnters.play()

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

def pause():
    window.blit(bkg, [0, 0])
    chairs.draw(window)
    customers.draw(window)
    counter.draw(window)
    counter2.draw(window)
    stove.draw(window)
    board.draw(window)
    oven.draw(window)
    window.blit(titlebox, [0, 2])
    window.blit(logo, [45, -133])
    window.blit(infobox, [220, 500])
    font = pygame.font.Font("./font/Lobster_1.3.otf", 24)
    returntogame.draw(window)
    quitbutton.draw(window)
    howto.draw(window)

def cookScreen():
    global window, spellcounter
    window.fill([200, 200, 200])
    table = pygame.surface.Surface([800, 240])
    table.fill([163, 77, 0])
    back.draw(window)
    window.blit(table, [0, 360])
    font = pygame.font.Font("./font/Lobster_1.3.otf", 24)
    render = font.render("Juicy Solution", 1, [0, 0, 0])
    position = 160 - (render.get_rect().width/2)
    window.blit(render, [position, 570])
    render = font.render("Zestful Potion", 1, [0, 0, 0])
    position = 320 - (render.get_rect().width / 2)
    window.blit(render, [position, 570])
    render = font.render("Bitter Curse", 1, [0, 0, 0])
    position = 480 - (render.get_rect().width / 2)
    window.blit(render, [position, 570])
    render = font.render("Sweet Spell", 1, [0, 0, 0])
    position = 640 - (render.get_rect().width / 2)
    window.blit(render, [position, 570])
    resetbutton.draw(window)
    castbutton.draw(window)
    juicy.draw(window)
    zesty.draw(window)
    bitter.draw(window)
    sweet.draw(window)
    if not currentorder == None:
        window.blit(foodimages[currentorder], [200, 20])
    for i in range(recipe[0]):
        window.blit(spellcounter, [(i * 35) + 90, 530])
    for i in range(recipe[1]):
        window.blit(spellcounter, [(i * 35) + 250, 530])
    for i in range(recipe[2]):
        window.blit(spellcounter, [(i * 35) + 410, 530])
    for i in range(recipe[3]):
        window.blit(spellcounter, [(i * 35) + 570, 530])

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
    shopbutton.draw(window)
    mainmenu.draw(window)

def shop():
    global window, back, money
    bigfont = pygame.font.Font("./font/Lobster_1.3.otf", 48)
    font = pygame.font.Font("./font/Lobster_1.3.otf", 24)
    window.fill([0, 0, 0])
    back.draw(window)
    render = bigfont.render("The Magic Shop", 1, [255, 255, 255])
    position = 400-(render.get_rect().width/2)
    window.blit(render, [position, 10])
    render = font.render("Money: $" + str(money), 1, [255, 255, 255])
    position = 400 - (render.get_rect().width / 2)
    window.blit(render, [position, 55])

    pygame.draw.line(window, [255, 255, 255], [400, 80], [400, 800], 2)
    pygame.draw.line(window, [255, 255, 255], [0, 80], [800, 80], 2)

    #GENEROSITY SPELL
    render = bigfont.render("Generosity Spell", 1, [255, 255, 255])
    window.blit(render, [10, 85])
    render = font.render("The Generosity Spell is a spell that makes", 1, [255, 255, 255])
    window.blit(render, [10, 125])
    render = font.render("customers leave more generous tips when", 1, [255, 255, 255])
    window.blit(render, [10, 150])
    render = font.render("served good food.", 1, [255, 255, 255])
    window.blit(render, [10, 175])
    render = bigfont.render("$100", 1, [255, 255, 255])
    window.blit(render, [10, 210])
    if money >= 100:
        buygenerosity.color([0, 200, 0])
    else:
        buygenerosity.color([200, 0, 0])
    if not spells["generosity"]:
        buygenerosity.draw(window)

    #ATTRACTION FIELD
    render = bigfont.render("Attraction Field", 1, [255, 255, 255])
    window.blit(render, [10, 260])
    render = font.render("The Attraction Field is a spell that", 1, [255, 255, 255])
    window.blit(render, [10, 300])
    render = font.render("makes more customers come to your", 1, [255, 255, 255])
    window.blit(render, [10, 325])
    render = font.render("Restaurant more often.", 1, [255, 255, 255])
    window.blit(render, [10, 350])
    render = bigfont.render("$120", 1, [255, 255, 255])
    window.blit(render, [10, 385])
    if money >= 120:
        buyattraction.color([0, 200, 0])
    else:
        buyattraction.color([200, 0, 0])
    if not spells["attraction"]:
        buyattraction.draw(window)

    #ENERGIZED SPELL
    render = bigfont.render("Energy Spell", 1, [255, 255, 255])
    window.blit(render, [10, 435])
    render = font.render("The Energy Spell gives you Energy to", 1, [255, 255, 255])
    window.blit(render, [10, 475])
    render = font.render("keep the Restaurant open until 12:00 AM.", 1, [255, 255, 255])
    window.blit(render, [10, 500])
    render = bigfont.render("$50", 1, [255, 255, 255])
    window.blit(render, [10, 535])
    if money >= 50:
        buyenergized.color([0, 200, 0])
    else:
        buyenergized.color([200, 0, 0])
    if not spells["energized"]:
        buyenergized.draw(window)

    #SPELL IMPROVEMENT SECTION + DESCRIPTION
    render = bigfont.render("Spell Improvements", 1, [255, 255, 255])
    window.blit(render, [410, 85])
    render = font.render("On this side of the shop, you can buy", 1, [255, 255, 255])
    window.blit(render, [410, 125])
    render = font.render("improvements for your different spells.", 1, [255, 255, 255])
    window.blit(render, [410, 150])
    render = font.render("These improvements will improve the", 1, [255, 255, 255])
    window.blit(render, [410, 175])
    render = font.render("rating of the food when that spell is", 1, [255, 255, 255])
    window.blit(render, [410, 200])
    render = font.render("mainly used.", 1, [255, 255, 255])
    window.blit(render, [410, 225])

    #PERFECTED SOLUTION

    render = font.render("Perfected Juice Solution - $20", 1, [255, 255, 255])
    window.blit(render, [410, 275])
    if money >= 20:
        juicys.color([0, 200, 0])
    else:
        juicys.color([200, 0, 0])
    if not spells["juicy"]:
        juicys.draw(window)

    #FLOWING POTION

    render = font.render("Flowing Zestful Potion - $50", 1, [255, 255, 255])
    window.blit(render, [410, 325])
    if money >= 50:
        zestys.color([0, 200, 0])
    else:
        zestys.color([200, 0, 0])
    if not spells["zesty"]:
        zestys.draw(window)

    #AGING BITTER SPELL

    render = font.render("Aging Bitter Spell - $100", 1, [255, 255, 255])
    window.blit(render, [410, 375])
    if money >= 100:
        bitters.color([0, 200, 0])
    else:
        bitters.color([200, 0, 0])
    if not spells["bitter"]:
        bitters.draw(window)

    #SWEET-TOOTH REFINEMENTS

    render = font.render("Sweet-Tooth Refinements - $200", 1, [255, 255, 255])
    window.blit(render, [410, 425])
    if money >= 200:
        sweets.color([0, 200, 0])
    else:
        sweets.color([200, 0, 0])
    if not spells["sweet"]:
        sweets.draw(window)

howtoindex = 0
def howtoscreen():
    global howtoplay, howtoindex, screen, prev
    window.fill([0, 0, 0])
    try:
        window.blit(pygame.transform.scale(howtoplay[howtoindex], [800, 600]), [0, 0])
    except:
        screen = prev
    next.color([255, 255, 255])

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
    global background, sounds, cooking, screen
    if screen == "game":
        if not background.get_busy():
            if countCustomers() > 0 and countCustomers() <= 2:
                background.play(sounds[0])
            elif countCustomers() == 3:
                background.play(sounds[random.randint(1, 2)])
            elif countCustomers() == 4:
                background.play(sounds[3])
    elif screen == "cook":
        if not background.get_busy():
            random.choice(cooking).play()

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
                        prev = "menu"
                elif screen == "how-to":
                    if back.click(mouse):
                        screen = str(prev)
                        back.color([0, 0, 0])
                        back.reset()
                        dinerphoto = pygame.transform.scale(random.choice(dinerphotos), [800, 600])
                    if next.click(mouse):
                        try:
                            howtoindex += 1
                        except:
                            screen = prev
                        next.reset()
                elif screen == "pause":
                    if returntogame.click(mouse):
                        screen = "game"
                        returntogame.reset()
                        background.unpause()
                        pygame.mixer.unpause()
                    if quitbutton.click(mouse):
                        screen = "menu"
                        quitbutton.reset()
                        background.stop()
                        pygame.mixer.stop()
                    if howto.click(mouse):
                        screen = "how-to"
                        back.color([255, 255, 255])
                        howto.reset()
                        prev = "pause"
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
                        background.stop()
                    elif board.click(mouse) and not currentorder == None:
                        screen = "cook"
                        recipe = [0, 0, 0, 0]
                        background.stop()
                    elif oven.click(mouse) and not currentorder == None:
                        screen = "cook"
                        recipe = [0, 0, 0, 0]
                        background.stop()
                elif screen == "cook":
                    if back.click(mouse):
                        screen = "game"
                        back.reset()
                        background.fadeout(1000)
                        pygame.mixer.fadeout(1000)
                    elif juicy.click(mouse) and recipe[0] < 4:
                        recipe[0] += 1
                        if recipe[0] == 1:
                            random.choice(potionsounds).play()
                    elif zesty.click(mouse) and recipe[1] < 4:
                        recipe[1] += 1
                        if recipe[1] == 1:
                            random.choice(potionsounds).play()
                    elif bitter.click(mouse) and recipe[2] < 4:
                        recipe[2] += 1
                        if recipe[2] == 1:
                            random.choice(spellsounds).play()
                    elif sweet.click(mouse) and recipe[3] < 4:
                        recipe[3] += 1
                        if recipe[3] == 1:
                            random.choice(spellsounds).play()

                    elif castbutton.click(mouse):
                        currentfood["name"] = currentorder
                        currentfood["recipe"] = recipe
                        screen = "game"
                        castbutton.reset()
                        background.fadeout(1000)
                        pygame.mixer.fadeout(1000)
                    elif resetbutton.click(mouse):
                        recipe = [0, 0, 0, 0]
                        resetbutton.reset()
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
                    if shopbutton.click(mouse):
                        screen = "shop"
                        back.color([255, 255, 255])
                        shopbutton.reset()
                elif screen == "shop":
                    if back.click(mouse):
                        screen = "day-end"
                        back.reset()
                    if buygenerosity.click(mouse):
                        if not spells["generosity"] and money >= 100:
                            spells["generosity"] = True
                            money -= 100
                            random.choice(coins).play()
                        buygenerosity.reset()
                    if buyattraction.click(mouse):
                        if not spells["attraction"] and money >= 120:
                            spells["attraction"] = True
                            money -= 120
                            pygame.time.set_timer(pygame.USEREVENT, 10000)
                            random.choice(coins).play()
                        buyattraction.reset()
                    if buyenergized.click(mouse):
                        if not spells["energized"] and money >= 50:
                            spells["energized"] = True
                            money -= 50
                            random.choice(coins).play()
                        buyenergized.reset()
                    if juicys.click(mouse):
                        if not spells["juicy"] and money >= 20:
                            spells["juicy"] = True
                            money -= 20
                            random.choice(coins).play()
                        juicys.reset()
                    if zestys.click(mouse):
                        if not spells["zesty"] and money >= 50:
                            spells["zesty"] = True
                            money -= 50
                            random.choice(coins).play()
                        zestys.reset()
                    if bitters.click(mouse):
                        if not spells["bitter"] and money >= 100:
                            spells["bitter"] = True
                            money -= 100
                            random.choice(coins).play()
                        bitters.reset()
                    if sweets.click(mouse):
                        if not spells["sweet"] and money >= 200:
                            spells["sweet"] = True
                            money -= 200
                            random.choice(coins).play()
                        sweets.reset()

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
                    screen = "pause"
                    background.pause()
                    pygame.mixer.pause()
                elif pressed[pygame.K_x]:
                    currentorder = None
                    currenttable = 0
            elif screen == "pause":
                if pressed[pygame.K_ESCAPE]:
                    screen = "game"
                    background.unpause()
                    pygame.mixer.unpause()
        if event.type == pygame.USEREVENT and bool(screen == "game" or screen == "cook"):
            newCustomer()
        if event.type == pygame.USEREVENT + 1:
            order = None
            update("leave")
            comment = None
        if event.type == pygame.USEREVENT + 2 and bool(screen == "game" or screen == "cook"):
            if gametime == 23:
                gametime = 0 #Midnight
            else:
                gametime += 1 #Add 1 Hour

            if gametime == 21 and not spells["energized"]:
                screen = "day-end"
                spells["energized"] = False
                background.fadeout(1000)
                pygame.mixer.fadeout(1000)
            elif gametime == 0 and spells["energized"]:
                screen = "day-end"
                spells["energized"] = False
                background.fadeout(1000)
                pygame.mixer.fadeout(1000)

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
            spells["energized"] = False
            background.fadeout(1000)
            pygame.mixer.fadeout(1000)
        drawObjects()
        player.draw(window)
        showOrder()
        if not data["rating"] == None:
            showRating()
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
        howtoscreen()
        back.draw(window)
        next.draw(window)
    elif screen == "shop":
        shop()
    elif screen == "pause":
        window.fill([0, 0, 0])
        pause()
    pygame.display.flip()
pygame.quit()