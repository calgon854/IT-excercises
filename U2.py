class Vector3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __len__(self):
        return 3
    
    def len(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def __abs__(self):
        return Vector3(abs(self.x),abs(self.y),abs(self.z))
    
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x*other, self.y*other,self.z*other)
        else:
            return Vector3(self.x*other.x, self.y*other.y,self.z*other.z)
        
    def __rmul__(self, other):
        return Vector3(self.x*other, self.y*other,self.z*other)

    def cross(self, other):
        return Vector3((self.y*other.z)-(self.z*other.y),(self.z*other.x)-(self.x*other.z),(self.x*other.y)-(self.y*other.x))
       
    def dot(self, other):
        return (self.x*other.x)+(self.y*other.y)+(self.z*other.z)
       
    def normalize(self):
        
        l = ((self.x**2)+(self.y**2)+(self.z**2))**0.5

        return Vector3(self.x/l, self.y/l, self.z/l)

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x+other, self.y+other,self.z+other)
        else:
            return Vector3(self.x+other.x, self.y+other.y,self.z+other.z)
        
    def __radd__(self, other):
        return Vector3(self.x+other, self.y+other,self.z+other)

            
    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x-other, self.y-other,self.z-other)
        else:
            return Vector3(self.x-other.x, self.y-other.y,self.z-other.z)
        
    def __rsub__(self, other):
        return Vector3(self.x-other, self.y-other,self.z-other)

    
# --------------------

v1 = Vector3(6,3,6)
v2 = Vector3(4,7,8)



v5 = Vector3(3,4, 8)
v6 = v5 + 1
v7 = 1 - v5   # mit - und + gefixed 

v3 = v1.normalize()


print(v3)


#print(v6)
#print(v7)  #geht nicht ohne fix radd -- magic!



#----------------
#v3 = v1 + v2
#v4 = v1 + v2 + v3
#v5 = v2 - v4

#s = len(v1)
#u = abs(v2)

#print(type(v2))
#print(u)

#print(v3)
#print(v4)
