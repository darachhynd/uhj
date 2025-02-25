import numpy as np
def polyfit_coeffs(x, y):
    '''This function computes the coefficients of the interpolating polynomial p(x) 
    that passes through the points (x_i, y_i) using the basis polynomials defined below.
    
    Args:
        x: A length 4 NumPy vector 'x' of floating point values, with 'x[i]' 
        containing the value of x_i,
        y: A length 4 NumPy vector 'y' of floating point values, with 'y[i]' 
        containing the value of y_i,
    Returns:
        a:  a length 4 NumPy vector 'a' of floating point values, with 'a[i]' 
        containing the value of the coefficient a_i.
    Raises:
        ValueError: If 'x' or 'y' is not a length 4 array.
    '''
    
    # Check if the arrays x and y are of length 4
    if len(x) != 4 or len(y) != 4:
        raise ValueError("Both 'x' and 'y' must be arrays of length 4.")
    
    # Define the basis polynomials p0(x), p1(x), p2(x), p3(x)
    def p0(x): return 1 - x**3
    def p1(x): return x + x**2
    def p2(x): return x**2 - x
    def p3(x): return 1 + x**3

    # Construct the polynomial matrix P - transpose it since y is the dot product between P and the coefficient matrix a.
    P_T = np.vstack([p0(x), p1(x), p2(x), p3(x)]).T

    # Solve the system (P^T)a = y for a
    a = np.linalg.solve(P_T, y)
    
    return a


