# 'KCF': better for accuracy and speed. Probably best for person tracking mode
# 'MEDIANFLOW': best for slow motion. Use with vehicles, slow objects
# if either reports failure, reacquire object

import cv2
import pygame

# initialize trackers
fast_tracker = cv2.TrackerKCF_create()
slow_tracker = cv2.TrackerMedianFlow_create()

camera = cv2.VideoCapture(0)

pygame.init()
screen = pygame.display.set_mode(960, 540)

while(True):

    frame = camera.read()[1]

    screen.fill([0, 0, 0])
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0, 0))
    pygame.display.update()
