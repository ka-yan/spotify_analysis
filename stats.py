"""
Kalyan Khatiwada
Project03
CS152B
4 October, 2022

This file is a library of functions that calculate certain statistics
such as sum, mean, min, max and variance. This file can be called to calculate those functions.
"""

def sum(numbers):
    """Calculates the sum of numbers given to it"""
    a= 0
    for num in numbers:
        a+=num
    return a
 

def mean(data):
    """Calculates the mean of the list of the numbers given as an argument."""
    summ= sum(data) #calls the sum function
    count = len(data)
    mean = summ / count
    return mean

def min(data):
    """Returns the minimum data value of the given list of numbers"""
    min = 2000 #a value higher than any values in the list
    for i in data:
        if i < min:
            min = i
    min_num = min
    return min_num

def max(data):
    """Returns the maximum value from the given list of values"""
    a = -2000 #value lower than any values in the list
    for i in data:
        if i > a:
            a = i
    max_num = a
    return max_num

def variance(data):
    """Returns the variance of the data given as arguments
    The variance is calculated by transforming the mathematical formula into a form python can understand or do easily. """
    mean1 = mean(data) #calling the mean function
    N = len(data)
    sum_diff =0
    for i in data:
        sum_diff += (i - mean1) ** 2 # calculating the sum of the square of the differences between the number and mean
    variance = sum_diff/(N-1) # Using the variance formula in pythonic terms
    return variance



if __name__ == "__main__":
    mean()
    min()
    max()
    variance()

