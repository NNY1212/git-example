import math
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
  def distance(self,other):
    return math.sqrt((self.x - other.x) **2 + (self.y - other.y) ** 2)
  
class Line2D:
    def __init__(self,p1,p2):
      if isinstance(p1,Vector2D) and (p2,Vector2D):
        self.p1 = p1
        self.p2 = p2
    def length(self):
        return self.p1.distance(self.p2)
    def __len__(self):
        return int(self.length())
    def __eq__(self, other):
      if isinstance(other, Line2D):
        return self.length() == other.length()
    def __lt__(self,other):
      if isinstance(other, self):
        return self.length() < other.length()
    def __le__(self,other):
      if isinstance(other, self):
        return self.length() <= other.length()
    def __gt__(self,other):
      if isinstance(other, self):
        return self.length() > other.length()
    def __ge__(self,other):
      if isinstance(other, self):
        return self.length() >= other.length()
    def __str__(self):
        return "({}, {}) - ({}, {})".format(self.p1.x,self.p1.y,self.p2.x,self.p2.y)

      
      
      
    

v1 = Vector2D(10,20)
v2 = Vector2D(2,5)
v3 = Vector2D(5,10)
v4 = Vector2D(5,20)
x1 = 10

l1 = Line2D(v1,v2)
l2 = Line2D(v3,v4)



print("{} + {} = {}".format(v1,v2,v1 + v2))
print("{} - {} = {}".format(v1,v2,v1 - v2))
print("{} * {} = {}".format(v1,v2,v1 * v2))
print("{} / {} = {}".format(v1,v2,v1 / v2))
print("-{} = {}".format(v1,-v1))
print("{} = {} = {}".format(v1,v2, v1 == v2))
print("{} = {} = {}".format(v1,v1, v1 == v1))
print("{} = {} = {}".format(v1,x1, v1 == x1))
print("line1: ",l1)
print("line2: ",l2)
print("line1의 길이: ",len(l1))
print("line2의 길이: ",len(l2))
print("line1 == line2 =",l1 == l2)
print("line1 == line1 =",l1 == l1)
print("line1 < line2 =",l1 < l2)
print("line1 > line2 =",l1 > l2)




print("20190269 안성준")
