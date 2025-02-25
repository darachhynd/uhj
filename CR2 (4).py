import numpy as np

def polyfit_coeffs(x, y):
    # | P_0(x_0)  P_1(x_0)  P_2(x_0)  P_3(x_0) | | a_0 |     | y_0 |
    # | P_0(x_1)  P_1(x_1)  P_2(x_1)  P_3(x_1) | | a_1 |  =  | y_1 |
    # | P_0(x_2)  P_1(x_2)  P_2(x_2)  P_3(x_2) | | a_2 |     | y_2 |
    # | P_0(x_3)  P_1(x_3)  P_2(x_3)  P_3(x_3) | | a_3 |     | y_3 |
    #                                              ==> Ma = y
    # find the matrix M, solve Ma = y by numpy.linalg.solve(), and return array a

    # Matrix M
    M = np.zeros([4,4])
    for i in range(4):
#  row i of M: [  P_0(x_i) ,    P_1(x_i)   ,    P_2(x_i)   ,  P_3(x_i)  ]
        M[i] = [1 - x[i]**3, x[i] + x[i]**2, x[i]**2 - x[i], 1 + x[i]**3]

    # solve Ma = y, and return a
    return np.linalg.solve(M, y)
