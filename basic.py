# 'KCF': better for accuracy and speed. Probably best for person tracking mode
# 'MEDIANFLOW': best for slow motion. Use with vehicles, slow objects
# if either reports failure, reacquire object

import cv2
import pygame
import numpy


def get_output(camera):
    frame = camera.read()[1]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = numpy.rot90(frame)
    return(frame)


def convert_box(box):
    return((box[1], box[0], box[3], box[2]))


# initialize trackers
fast_tracker = cv2.TrackerKCF_create()
slow_tracker = cv2.TrackerMedianFlow_create()

camera = cv2.VideoCapture(0)

box = (175, 250, 100, 100)

pygame.init()
screen = pygame.display.set_mode([600, 450])

selected = False
while(not selected):
    frame = pygame.surfarray.make_surface(get_output(camera))
    screen.blit(frame, (0, 0))

    pgbox = (box[1], box[0], box[3], box[2])
    pygame.draw.rect(screen, (255, 0, 0), pgbox, 1)
    pygame.display.update()

    if(pygame.key.get_pressed()[pygame.K_SPACE]):
        selected = True

    pygame.event.pump()

fast_tracker.init(get_output(camera), box)
slow_tracker.init(get_output(camera), box)

while(True):

    frame = get_output(camera)

    screen.fill([0, 0, 0])

    fast_box = fast_tracker.update(frame)[1]
    slow_box = slow_tracker.update(frame)[1]

    # display screen
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0, 0))

    pygame.draw.rect(screen, (255, 0, 0), convert_box(fast_box), 1)
    pygame.draw.rect(screen, (0, 255, 0), convert_box(slow_box), 1)

    pygame.display.update()
