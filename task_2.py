## This code adresses the problems in task 2 

from cluster import Cluster
import matplotlib.pyplot as plt
import math
import numpy as np

class ArrayManipulator:
    def __init__(self, lower, upper, step):
        self.lower_limit = int(lower)
        self.upper_limit = int(upper)
        self.step = int(step)
        self.error, self.error_code = self.quick_check()
        self.test_list = self.make_array()
        self.in_order = True
        self.duplicates = False
        self.list_mean= 0
    
    def __str__(self):
        return f"{self.lower_limit}, {self.upper_limit}, {self.step}"

    def quick_check(self):
        if(self.upper_limit > self.lower_limit):
            if self.step >0 :
                return False, 'OK'
            else :
                return True, 'Impossible array'
        else:
            if self.step > 0:
                return True, 'Impossible array'
            else : 
                return False, 'OK'
    
    def make_array(self):
        if self.error:
            return
        else:
            return list(range(self.lower_limit, self.upper_limit, self.step))
    
    def make_all_zero(self):
        ## this is a lazy solution, but achieves the same result
        self.all_zero = [0] * len(self.test_list)
        print('Set all to 0')
    
    def are_elements_in_order(self):
        a=1
        if (self.step > 0):
            while (a<len(self.test_list)):
                if (self.test_list[a] < self.test_list[a-1]):
                    self.in_order = False
                    print('List elements are not in order')
                    break
                a=a+1
        else:
            while(a<len(self.test_list)):
                if(self.test_list[a]> self.test_list[a-1]):
                    self.in_order = False
                    print('List elements are not in order')
                    break
                a=a+1
        if (self.in_order): 
            print('List elements are in order')
    
    def are_any_elements_equal(self):
        a=0
        while (a<len(self.test_list)):
            temp = self.test_list.copy()
            temp.remove(self.test_list[a])
            if (self.test_list[a] in temp):
                self.duplicates = True
                print('Duplicate values found')
                break
            a=a+1
        if (self.duplicates==False): 
            print('No duplicate values found')
    
    def find_mean(self):
        a=0
        list_sum=0
        while (a<len(self.test_list)):
            list_sum = list_sum + self.test_list[a]
            a=a+1
        self.list_mean = list_sum / a
        print('The mean of the list is :')
        print(self.list_mean)

class DistanceCalculation:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.ljp =0
        self.distance3d = 0

    def find_ljp(self, x):
        self.x = x
        self.ljp = 4*(pow(self.x, (-12)) - pow(self.x, (-6)))
        f"The LJP of {x} is {self.ljp}"
        return self.ljp
    
    def dist3d(self):
        distance = pow((pow(self.x2-self.x1, 2)+pow(self.y2-self.y1, 2) + pow(self.z2-self.z1,2)), 0.5)
        print('3D distance is :', distance)
        return distance

class PlotMaker:
    def __init__(self, colour, x_label, y_label):
        self.colour = colour
        self.x_label = x_label
        self.y_label = y_label
        self.x_vals = np.linspace(0,(2*math.pi),201)
        
    
    def make_sin_plot(self):
        plt.plot(self.x_vals, np.sin(self.x_vals), color=self.colour, linestyle='dashed' )
        plt.plot.xlabel = self.x_label
        plt.plot.ylabel = self.y_label
        plt.plot.axis=('tight')
        plt.show()
        
        

## Task 2.1
arrayMultiplier = ArrayManipulator(1, 10, 1)
arrayMultiplier.make_all_zero()

## Task 2.2
print('Checking array order')
arrayMultiplier.are_elements_in_order()
print('Flipping one value, checking order again')
arrayMultiplier.test_list[3] = arrayMultiplier.test_list[3] * (-1)
arrayMultiplier.are_elements_in_order()

## Task 2.3
print('Checking for duplicates in array')
arrayMultiplier.are_any_elements_equal()
print('Now setting two values to the same')
arrayMultiplier.test_list[2] = arrayMultiplier.test_list[3]
arrayMultiplier.are_any_elements_equal()

## Task 2.4
#inputArray = ArrayManipulator(input('Lower limit : '), input('Upper limit : '), input('Step Size : '))

## Task 2.5
distanceCalc = DistanceCalculation(1,2,3,4,5,6)
distanceCalc.find_ljp(5)
print("The LJP of ", distanceCalc.x,  "is : ", distanceCalc.ljp)

## Task 2.6
distanceCalc.dist3d()

## Task 2.7
newCluster = Cluster(1,2,3,4,5,6,10,10,10)
newCluster.find_ljp(5)
newCluster.dist3d()


## Task 2.8
plotmaker = PlotMaker('green', 'x', 'y')
plotmaker.make_sin_plot()

## Task 2.10
newCluster.get_particle_distance()