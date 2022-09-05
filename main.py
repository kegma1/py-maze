import random
from random import Random
import pygame
import sys
from pygame import image
from pygame.locals import *
from pygame.time import *
from cell import Cell
import pygame.time
import pygame.image


# size = int(input("window size: "))+1
w = int(input("maze size: "))
# screenSize = width, height = size, size
screenSize = width, height = 400, 400
cols = width // w
rows = height // w

grid = []

for j in range(rows):
    grid.append([])
    for i in range(cols):
        cell = Cell(i, j)
        grid[j].append(cell)
startPoint = start_x, start_y = 0, 0
endPoint = end_x, end_y = len(grid)-1, len(grid[0])-1


def removeWalls(a, b):
    x = a.i - b.i
    y = a.j - b.j
    if x == 1:
        a.sides[3] = False
        b.sides[1] = False
    elif x == -1:
        a.sides[1] = False
        b.sides[3] = False

    if y == 1:
        a.sides[0] = False
        b.sides[2] = False
    elif y == -1:
        a.sides[2] = False
        b.sides[0] = False


def convert_to_lines(grid, w):
    lines = []

    for cell in grid:
        lines.append(((cell.i*w)+w/2, (cell.j*w)+w/2))
    return lines


def make_file_name():
    counter = 0
    found = False
    while not found:
        try:
            pygame.image.load("maze{}.png".format(counter))
        except:
            found = True
            return "maze{}.png".format(counter)
        finally:
            counter += 1


def main():
    pygame.init()
    # setup
    screen = pygame.display.set_mode(screenSize)

    current = grid[start_x][start_y]
    stack = []
    path = []
    done = False
    solved = False
    r = 0
    next = 0

    # main loop
    while True:
        # check if closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not done:
            # maze making algorithm
            current.visited = True
            neighbors = current.getNeighbors(grid)
            if neighbors:
                r = random.randrange(0, len(neighbors))
                next = neighbors[r]
            else:
                next = None
            if next:
                next.visited = True
                stack.append(current)
                removeWalls(current, next)
                current = next

                if current.j == endPoint[0] and current.i == endPoint[1]:
                    path = convert_to_lines(stack.copy(), w)
                    path.append(((endPoint[1]*w)+w/2, (endPoint[0]*w)+w/2))
                    solved = True

            elif len(stack) > 0:
                current = stack.pop()
            else:
                done = True
                print(pygame.time.get_ticks()/1000)
                pygame.image.save(screen, make_file_name())

        # clear screen
        screen.fill((51, 51, 51))

        # draw path
        # if solved:
        #     pygame.draw.lines(screen, (0, 255, 0), False, path, 1)

        # draw maze
        current.highlight(screen, w, (0, 255, 0, 125))
        grid[end_x][end_y].highlight(screen, w, (0, 135, 255, 250))
        grid[start_x][start_y].highlight(screen, w, (255, 0, 0, 250))
        for i in range(len(grid)):
            for cell in grid[i]:
                cell.show(screen, w, (255, 255, 255, 255))

        # refresh screen
        pygame.display.update()


main()
