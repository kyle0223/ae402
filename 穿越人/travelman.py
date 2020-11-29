import pygame
import random
  
# 根據count決定採用的圖像
def move(image1, image2):
    global count
    if count < 5:
        image = image1
    elif count >= 5:
        image = image2

    if count >= 10:
        count = 0
    else:
        count += 1
    return image

WHITE    = ( 255, 255, 255)

pygame.init()

size = (400, 300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("穿越時空")

done = False

clock = pygame.time.Clock()

# 影像素材
standing = pygame.image.load("standing.png")
down1 = pygame.image.load("down1.png")
down2 = pygame.image.load("down2.png")
up1 = pygame.image.load("up1.png")
up2 = pygame.image.load("up2.png")
left1 = pygame.image.load("side1.png")
left2 = pygame.image.load("side2.png")
right1 = pygame.image.load('side1.png')
right2 = pygame.image.load('side2.png')
right1 = pygame.transform.flip(right1, True, False)
right2 = pygame.transform.flip(right2, True, False)
teleport1 = pygame.image.load("teleport1.png")
teleport2 = pygame.image.load("teleport2.png")
teleport3 = pygame.image.load("teleport3.png")
# 聲音素材
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

teleportSound = pygame.mixer.Sound("teleport.wav")

# -------- 主要的程式迴圈 -----------
x = 0
y = 0
locked = False # 穿越模式
while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): # 從事件list中抓取事件
        if event.type == pygame.QUIT: # 當使用者按下結束
            done = True # 將done變數設為True-->while迴圈將會結束

    keys = pygame.key.get_pressed()

    if not locked: #不在穿越模式
        if keys[pygame.K_LEFT]:
            image = move(left1, left2)
            x -= 1                
        elif keys[pygame.K_RIGHT]:
            image = move(right1, right2)            
            x += 1
        elif keys[pygame.K_UP]:
            image = move(up1, up2)            
            y -= 1
        elif keys[pygame.K_DOWN]:
            image = move(down1, down2)            
            y += 1
        elif keys[pygame.K_SPACE]:
            locked = True
        else:
            image = standing
            count = 0
    else: # 穿越模式
        if count == 0:
            teleportSound.play()
        if count < 5:
            image = teleport1
        elif count < 10:
            image = teleport2
        elif count < 15:
            image = teleport3
        else:
            x = random.randrange(0, size[0])
            y = random.randrange(0, size[1])
            count = 0
            locked = False
        count += 1

    screen.fill(WHITE)
    screen.blit(image, (x, y))
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

