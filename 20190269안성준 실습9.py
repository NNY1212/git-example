class Vector2D:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __add__(self,other):
    return Vector2D(self.x + other.x, self.y + other.y)
  def __sub__(self,other):
    return Vector2D(self.x - other.x, self.y - other.y)
  def __mul__(self,other):
    return Vector2D(self.x * other.x, self.y * other.y)
  def __truediv__ (self,other):
    return Vector2D(self.x / other.x, self.y / other.y)
  def __str__(self):
    return "({0},{1})".format(self.x,self.y)
  def __neg__ (self):
    return Vector2D(-self.x,-self.y)
  def __eq__(self,other):
    if isinstance(other, Vector2D):
        return self.x == other.x and self.y == other.y
    return NotImplemented

v1 = Vector2D(10,20)
v2 = Vector2D(2,5)
x1 = 10
print("{} + {} = {}".format(v1,v2,v1 + v2))
print("{} - {} = {}".format(v1,v2,v1 - v2))
print("{} * {} = {}".format(v1,v2,v1 * v2))
print("{} / {} = {}".format(v1,v2,v1 / v2))
print("-{} = {}".format(v1,-v1))
print("{} = {} = {}".format(v1,v2, v1 == v2))
print("{} = {} = {}".format(v1,v1, v1 == v1))
print("{} = {} = {}".format(v1,x1, v1 == x1))
print("20190269 안성준")
