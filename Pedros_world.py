from funciones import redondeo
import random
import math
#----------------------------------------------------------------------------------------------------------------------#

class Entorno:
    def __init__(self,totalX,totalY,dirt_rate):
        self.totalX = totalX
        self.totalY = totalY
        self.dirt_rate = dirt_rate
        self.peterX = random.randint(0,totalX-1)
        self.peterY = random.randint(0,totalY-1)
        self.world = [[0]*totalX for i in range(totalY)]
        self.acciones = 1000
        self.rendimiento = 0

    def suciedad(self):
        total_casillas = self.totalX * self.totalY
        cant_sucias = (self.dirt_rate * total_casillas)/100
        cant_sucias = redondeo(cant_sucias)
        while(cant_sucias > 0):
            new_x = random.randint(0,self.totalX-1)
            new_y = random.randint(0,self.totalY-1)
            if(self.world[new_x][new_y] != 1):
                self.world[new_x][new_y] = 1
                cant_sucias = cant_sucias - 1

    def clean(self):
        self.world[self.peterX][self.peterY] = 0
        self.rendimiento = self.rendimiento+ 1

    def mover(self, X, Y):
        if (X >= 0 and X < self.totalX) and (Y >= 0 and Y < self.totalY):
            self.peterX = X
            self.peterY = Y
            self.acciones = self.acciones - 1
            return True
        return False

    def is_dirty(self):
        if (self.world[self.peterX][self.peterY] == 1):
            return True
        return False


    def perfomance(self):
        total_casillas = self.totalX * self.totalY
        cant_sucias = (self.dirt_rate * total_casillas) / 100
        cant_sucias = redondeo(cant_sucias)
        limpio = self.rendimiento * 100 / cant_sucias
        print(" Peter limpio aproximadamente un", round(limpio, 2), "%")
