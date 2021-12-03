import random
import numpy as np
import math


class Flood:
    def __init__(self, gridsize):
        self.data = np.zeros((gridsize, gridsize))
        self.colors_dict = {}
        self.initialized = False
        self.ended = False
        self.step = gridsize//2

    def set_seeds(self, number_of_seeds = 5):
        self.colors_dict[0] = (np.inf, np.inf)
        for i in range(1, number_of_seeds+1):
            x = random.choice(range(0, self.data.shape[0]))
            y = random.choice(range(0, self.data.shape[1]))
            self.data[x][y] = i
            self.colors_dict[i] = (x, y)
        self.initialized = True
        

    def common_flood_iteration(self):
        width = self.data.shape[0]
        height = self.data.shape[1]
        prev_data = self.data.copy()

        for x in range(width):
            for y in range(height):
                if self.data[x][y] > 0:
                    continue
                esquerda = x - 1
                direita = x + 1
                cima = y - 1
                baixo = y + 1
                horizontal = [esquerda, x, direita]
                vertical = [cima, y, baixo]
                for i in horizontal:
                    for j in vertical:
                        #Checamos se pelo menos um dos índices atuais está fora da imagem ou é a própria célula
                        if i >= 0 and i < width and j >= 0 and j < height:
                            neighboor_color = int(prev_data[i][j])
                            if neighboor_color > 0:
                                self.data[x][y] = self.data[i][j]
                                
                                    
        return self.data

    def jump_flood_iteration(self):
        width = self.data.shape[0]
        height = self.data.shape[1]
        changed = False
        distances = {}

        print(f"Step: {self.step}")
        for x in range(width):
            for y in range(height):
                esquerda = x - self.step
                direita = x + self.step
                cima = y - self.step
                baixo = y + self.step
                horizontal = [esquerda, x, direita]
                vertical = [cima, y, baixo]
                for i in horizontal:
                    for j in vertical:
                        #Checamos se pelo menos um dos índices atuais está fora da imagem ou é a própria célula
                        if i >= 0 and i < width and j >= 0 and j < height:
                            neighboor_color = int(self.data[i][j])
                            current_color = int(self.data[x][y])
                            neighboor_seed_pos = self.colors_dict[neighboor_color]
                            current_seed_pos = self.colors_dict[current_color]
                            if neighboor_color > 0:
                                if current_color == 0:
                                    self.data[x][y] = self.data[i][j]
                                    changed = True
                                else:
                                    current_seed_distance = None
                                    if not (x,y) in distances:
                                        current_seed_distance = (current_seed_pos[0]-x)**2 + (current_seed_pos[1]-y)**2
                                    else:
                                        current_seed_distance = distances[(x,y)]

                                    neighboor_seed_distance = (neighboor_seed_pos[0]-x)**2 + (neighboor_seed_pos[1]-y)**2
                                    if neighboor_seed_distance < current_seed_distance:
                                        distances[(x,y)] = neighboor_seed_distance
                                        self.data[x][y] = self.data[i][j]
                                        changed = True

        self.step = self.step //2
        if self.step < 1:
            self.step = 1
        if not changed:
            self.ended = True
        

    def common_flood_with_distance_iteration(self):
        width = self.data.shape[0]
        height = self.data.shape[1]
        prev_data = self.data.copy()

        for x in range(width):
            for y in range(height):
                if self.data[x][y] > 0:
                    continue
                esquerda = x - 1
                direita = x + 1
                cima = y - 1
                baixo = y + 1
                horizontal = [esquerda, x, direita]
                vertical = [cima, y, baixo]
                for i in horizontal:
                    for j in vertical:
                        #Checamos se pelo menos um dos índices atuais está fora da imagem ou é a própria célula
                        if i >= 0 and i < width and j >= 0 and j < height:
                            neighboor_color = int(prev_data[i][j])
                            current_color = int(prev_data[x][y])
                            neighboor_seed_pos = self.colors_dict[neighboor_color]
                            current_seed_pos = self.colors_dict[current_color]
                            if neighboor_color > 0:
                                if current_color == 0:
                                    self.data[x][y] = self.data[i][j]
                                else:
                                    current_seed_distance = np.sqrt((current_seed_pos[0]-x)**2 + (current_seed_pos[1]-y)**2)
                                    neighboor_seed_distance = np.sqrt((neighboor_seed_pos[0]-x)**2 + (neighboor_seed_pos[1]-y)**2)
                                    if neighboor_seed_distance < current_seed_distance:
                                        self.data[x][y] = self.data[i][j]

        return self.data