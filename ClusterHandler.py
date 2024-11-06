import numpy as np 
import random as rand

class ClusterHandler:
    def __new__(ch, filename):
        print('Creating new cluster object')
        cluster = super().__new__(ch)
        return cluster

    def __init__(self, filename):
        self.filename = filename
        self.particle_coords = self.get_matrix_from_file()
        self.particles, self.dims = self.particle_coords.shape
        self.energies = np.zeros((int(self.particles), int(self.particles)))
        self.distances = self.get_relative_distance()
        self.total_energy = self.get_total_energy()
        self.min_distance, self.min_location = self.get_minimum_distance()
        self.com = self.get_com()

    def get_matrix_from_file(self):
        y=[]
        f = open(self.filename, 'r')     
        for line in f:                
            g=line.split(' ')   ## split on space now         
            y.append(g)
        ##self.particle_coords=np.array(y).astype(np.float16)
        return np.array(y).astype(np.float16)
        ##print(self.array_y)
    
    def get_relative_distance(self):
        distances = np.zeros((int(self.particles), int(self.particles)))
        for b in range(self.particles):
            for a in range(b, self.particles):
                distances[b,a]= self.dist3d(self.particle_coords[b], self.particle_coords[a])
       ## print(distances)
        self.distances = distances
        return distances

    def dist3d(self, p1, p2):
        distance = pow((pow(p2[0]-p1[0], 2)+pow(p2[1]-p1[1], 2) + pow(p2[2]-p1[2],2)), 0.5)
       ## print('3D distance is :', distance)
        return distance
    
    def find_ljp(self, x):
        if (x!=0):
            self.ljp = 4*(pow(x, (-12)) - pow(x, (-6)))
        else :
            self.ljp=0
        ##print(f"The LJP of {x} is {self.ljp}")
        return self.ljp

    def get_total_energy(self):
        energies = np.zeros((int(self.particles), int(self.particles)))
        energy_sum = 0
        for b in range(self.particles):
            for a in range(b, self.particles):
                energies[b,a]= self.find_ljp(self.distances[b,a])
       ## print(energies)
        energy_sum=energies.sum()
        self.energies = energies
        self.total_energy = energy_sum()
        return energy_sum
    
    def get_minimum_distance(self):
        masked_temp = np.ma.masked_equal(self.distances, 0.0, copy=False)
        print(f"Minimum : {masked_temp.min()}, Maximum : {masked_temp.max()}")
        return masked_temp.min(), np.where(masked_temp==masked_temp.min())
    
    def get_com(self):
        com =[]
        for b in range(self.dims):
            _com=0
            for a in range(self.particles):
                _com = _com + self.particle_array[a,b]
            com.append((_com/self.particles))
        print(f"COM : {com}")
        return com
    
    def move_one_atom_random(self):
        random_particle = rand.randint(0, self.particles-1)
        random_dimension = rand.randint(0,self.dims-1)
        self.particle_coords[random_particle, random_dimension]= self.particle_coords[random_particle, random_dimension] + rand.uniform(-0.1, 0.1)
        