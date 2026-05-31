from factorial.factorial import factorial
def ncr(n, r):
    result = factorial(n) / (factorial(r) * factorial(n-r))
    return result
def npr(n, r):
    result = factorial(n) / factorial(n-r)
    return result
