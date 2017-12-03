def factors(n):
    """
    returns a set of the factor of n
    """
    return list(set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n // i)
    ))


print(factors(12))
q = factors(12)
print(type(q))
