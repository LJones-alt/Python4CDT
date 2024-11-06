## Hold all the gubbins for task 4 
from ClusterHandler import ClusterHandler as ch
import random

clusterHanlder = ch('data.txt')
total_energy = clusterHanlder.get_total_energy()
print(total_energy)

print(clusterHanlder.min_distance, 'at' , clusterHanlder.min_location)

## optimisation code

clusterHanlder.move_one_atom_random()