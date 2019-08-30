import random
class Rt3pe:
    def __init__(self, entorno):
        self.entorno = entorno
        self.posicionX = entorno.peterX
        self.posicionY = entorno.peterY
        self.totalX = entorno.totalX
        self.totalY = entorno.totalY
        self.sucio = False;

    def up(self):
        self.entorno.mover(self.entorno.peterX - 1, self.entorno.peterY)
    def down(self):
        self.entorno.mover(self.entorno.peterX + 1, self.entorno.peterY)
    def left(self):
        self.entorno.mover(self.entorno.peterX, self.entorno.peterY - 1)
    def right(self):
        self.entorno.mover(self.entorno.peterX, self.entorno.peterY + 1)
    def stand(self):
        self.entorno.mover(self.entorno.peterX, self.entorno.peterY)
    def suck(self):
        self.entorno.clean()

    def perspective(self):
        self.posicionX = self.entorno.peterX
        self.posicionY = self.entorno.peterY
        self.sucio = self.entorno.is_dirty()

    def think(self):
        self.perspective()
        if (self.sucio):
            self.suck()
        while (self.entorno.acciones > 0):
            accion = random.randint(1,5)
            if accion == 1:
                self.up()
                self.perspective()
                if (self.sucio):
                    self.suck()
            if accion == 2:
                self.down()
                self.perspective()
                if (self.sucio):
                    self.suck()
            if accion == 3:
                self.right()
                self.perspective()
                if (self.sucio):
                    self.suck()
            if accion == 4:
                self.left()
                self.perspective()
                if (self.sucio):
                    self.suck()
            if accion == 5:
                self.stand()
