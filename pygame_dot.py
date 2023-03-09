import pygame

# init
pygame.init()
isRun = True

window = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

#posisi
x = 250
y = 250

#ukuran
panjang = 20
lebar = 20

#kecepatan
speed = 10

while isRun:
# user input
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - lebar:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - lebar:
        y += speed

#update
    window.fill((255,255,255))
    pygame.draw.rect(window, (255,0,0), (x,y,lebar,panjang))

# render
    pygame.display.update()

pygame.quit()