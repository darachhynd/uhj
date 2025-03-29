def polynomial_with_roots(N, m):
    """
    Return the coefficient a_m of x^m in p(x),
    computed exactly using integer arithmetic.
    """
    # Initialize a list of length m+1 to hold coefficients of x^0 through x^m
    coeffs = [1] + [0] * m

    # Build up the polynomial factor‑by‑factor
    for q in range(1, N + 1):
        # Only update down to k = 1, up to m
        for k in range(min(q, m), 0, -1):
            coeffs[k] += q * coeffs[k - 1]

    return coeffs[m]