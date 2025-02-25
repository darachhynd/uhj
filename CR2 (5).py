import numpy as np 

def polyfit_coeffs(x, y):
    ''' 
    Returns a vector of the 4 unknown coefficients, a_i, of the polynomial 
    p(x) = a_0p_0(x) + a_1p_1(x) + a_2p_2(x) + a_3p_3(x). 

    Parameters
    ----------
    x : length 4 vector 
        Each x[i] is the value of x_i 
    y : length 4 vector 
        Each y[i] is the value of y_i = p(x_i)
    '''
    # Define a 4x4 matrix with every element set to 0. This matrix will later be changed within the function.
    # This matrix has the shape 4x4 since it will be used to solve the linear system A * a = y and both a & y are length 4 vectors
    # so for this system to work, the number of columns and rows in A must match the number of rows in a and y respectively. 
    A = np.zeros([4,4])
    # Using the defintion of the 4 polynomials that sum to make p(x), create a tuple, p_values, where each element i is a numpy array 
    # containing the values of p_0 to p_3 for x[i].
    p_0 = 1 - x**3
    p_1 = x + x**2
    p_2 = x**2 - x
    p_3 = 1 + x**3 
    p_values = (p_0, p_1, p_2, p_3)
    for i in range(4):
    # Change the matrix A so that each column i contains the values for p_0 to p_3 for x[i]
        A[:, i] = p_values[i]
    # Solve the linear system A * a = y to find the values of a_0, a_1, a_2 & a_3
    a = np.linalg.solve(A, y)
    return a