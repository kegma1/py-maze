import random
import pygame
from pygame.locals import *
from pygame.surface import Surface


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j

        self.sides = [True, True, True, True]
        self.visited = False

    def show(self, screen, w, color):
        x = self.i*w
        y = self.j*w

        # top
        if self.sides[0]:
            pygame.draw.line(screen, color, (x, y), (x+w, y))
        # right
        if self.sides[1]:
            pygame.draw.line(screen, color, (x+w, y), (x+w, y+w))
        # bottom
        if self.sides[2]:
            pygame.draw.line(screen, color, (x+w, y+w), (x, y+w))
        # left
        if self.sides[3]:
            pygame.draw.line(screen, color, (x, y+w), (x, y))
   
    def getNeighbors(self, grid):
        neighbors = []

        top = right = bottom = left = grid[self.j][self.i]

        jPos = self.j+1
        jNeg = self.j-1
        iPos = self.i+1
        iNeg = self.i-1

        if not jNeg < 0: top = grid[jNeg][self.i]
        if  not iPos >= len(grid[0]): right = grid[self.j][iPos]
        if  not jPos >= len(grid): bottom = grid[jPos][self.i]
        if not iNeg < 0: left = grid[self.j][iNeg]

        if not top.visited:
            neighbors.append(top)
        if not right.visited:
            neighbors.append(right)
        if not bottom.visited:
            neighbors.append(bottom)
        if not left.visited:
            neighbors.append(left)
        if len(neighbors) > 0:
            return neighbors
        else:
            return None

    def highlight (self, screen, w, color):
        x = self.i*w
        y = self.j*w
        
        visitedSurface = pygame.Surface((w,w), pygame.SRCALPHA)
        visitedSurface.fill(color)
        screen.blit(visitedSurface, (x, y))
            


