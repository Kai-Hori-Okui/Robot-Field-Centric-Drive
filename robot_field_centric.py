import pygame
import numpy as np

def draw_robot(x, y, size, rotation):
    base_x = size * (np.cos(rotation) - np.sin(rotation))
    base_y = size * (np.cos(rotation) + np.sin(rotation))
    points = []

    points.append([x + base_x, y + base_y])
    points.append([x - base_y, y + base_x])
    points.append([x - base_x, y - base_y])
    points.append([x + base_y, y - base_x])
    
    pygame.draw.polygon(screen, (255, 0, 0), points) # draw a red square on the screen

width, height = 1500, 900  # desired window size
screen = pygame.display.set_mode((width, height))

x = width//2
y = height//2
rotation = 0
size = 30

field_centric = 0

axial, lateral, yaw = [0,0,0]

pygame.key.set_repeat()

running = True
while running:
    axial, lateral, yaw = [0,0,0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                field_centric = 1-field_centric
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        axial += -0.5
    if keys[pygame.K_s]:
        axial += 0.5

    if keys[pygame.K_a]:
        lateral += -0.5
    if keys[pygame.K_d]:
        lateral += 0.5

    if keys[pygame.K_LEFT]:
        yaw += -0.002
    if keys[pygame.K_RIGHT]:
        yaw += 0.002
    

    screen.fill((0, 0, 0))

    # field centric
    if field_centric == 1:
        correction = -rotation

        new_lateral = lateral*np.cos(correction) - axial*np.sin(correction)
        new_axial = axial*np.cos(correction) + lateral*np.sin(correction)

        lateral = new_lateral
        axial = new_axial

    x += lateral*np.cos(rotation) - (axial)*np.sin(rotation)
    y += (axial)*np.cos(rotation) + lateral*np.sin(rotation)
    rotation += yaw

    draw_robot(x, y, size, rotation)
    pygame.display.flip()

pygame.quit()
