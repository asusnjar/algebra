from math import pi
from turtle import circle
class Krug:
    def __init__(self, radius):
        self.r = radius
        return
    def povrsina(self):
        return self.r ** 2 * pi
    def opseg(self):
        return 2 * self.r * pi
    def crtaj(self):
        circle(self.r)

k1 = Krug(50)
k2 = Krug(100)
print(k1.r)
print(k2.povrsina())
k1.crtaj()
