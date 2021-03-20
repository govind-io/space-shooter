import pygame
import random
import math
import time
pygame.init()
#Global Variables
screen=pygame.display.set_mode((800,500))
icon=pygame.image.load("icon.png")
pygame.display.set_caption("Ashavik Space")
pygame.display.set_icon(icon)
background=pygame.image.load("background.png")
playerimg=pygame.image.load("ufo.png")
game_over_image=pygame.image.load("gameoverpic.png")
startingimg=pygame.image.load("starting.png")
blast=pygame.image.load("blast.png")
count=0
score=0
font=pygame.font.Font('freesansbold.ttf',32)
f=open("score_record.txt")

#player variables
playery=360
playerx=368
player_change=0

#bullet variables
bullet_num=5
bullet_change=-2
bulletimg=[]
bullet_state=[]
bullety=[]
bulletx=[]
bullet_image=pygame.image.load("bullet.png")

#enemy Variables
enemyimg=[]
enemyx=[]
enemyy=[]
enemy_image=pygame.image.load("enemy.png")
enemy_num=6
enemyy_change=[]

#setting number of bullets
for i in range(bullet_num):
    bulletimg.append(bullet_image)
    bullet_state.append("ready")
    bullety.append(360)
    bulletx.append(0)

#setting number of enemies
for digit in range(enemy_num):
    enemyimg.append(enemy_image)
    enemyx.append(random.randint(0,736))
    enemyy.append(random.randint(0,50))
    enemyy_change.append(0.05)

#sounds
fire=pygame.mixer.Sound("fire.wav")
boom=pygame.mixer.Sound("boom.wav")
#game_over=pygame.mixer.Sound("gameover.wav")
boom.set_volume(200)
#enemy spawn
def spawn_enemy(number):
    x=random.randint(0,736)
    y=random.randint(0,50)
    enemyx[number]=x
    enemyy[number]=y
#enemy movement
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

#player movement
def player(x,y):
    screen.blit(playerimg,(x,y))

#bullet movement
def bullet(x,y,n): 
    screen.blit(bulletimg[n],(x,y))
    global bullet_state
    bullet_state[n]="fire"

#check if score
def score_checker():
    for i in range(bullet_num):
        for n in range(enemy_num):
            distance=math.sqrt(math.pow((bulletx[i]-enemyx[n]),2)+math.pow((bullety[i]-enemyy[n]),2))
            if distance<50:
                global score
                score+=1
                boom.play()
                screen.blit(blast,(enemyx[n],enemyy[n]))
                pygame.display.update()
                time.sleep(0.05)
                spawn_enemy(n)
                bullety[i]=-20

#check if game over
def game_over():
    for i in range(enemy_num):
        if enemyy[i]>290:
            screen.blit(game_over_image,(0,0))
            score_value=font.render(str(score), True, (255,255,255))
            temp=f.read()
            if score>int(temp):
                f.write(score)
                temp=score    
            high_score=font.render("Highest Score is:"+str(temp), True, (255,255,255))
            screen.blit(high_score,(340,220))
            screen.blit(score_value,(340,205))
            pygame.display.update()
            return True
    else:
        return False
      
#game starting loop
starting=True
while starting:
    screen.fill((255,255,255))
    screen.blit(startingimg,(0,0))
    for events in pygame.event.get():
        if events.type==pygame.KEYDOWN and events.key==pygame.K_RETURN:
            starting=False

pygame.mixer.music.load("bgsound.mp3")
#main game loop
result=True
while result:
    pygame.mixer.music.play(-1)
    is_over=game_over()
    if is_over:
        pygame.mixer.music.stop()
        #game_over.play()
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                result=False
            elif events.type==pygame.KEYDOWN and events.key==pygame.K_RETURN:
                is_over=False
                #reseting global variables
                #Global Variables
                screen=pygame.display.set_mode((800,500))
                icon=pygame.image.load("icon.png")
                pygame.display.set_caption("Ashavik Space")
                pygame.display.set_icon(icon)
                background=pygame.image.load("background.png")
                playerimg=pygame.image.load("ufo.png")
                game_over_image=pygame.image.load("gameoverpic.png")
                startingimg=pygame.image.load("starting.png")
                blast=pygame.image.load("blast.png")
                count=0
                score=0
                font=pygame.font.Font('freesansbold.ttf',32)

                #player variables
                playery=360
                playerx=368
                player_change=0

                #bullet variables
                bullet_num=5
                bullet_change=-1
                bulletimg=[]
                bullet_state=[]
                bullety=[]
                bulletx=[]
                bullet_image=pygame.image.load("bullet.png")

                #enemy Variables
                enemyimg=[]
                enemyx=[]
                enemyy=[]
                enemy_image=pygame.image.load("enemy.png")
                enemy_num=4
                enemyy_change=[]

                #setting number of bullets
                for i in range(bullet_num):
                    bulletimg.append(bullet_image)
                    bullet_state.append("ready")
                    bullety.append(360)
                    bulletx.append(0)

                #setting number of enemies
                for digit in range(enemy_num):
                    enemyimg.append(enemy_image)
                    enemyx.append(random.randint(0,736))
                    enemyy.append(random.randint(0,50))
                    enemyy_change.append(1)

                #sounds
                fire=pygame.mixer.Sound("fire.wav")
                boom=pygame.mixer.Sound("boom.wav")
                #game_over=pygame.mixer.Sound("gameover.wav")
                boom.set_volume(200)
    else:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                result=False
            if events.type==pygame.KEYDOWN:
                if events.key==pygame.K_LEFT:
                    player_change=-1
                elif events.key==pygame.K_RIGHT:
                    player_change=1
                elif events.key==pygame.K_UP:
                    if count>4:
                        count=0
                    if bullet_state[count]=="ready":
                        temp=playerx+26
                        bulletx[count]=temp
                        bullet(bulletx[count],bullety[count],count)
                        fire.play()
                        count+=1
            elif events.type==pygame.KEYUP:
                if events.key==pygame.K_RIGHT or events.key==pygame.K_LEFT:
                    player_change=0
        screen.fill((255,0,0))
        screen.blit(background,(0,0))
        playerx+=player_change
        if playerx<0:
            playerx=0
        elif playerx>736:
            playerx=736
        for num in range(bullet_num):
            if bullet_state[num]=="fire":
                bullety[num]+=bullet_change
                bullet(bulletx[num],bullety[num],num)
            if bullety[num]<=0:
                bullet_state[num]="ready"
                bullety[num]=360
        for digits in range(enemy_num):
            enemy(enemyx[digits],enemyy[digits],digits)
            enemyy[digits]+=enemyy_change[digits]
        player(playerx,playery)
        score_checker()

        #Show Score
        score_value=font.render("Score :"+ str(score), True, (255,255,255))
        screen.blit(score_value,(10,10))  
        pygame.display.update()
    
        
