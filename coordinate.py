class Coordinate:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y
    def translate(self, X_trans, Y_trans):
        self.x += X_trans
        self.y += Y_trans
    def __str__(self):
        return f"Coor<{self.x}, {self.y}>"
    def __add__(self, other):
        return Coordinate(self.x+other.x, self.y+other.y)


coor_1 = Coordinate(5,8)
coor_2 = Coordinate(3,6)

# print(f"Coor<{coor_1.x}, {coor_1.y}>")
print(coor_1)

# coor_1.translate(4,-5)
# print(f"Coor<{coor_1.x}, {coor_1.y}>")
print(coor_2)

coor_3 = coor_1 + coor_2
print(coor_3)
print(type(coor_3))
print(type(coor_1))