import pygame
import math
import random

WINDOW_SIZE = (600,600)
G = pow(6.67430,0)
WINDOW_CAPTION = 'Gravity Simulator'
WINDOW_COLOR = (19,19,19)

OBJECT_RADIUS_MULTIPLIER = pow(1,-24) 
OBJECT_MASS_MULTIPLIER = pow(1,24)
OBJECT_COLOR = (250,209,102)

CURSOR_COLOR = (20,60,80)

running = True
cursor_radius = 1

pygame.init()
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_CAPTION)

def draw_cursor(mouse_pos):
    pygame.draw.circle(window,CURSOR_COLOR,mouse_pos,cursor_radius)

def change_cursor_radius(events):
    global cursor_radius
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                cursor_radius += 1
            elif e.key == pygame.K_s:
                cursor_radius -= 1

def f_mag(o1,o2):
    return -(G*o1.mass*o2.mass)/(pow(o2.pos[0]-o1.pos[0],2)+pow(o2.pos[1]-o1.pos[1],2))

objects = []

class Object:
    def __init__(self,pos:tuple,mass:int):
        self.pos = pos #pos
        self.mass = mass*pow(OBJECT_MASS_MULTIPLIER,2) #in kg

    def add_force(self,force_vec):
        res = list(self.pos)
        res[0] += force_vec[0]
        res[1] += force_vec[1]
        self.pos = tuple(res)

    def draw(self):
        pygame.draw.circle(window,OBJECT_COLOR,self.pos,self.mass*OBJECT_RADIUS_MULTIPLIER)

def draw_objects():
    if objects:
        for o in objects:
            o.draw()

def add_forces():
    for i in range(len(objects)):
        for j in range(len(objects)):
            if i != j:
                f = f_mag(objects[i],objects[j])
                f_vec = ((objects[i].pos[0]-objects[j].pos[0])*f,(objects[i].pos[1]-objects[j].pos[1])*f)
                objects[i].add_force(f_vec)

def add_object(events,mouse_pos):
    for e in events:
        if e.type == pygame.MOUSEBUTTONDOWN:
            objects.append(Object(mouse_pos,cursor_radius))

def main():
    while running:
        events = pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        add_object(events,mouse_pos)
        add_forces()
        window.fill(WINDOW_COLOR)
        draw_cursor(mouse_pos)
        change_cursor_radius(events)
        draw_objects()
        pygame.display.flip() 
if __name__ == '__main__':
    main()
