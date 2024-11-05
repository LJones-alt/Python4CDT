import numpy as np

class MatrixCluster:
    def __new__(cls, particle_array, lx , ly, lz):
        print('Creating new cluster object')
        cluster = super().__new__(cls)
        return cluster

    def __init__(self, particle_array, lx, ly, lz):
        self.ljp =0
        self.lx =lx
        self.ly = ly
        self.lz = lz
        self.distance3d = 0
        self.particle_array = particle_array
        self.particles , self.dims = self.particle_array.shape
        self.distances = []

    def find_ljp(self, x):
        self.x = x
        self.ljp = 4*(pow(self.x, (-12)) - pow(self.x, (-6)))
        print(f"The LJP of {x} is {self.ljp}")
        return self.ljp
    
    def dist3d(self, p1, p2):
        distance = pow((pow(p2[0]-p1[0], 2)+pow(p2[1]-p1[1], 2) + pow(p2[2]-p1[2],2)), 0.5)
        print('3D distance is :', distance)
        return distance
    
    def get_relative_distance(self):
        distances = np.zeros((int(self.particles), int(self.particles)))
        for b in range(self.particles):
            for a in range(self.particles):
                distances[b,a]= self.dist3d(self.particle_array[b], self.particle_array[a])
        print(distances)
        return distances
    
    def get_com(self):
        com =[]
        for b in range(self.dims):
            _com=0
            for a in range(self.particles):
                _com = _com + self.particle_array[a,b]
            com.append((_com/self.particles))
        print(f"COM : {com}")
        return com


    def get_delta(self, k1, k2, l):
        if (k1-k2) < (-0.5*l):
            return (k1-k2 +l)
        elif (-0.5*l) <= (k1-k2) <= (0.5*l):
            return (k1-k2)
        elif (k1-k2) > (0.5*l):
            return (k1-k2-l)
        else :
            return 0

    def get_particle_distance(self, x1, x2, y1, y2, z1, z2):
        particle_distance = pow(self.get_delta(x1, x2, self.lx), 2) + pow(self.get_delta(y1, y2, self.ly), 2) + pow(self.get_delta(z1, z2, self.lz),2)
        print(f"The particle distance is {particle_distance}")
        return particle_distance