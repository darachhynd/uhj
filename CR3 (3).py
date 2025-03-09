import numpy as np

def midpoint(f, a, b, M):
    '''
    Returns the integral of a generic function f calculated by the midpoint rule over the interval [a,b] using M subintervals as instructed.
    '''
    subint_sum = 0
    for i in range(M):
        h = (b-a)/M # the width of each sub interval
        lower = a + i*h
        upper = a + (i+1)*h # upper and lower here refer to the upper and lower boundaries of the sub intervals over which we are summing 
        subint_sum = subint_sum + f((upper + lower)/2)
        
    approx_integral = subint_sum * (b-a)/M
    return approx_integral
