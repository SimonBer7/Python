
def get_i(u, r):
    if (isinstance(u, int or float)) and (isinstance(r, int or float)) and u > 0 and r > 0:
        result_i = float(u / r)
    else:
        raise ValueError
    return result_i

def get_u(i, r):
    if (isinstance(i, int or float)) and (isinstance(r, int or float)) and i > 0 and r > 0:
        result_u = i * r
    else:
        raise ValueError
    return result_u

def get_r(i, u):
    if (isinstance(i, int or float)) and (isinstance(u, int or float)) and u > 0 and i > 0:
        result_r = u / i
    else:
        raise ValueError
    return result_r



