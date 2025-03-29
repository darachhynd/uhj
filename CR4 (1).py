def polynomial_with_roots(N, m):
    """Return the power series coefficient of the expansion (sum from q=0 to N)(a_q * x ^ q) as an integer.

    Parameters
    ----------

    N : int
        A strictly positive integer denoting the degree of the polynomial p(x).
    m : int
        An integer strictly between 0 and N denoting the index of the coefficient 
        to be returned in the power series expansion of p(x)..

    Returns
    -------

    p[m] : int
        The coefficient a_m of the x^m term in the expansion of p(x).
    """

    # initialise p(x) with p(x) = 1
    # here, p(x) only has one coefficient ([1])
    p = [1]

    # multiplying p(x) by (qx + 1) for each q from 1 to N
    for q in range(1, N + 1): # from 1 to (N + 1) - 1, ie from 1 to N

        # firstly, we append 0's to prepare for the new higher power term that we get when multiplying by each qx in (qx + 1)
        # ie when we multiply by qx, we get a new term with degree increased by 1 and hence a new coefficient
        p.append(0)
        
        # for each q: updating the  coefficients from the highest degree term (ie the last coeffiecient) first to avoid overwriting coefficients when still updating the lower degree terms
        for i in range(len(p) - 1, 0, -1): # from the last index (index of the highest degree term) to the first, with step size 1.
            # updating the coefficient at position i in the list p
            p[i] += p[i - 1] * q # multiplying by qx increases the power of x by 1, ie from i - 1 to i (e.g. x ^ 1 becomes x ^ 2)

            # note that the 1 from (qx + 1) only affects the constant term, ie note how the 1 stays "the same" in (x + 1) * (2x + 1) = 2x^2 + 3x + 1.
            # this is why we don't include the 0th term in the above loop


    # Return the coefficient of x^m
    return p[m]