import pygame
pygame.init()

win = pygame.display.set_mode((1200,675))

pygame.display.set_caption("2d platformer")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('boxing_ring.png')
char = pygame.image.load('standing.png')

bulletSound = pygame.mixer.Sound('lazer.wav')


music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
score = 0






class player(object):
    def __init__(self, x,y ,width, height):
        self.x = 900
        self.y = 425
        self.width = 64
        self.height = 64
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.health = 20
        self.hitbox = (self.x + 17, self.y + 11, 29,52)
        self.cooldown = 0

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1           
            elif self.right:
                 
                  win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                  self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29,52)
        pygame.draw.rect(win, (225,0,0), (self.hitbox[0] - 35, self.hitbox[1] - 20,100,10))
        pygame.draw.rect(win, (0,225,0), (self.hitbox[0] - 35, self.hitbox[1] - 20,50 -((50/10)* (10 - self.health)),10))
        #pygame.draw.rect(win, (225,0,0), self.hitbox,2)
                    
            
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
       self.x = x
       self.y = y
       self.radius = radius
       self.color = color
       self.facing = facing
       self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win,self.color, (self.x,self.y), self.radius)




class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width= width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 5
        self.path = [self.x, self.end]
        self.hitbox = (self.x + 17, self.y + 2, 31,57)
        self.health = 20
        self.visible = True
    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (225,0,0), (self.hitbox[0] - 35, self.hitbox[1] - 20,100,10))
            pygame.draw.rect(win, (0,225,0), (self.hitbox[0] - 35, self.hitbox[1] - 20,50 -((50/10)* (10 - self.health)),10))
            self.hitbox = (self.x + 17, self.y + 2, 31,57)
            #pygame.draw.rect(win, (225,0,0), self.hitbox,2)
    def hit(self):
        if self.health > 0:
           self.health -= 1
        else:
            self.visible = False
           
            
        print('hit')
        
        
        
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        
print( str(35/6))   
time = 60
cooldown = 0
def redrawGameWindow():
    
    
    
    
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score),1,(225,0,0))
    win.blit(text,(950, 10))
    man.draw(win)
    if true1 == False and true2 == True:
        goblin2.draw(win)
    if true == True: 
       goblin.draw(win)
    if true3 == True:
        goblin3.draw(win)
    if true4 == True:
        goblin4.draw(win)
    if true5 == True:
        goblin5.draw(win)
    if true6 == True:
        goblin6.draw(win)
    if true7 == True:
        goblin7.draw(win)
    if true8 == True:
        goblin8.draw(win)
    if true9 == True:
        goblin9.draw(win)
    if true10 == True:
        goblin10.draw(win)
    #pygame.draw.rect(win,(0,225,0),(100,10, 100,10))
    #pygame.draw.rect(win,(225,0,0),(100,10, 100,10))
    for bullet in bullets:
        bullet.draw(win)
    
        
    pygame.display.update()


    
#main loop
font = pygame.font.SysFont('calibri', 30, True)
goblin = enemy(1200/4,425, 64,64, 1200/4 + 1200/4 + 1200/4)
goblin2 = enemy(1200/4,425, 64,64, 1200/4 + 1200/4 + 1200/4)
goblin3 = enemy(1200/4,425, 64,64, 1200/4 + 1200/4 + 1200/4)
goblin4 = enemy(1200/4,425, 64,64, 1200/4 + 1200/4 + 1200/4)
goblin5 = enemy(1200/4,425, 64,64, 1200/4 + 1200/4 + 1200/4)
goblin6 = enemy(1200/4,425, 64,64, 1200/4 + 1200/4 + 1200/4)
goblin7 = enemy(1200/4,425, 64,64, 1200/4 + 1200/4 + 1200/4)
goblin8 = enemy(1200/4,425, 64,64, 1200/4 + 1200/4 + 1200/4)
goblin9 = enemy(1200/4,425, 64,64, 1200/4 + 1200/4 + 1200/4)
goblin10 = enemy(1200/4,425, 64,64, 1200/4 + 1200/4 + 1200/4)
shoot = 0
true1 = True
true2 = False
true3 = False
true4 = False
true5 = False
true6 = False
true7 = False
true8 = False
true9 = False
true10 = False
true = True
lol = True



man = player(900, 425, 64,64)
bullets = []
run = True
while run:
    pygame.draw.rect(win,(0,225,255),(900,10, 20,10))
    if true1 == True:
        
        if goblin.visible == False and score < 1:
           del goblin
           true1 = False
           true = False
           true2 = True
           score += 1
    if true2 == True:
        if goblin2.visible == False and score < 2:
              del goblin2
              true2 = False 
              score += 1
              true3 = True
    if true3 == True:                                
                                 

         if goblin3.visible == False and score < 3:
            del goblin3
            true3 = False
            score += 1
            true4 = True
    if true4 == True:
        if goblin4.visible == False and score < 4:
            del goblin4
            true4 = False
            score += 1
            true5 = True
    if true5 == True:
        if goblin5.visible == False and score < 5:
            del goblin5
            true5 = False
            score += 1
            true6 = True
    if true6 == True:
        if goblin6.visible == False and score < 6:
            del goblin6
            true6 = False
            score += 1
            true7 = True
    if true7 == True:
        if goblin7.visible == False and score < 7:
            del goblin7
            true7 = False
            score += 1
            true8 = True
    if true8 == True:
        if goblin8.visible == False and score < 8:
            del goblin8
            true8 = False
            score += 1
            true9 = True
    if true9 == True:
        if goblin9.visible == False and score < 9:
            del goblin9
            true9 = False
            score += 1
            true10 = True
    if true10 == True:
        if goblin10.visible == False and score < 10:
            del goblin10
            true10 = False
            score += 1
         
            
      
    clock.tick(80)
    if shoot > 0:
        shoot += 1
    if shoot > 3:
        shoot = 0
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   
            pygame.quit()

    for bullet in bullets:
        if true1 == True:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    
                    bullets.pop(bullets.index(bullet))
        if true2 == True:
            
            if bullet.y - bullet.radius < goblin2.hitbox[1] + goblin2.hitbox[3] and bullet.y + bullet.radius > goblin2.hitbox[1]:
                if bullet.x + bullet.radius > goblin2.hitbox[0] and bullet.x - bullet.radius < goblin2.hitbox[0] + goblin2.hitbox[2]:
                     goblin2.hit()
                     
                     bullets.pop(bullets.index(bullet))



        if true3 == True:
             if bullet.y - bullet.radius < goblin3.hitbox[1] + goblin3.hitbox[3] and bullet.y + bullet.radius > goblin3.hitbox[1]:
                  if bullet.x + bullet.radius > goblin3.hitbox[0] and bullet.x - bullet.radius < goblin3.hitbox[0] + goblin3.hitbox[2]:
                      goblin3.hit()
                      bullets.pop(bullets.index(bullet))
                                


            
            
               

        if true4 == True:
            
            if bullet.y - bullet.radius < goblin4.hitbox[1] + goblin4.hitbox[3] and bullet.y + bullet.radius > goblin4.hitbox[1]:
                 if bullet.x + bullet.radius > goblin4.hitbox[0] and bullet.x - bullet.radius < goblin4.hitbox[0] + goblin4.hitbox[2]:
                     goblin4.hit()
                     
                     bullets.pop(bullets.index(bullet))
            
        if bullet.x < 1200 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shoot == 0:
        
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 3:
            bulletSound.play()
            bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6, (255,215,0),facing))
        shoot = 1
    if keys[pygame.K_LEFT] and man.x > man.vel:
      man.x -= man.vel
      man.left= True
      man.right = False
      man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 1200 - man.width - man.vel:
      man.x += man.vel
      man.right = True
      man.left = False
      man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
                    
    if not(man.isJump):  
        if keys[pygame.K_UP] and man.cooldown <1 :
                
                man.cooldown += 1
                
                
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.6 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    if cooldown == 1 and man.isJump == False:
        
        if clock2.tick() == clock2.tick(30):
            cooldown = 0
        
        #for cooldown in range(0, 10000):
         #   if cooldown == 10000:
               # cooldown = 0
    print(str(man.cooldown))
    
    
    
    
    redrawGameWindow()
    
