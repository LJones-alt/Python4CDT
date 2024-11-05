class Cluster:
    def __new__(cls, x1, x2, y1, y2, z1, z2, lx, ly, lz):
        print('Creating new cluster object')
        cluster = super().__new__(cls)
        return cluster

    def __init__(self, x1, x2, y1, y2, z1, z2, lx, ly ,lz):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.lx = lx
        self.ly = ly
        self.lz = lz 
        self.ljp =0
        self.distance3d = 0

    def find_ljp(self, x):
        self.x = x
        self.ljp = 4*(pow(self.x, (-12)) - pow(self.x, (-6)))
        print(f"The LJP of {x} is {self.ljp}")
        return self.ljp
    
    def dist3d(self):
        distance = pow((pow(self.x2-self.x1, 2)+pow(self.y2-self.y1, 2) + pow(self.z2-self.z1,2)), 0.5)
        print('3D distance is :', distance)
        return distance
    
    def get_delta(self, k1, k2, l):
        if (k1-k2) < (-0.5*l):
            return (k1-k2 +l)
        elif (-0.5*l) <= (k1-k2) <= (0.5*l):
            return (k1-k2)
        elif (k1-k2) > (0.5*l):
            return (k1-k2-l)
        else :
            return 0

    def get_particle_distance(self):
        particle_distance = pow(self.get_delta(self.x1, self.x2, self.lx), 2) + pow(self.get_delta(self.y1, self.y2, self.ly), 2) + pow(self.get_delta(self.z1, self.z2, self.lz),2)
        print(f"The particle distance is {particle_distance}")
        return particle_distance