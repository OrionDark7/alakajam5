import pygame, random

pygame.mixer.init()
food = {"burger":[3, 1, 1, 0], "tacos":[3, 2, 0, 1], "fries":[2, 3, 1, 0], "cupcake":[0, 0, 0, 4], "sushi":[2, 3, 1, 1]}
comments = ["Dang, that's good!", "Perfect!", "Mmm, tasty!", "Just how I like it!", "Big tip for you!", "Culinary Genius!", "I'd eat here again."]

class player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/player.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
    def draw(self, surface):
        surface.blit(self.image, [self.rect.left, self.rect.top])

class customer(pygame.sprite.Sprite):
    def __init__(self, pos, order):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/customers/customer" + str(random.randint(1, 3)) + ".png")
        self.image = pygame.transform.scale(self.image, [75,75])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
        self.order = str(order)
        self.table = ((self.rect.top - 25) / 120) + 1
        self.toleave = False
        self.chewing = [pygame.mixer.Sound("./sfx/sounds/crunching.wav"), pygame.mixer.Sound("./sfx/sounds/crunching2.wav"), pygame.mixer.Sound("./sfx/sounds/slurping.wav")]
        self.tip = [pygame.mixer.Sound("./sfx/sounds/coins1.wav"), pygame.mixer.Sound("./sfx/sounds/coins2.wav"), pygame.mixer.Sound("./sfx/sounds/coins3.wav")]
    def draw(self, surface):
        surface.blit(self.image, [self.rect.left, self.rect.top])
    def update(self, action, mouse, data, spells):
        global food, comments
        if action == "click" and self.rect.collidepoint(mouse):
            data["order"] = self.order
            data["pos"] = self.rect.left, self.rect.top
            data["table"] = self.table
        elif action == "serve" and self.rect.collidepoint(mouse) and data["table"] == self.table and data["food"]["name"] == self.order:
            self.toleave = True
            rating1 = 0
            rating2 = 0
            rating3 = 0
            rating4 = 0
            data["comments"] = "Some good Food!"
            if data["food"]["recipe"] == food[data["food"]["name"]]:
                rating = 1
                data["comments"] = random.choice(comments)
            else:
                if not food[data["food"]["name"]][0] == 0:
                    rating1 = float(data["food"]["recipe"][0] / food[data["food"]["name"]][0])
                    if rating1 >= 0.6:
                        rating1 = 1
                    if rating1 > 1:
                        rating1 = 1 - (rating1 - 1)
                        data["comments"] = "A little too juicy."
                    elif rating1 < 1:
                        data["comments"] = "Dry, not juicy enough."
                else:
                    if data["food"]["recipe"][0] > 0:
                        rating1 = 1 - (float(data["food"]["recipe"][0])/4)
                        data["comments"] = "This is really juicy."
                    else:
                        rating1 = 1
                if not food[data["food"]["name"]][1] == 0:
                    rating2 = float(data["food"]["recipe"][1] / food[data["food"]["name"]][1])
                    if rating2 >= 0.6:
                        rating2 = 1
                    if rating2 > 1:
                        rating2 = 1 - (rating2 - 1)
                        data["comments"] = "Yep, that's too zesty."
                    elif rating2 < 1:
                        data["comments"] = "Not zesty enough."
                else:
                    if data["food"]["recipe"][1] > 0:
                        rating2 = 1 - (float(data["food"]["recipe"][1])/4)
                        data["comments"] = "Woah, really zesty!"
                    else:
                        rating2 = 1
                if not food[data["food"]["name"]][2] == 0:
                    rating3 = float(data["food"]["recipe"][2] / food[data["food"]["name"]][2])
                    if rating3 >= 0.6:
                        rating3 = 1
                    if rating3 > 1:
                        rating3 = 1 - (rating3 - 1)
                        data["comments"] = "That's really bitter..."
                    elif rating3 < 1:
                        data["comments"] = "Not bitter enough."
                else:
                    if data["food"]["recipe"][2] > 0:
                        rating3 = 1 - (float(data["food"]["recipe"][2])/4)
                        data["comments"] = "Yuck! Too bitter!"
                    else:
                        rating3 = 1
                if not food[data["food"]["name"]][3] == 0:
                    rating4 = float(data["food"]["recipe"][3] / food[data["food"]["name"]][3])
                    if rating4 >= 0.6:
                        rating4 = 1
                    if rating4 > 1:
                        rating4 = 1 - (rating4 - 1)
                        data["comments"] = "Too sweet!"
                    elif rating4 < 1:
                        data["comments"] = "Eh, not sweet enough."
                else:
                    if data["food"]["recipe"][3] > 0:
                        rating4 = 1 - (float(data["food"]["recipe"][3])/4)
                        data["comments"] = "Woah, too sweet!"
                    else:
                        rating4 = 1
                print float(rating1 +  rating2 + rating3 + rating4) / 4
                rating = float(float(rating1 + rating2 + rating3 + rating4) / 4)
            data["rating"] = float(rating) * 10
            random.choice(self.chewing).play()
            if rating > 0.8:
                if rating == 1 and data["comments"] == "Big tip for you!": #What? You thought I was joking about that?
                    if spells["generosity"]:
                        data["tip"] = int(rating * random.randint(28, 32))
                        random.choice(self.tip).play()
                    else:
                        data["tip"] = int(rating * random.randint(18, 22))
                        random.choice(self.tip).play()
                else:
                    if spells["generosity"]:
                        data["tip"] = int(rating * random.randint(13, 17))
                        random.choice(self.tip).play()
                    else:
                        data["tip"] = int(rating * random.randint(8, 12))
                        random.choice(self.tip).play()
            else:
                data["tip"] = 0
        elif action == "serve" and self.rect.collidepoint(mouse) and not data["table"] == self.table:
            data["order"] = self.order
            data["pos"] = self.rect.left, self.rect.top
            data["table"] = self.table
        elif action == "leave" and self.toleave:
            data["seats"][self.table - 1] = False
            self.kill()

