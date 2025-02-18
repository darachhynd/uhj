import numpy as np

def polyfit_coeffs(x, y):
  """ takes two arrays, x and y and return an  array of coefficients that satsify the condition the polynomial passed through all the points"""
    def p0(x):
        y = 1 - x**3
        return y
    def p1(x):
        y = x + x**2
        return y
    def p2(x):
        y = x**2 - x
        return y
    def p3(x):
        y = 1+x**3
        return y
    # returns an array of the calculated values for p_1,p_2 etc for a given value of x 
    def p(x):
        y =np.array([p0(x),p1(x),p2(x),p3(x)])
        return y
    
    # creates a  coeffieinrtr matrix 
    X = np.concatenate(([p(x[0])],[p(x[1])],[p(x[2])],[p(x[3])]),axis = 0)
    # solves Xa = y for a
    solution = np.linalg.solve(X, y)
    
    return(solution)
  
