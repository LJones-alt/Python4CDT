#Lets do some list manipulation
a=[1,2,3,4,5]
print('The original list is : ', a)
# To select a list element - use [] and the position in the list
# To raise a numeric value to a power, use **  
print('Now lets square the number in position 1 : ', 'a[1]**2 = ',(a[1]**2))
print('Now lets take the value of the first element away from the last element : ', 'a[-1]-a[0] = ', a[-1]-a[0])
# replace a[1] with a[3]
a[1]=a[3]
print('Now replace the value in position 1 with that in position 3: ', 'a[1] = a[3]', a)
