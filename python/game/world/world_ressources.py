import routines
import pygame

tree_ressources = {}
parallax_ressources = {}

def init_tree_ressources():
    if tree_ressources == {}:
        tree_ressources['tree1'] = routines.load_png('world/trees/tree1.png')

def init_parallax_ressources(width,height):
    if parallax_ressources == {}:
        parallax_ressources['back'] = pygame.transform.scale(routines.load_png('world/trees/far-background.png')[0],(width,height))
        parallax_ressources['front'] = pygame.transform.scale(routines.load_png('world/trees/near-background.png')[0],(width,height))
