#---------------------------------------------------------------------------------------------------------------------#

class P3ter:
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
        tamX =self.entorno.totalX
        tamY =self.entorno.totalY

        while self.posicionX > 0:
            self.perspective()
            if (self.sucio):
                self.suck()
            self.up()

        while self.posicionY > 0:
            self.perspective()
            if (self.sucio):
                self.suck()
            self.left()

        while (self.entorno.acciones > 0):
            if self.posicionX == tamX-1 and self.posicionY == 0:
                break
            while self.posicionY < (tamY-1):
                self.right()
                self.perspective()
                if (self.sucio):
                    self.suck()
            if self.posicionY == (tamY-1):
                self.down()
                self.perspective()
                if (self.sucio):
                    self.suck()
            while self.posicionY > (0):
                self.left()
                self.perspective()
                if (self.sucio):
                    self.suck()
            if self.posicionY == 0:
                self.down()
                self.perspective()
                if (self.sucio):
                    self.suck()
