import numpy as np

def midpoint(f, a, b, M):
    '''
    Returns the integral of a generic function f calculated by the midpoint rule 
    over the interval [a, b] using M subintervals as instructed.
    
    Parameters:
        f (function): The function to be integrated.
        a (float): The starting point of the interval.
        b (float): The ending point of the interval.
        M (int): The number of subintervals to use in the approximation.
    
    Returns:
        float: The approximated integral value.
    '''
    # Step size (width of each sub-interval)
    h = (b - a) / M  
    
    # Computing sum of function values at midpoints
    integral = sum(f(a + (i + 0.5) * h) for i in range(M))
    
    # Multiplying by step size to approximate the integral
    return integral * h 