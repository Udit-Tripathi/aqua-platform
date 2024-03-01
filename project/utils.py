import numpy as np

def sumvalues(values):
    """This function returns the sum of the values of the provided list/array(values)all elements of values -> int or float"""
    sum=0 
    values=np.array(values)
    for value in values:
        if type(value) == str:          
            raise Exception("invalid input")
        else:
            sum = sum + value           
    return sum


    
def maxvalue(values):
    """Takes a parameter called values, calculates the max value in values then returns that number""" 
    max_index=0
    length = 0
    for char in values:
        length += 1 
    for i in range(length): 
        if type(values[i])==str: 
            raise Exception("invalid input")
        elif values[i]>values[max_index]:
            max_index=i  
    return max_index


def minvalue(values):
    """This function returns the minimum value of the provided list/array(values) all elements of values -> int or float"""   
    min_index=0
    length=0
    for char in values:
        length += 1  
    for i in range(length): 
        if type(values[i])==str:
            raise Exception("invalid input")
        elif values[i]<values[min_index]:
            min_index=i  
    return min_index


def meannvalue(values): 
    """This function returns the mean of the values of the provided list/array(values) all elements of values -> int or float"""
          
    sumvalue=0
    num_value=0
    for value in values:
        num_value+=1    
    for value in values: 
        if type(value)==int or type(value)==float:
            sumvalue+=value 
        else:
            raise Exception("invalid input")
    mean=sumvalue/num_value
    return mean
    

def countvalue(values,x):
    """This function returns the number of occurrences of the value x in the provided list or array"""
    occuring_value=0
    for value in values:
        if x==value:
            occuring_value+=1
    return occuring_value    
    



