## this code prints the number between two user defined numbers. some error handling included


class NumberClass:
    def __init__(self, lower_limit, upper_limit, steps):
        self.lower_lim = lower_limit
        self.upper_lim = upper_limit
        self.steps = steps
        ## minor error handling
        [self.error, self.error_code] = self.limit_check()
        self.even_list = []
        self.even_list_sum =0
        self.list_sum = 0
   
    
    ## this defines what you see when you call the object!
    def __str__(self):
        return f"{self.lower_lim}, {self.upper_lim}, {self.steps}"
        
    def limit_check(self):
        if (self.lower_lim >= self.upper_lim):
            return 1, 'lower limit above upper'
        else:
            if ((self.upper_lim - self.lower_lim) < self.steps):
                return 1, 'step value larger than range'
            else: 
                self.test_list = list(range(self.lower_lim, self.upper_lim, self.steps))
                return 0, 'OK'

    def print_list(self,list_to_print):
        a=0
        print('The result is : ')
        while a<len(list_to_print):
            print(list_to_print[a])
            a=a+1

    def create_even_array(self):
        if self.error ==0:
            a=self.lower_lim
            ## handle first one being odd
            if (a%2 !=0):
                a=a+1
            while a<= self.upper_lim:
                if a%2==0:
                    self.even_list.append(a)
                a=a+self.steps
            self.print_list(self.even_list)
        else:
            print(self.error_code)

    def sum_all_even(self):
        a=0
        while (a<len(self.even_list)):
            self.even_list_sum = self.even_list_sum + self.even_list[a]
            a=a+1
        print('The sum of the even values is : ')
        print(self.even_list_sum)

    def find_mean_of_list(self):
        a=0
        self.test_list = list(range(self.lower_lim, self.upper_lim, self.steps))
        while (a<len(self.test_list)):
            self.list_sum = self.list_sum + self.test_list[a]
            a=a+1
        self.list_mean = self.list_sum / a
        print('The mean of the list is :')
        print(self.list_mean)
    
    def make_all_negative(self):
        a=0
        self.negative_list = self.test_list.copy()
        while (a<len(self.test_list)):
            if (self.test_list[a] >0) :
                self.negative_list[a] = -abs(self.test_list[a])
            a=a+1
        self.print_list(self.negative_list)

    def does_list_have_zero(self):
        if 0 in self.test_list:
            print('The list b contains a zero')
        else:
            print('The list b does not contain a zero')
        
class FactorialList:
    def __init__(self, array_length):
        self.array_length = array_length
        self.factorial_array = [0]
    
    def create_factorial_array(self):
        a=1
        self.factorial_array[0] =1
        while (a<self.array_length):
            self.factorial_array.append(self.factorial_array[a-1] * (a+1))
            a=a+1
        self.print_list(self.factorial_array)
    
    def print_list(self,list_to_print):
        a=0
        print('The result list is : ')
        while a<len(list_to_print):
            print(list_to_print[a])
            a=a+1

class FussyDivider:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.result =0 
        self.error , self.error_code = self.is_y_non_zero()

    def is_y_non_zero(self):
        if (self.y!=0):
            self.error = False
            self.error_code = 'OK'
        else: 
            self.error = True
            self.error_code = 'cannot divide by zero'
            print(self.error_code)
        return self.error, self.error_code
    
    def do_divison(self):
        if self.error :
            return 
        else:
            self.result = self.x/self.y
            print('The result is', self.result)

## This is tasks 1.3 - 1.5 
print_these = NumberClass(1,10,2)
print(print_these.error_code)
## Task 1.3
print_these.create_even_array()
## Task 1.4
print_these.sum_all_even()

## Task 1.5
factoriallist=FactorialList(10)
factoriallist.create_factorial_array()

## Task 1.6
print_these.find_mean_of_list()

## Task 1.7
fussyDivider = FussyDivider(5, 10)
fussyDivider.do_divison()

## Task 1.8
negative_printer = NumberClass(-2, 5, 1)
negative_printer.make_all_negative()

## Task 1.9
print('For the list in 1.2-1.4 : ')
print_these.does_list_have_zero()
print('For the list in 1.8 : ')
negative_printer.does_list_have_zero()