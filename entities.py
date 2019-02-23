import pygame, random

food = {"burger":[3, 1, 1, 0], "tacos":[3, 2, 0, 1], "fries":[2, 3, 1, 0], "cupcake":[0, 0, 0, 4], "sushi":[2, 3, 1, 1]}

class player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([50, 50])
        self.image.fill([122, 59, 1])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
    def draw(self, surface):
        surface.blit(self.image, [self.rect.left, self.rect.top])

class customer(pygame.sprite.Sprite):
    def __init__(self, pos, order):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([50, 50])
        self.image.fill([255, 175, 102])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
        self.order = str(order)
        self.table = ((self.rect.top - 37) / 120) + 1
        self.toleave = False
    def draw(self, surface):
        surface.blit(self.image, [self.rect.left, self.rect.top])
    def update(self, action, mouse, data):
        global food
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
            if data["food"]["recipe"] == food[data["food"]["name"]]:
                rating = 1
                data["comments"] = "Perfect!"
            else:
                if not food[data["food"]["name"]][0] == 0:
                    rating1 = float(data["food"]["recipe"][0] / food[data["food"]["name"]][0])
                    if rating1 > 1:
                        rating1 = 1 - (rating1 - 1)
                        data["comments"] = "too juicy"
                    elif rating1 < 1:
                        data["comments"] = "not juicy enough"
                else:
                    if data["food"]["recipe"][0] > 0:
                        rating1 = 1 - (float(data["food"]["recipe"][0])/4)
                        data["comments"] = "too juicy"
                    else:
                        rating1 = 1
                if not food[data["food"]["name"]][1] == 0:
                    rating2 = float(data["food"]["recipe"][1] / food[data["food"]["name"]][1])
                    if rating2 > 1:
                        rating2 = 1 - (rating2 - 1)
                        data["comments"] = "too zesty"
                    elif rating2 < 1:
                        data["comments"] = "not zesty enough"
                else:
                    if data["food"]["recipe"][1] > 0:
                        rating2 = 1 - (float(data["food"]["recipe"][1])/4)
                        data["comments"] = "too zesty"
                    else:
                        rating2 = 1
                if not food[data["food"]["name"]][2] == 0:
                    rating3 = float(data["food"]["recipe"][2] / food[data["food"]["name"]][2])
                    if rating3 > 1:
                        rating3 = 1 - (rating3 - 1)
                        data["comments"] = "too bitter"
                    elif rating3 < 1:
                        data["comments"] = "not bitter enough"
                else:
                    if data["food"]["recipe"][2] > 0:
                        rating3 = 1 - (float(data["food"]["recipe"][2])/4)
                        data["comments"] = "too bitter"
                    else:
                        rating3 = 1
                if not food[data["food"]["name"]][3] == 0:
                    rating4 = float(data["food"]["recipe"][3] / food[data["food"]["name"]][3])
                    if rating4 > 1:
                        rating4 = 1 - (rating4 - 1)
                        data["comments"] = "too sweet"
                    elif rating4 < 1:
                        data["comments"] = "not sweet enough"
                else:
                    if data["food"]["recipe"][3] > 0:
                        rating4 = 1 - (float(data["food"]["recipe"][3])/4)
                        data["comments"] = "too sweet"
                    else:
                        rating4 = 1
                print float(rating1 +  rating2 + rating3 + rating4) / 4
                rating = float(float(rating1 + rating2 + rating3 + rating4) / 4)
            data["rating"] = float(rating) * 10
            print "Final Score: " + str(rating * 100) + "%"
            print "Additional Comments: " + data["comments"]
            if rating > 0.8:
                data["tip"] = int(rating * random.randint(8, 12))
            else:
                data["tip"] = 0
        elif action == "serve" and self.rect.collidepoint(mouse) and not data["table"] == self.table:
            data["order"] = self.order
            data["pos"] = self.rect.left, self.rect.top
            data["table"] = self.table
        elif action == "leave" and self.toleave:
            data["seats"][self.table - 1] = False
            self.kill()

