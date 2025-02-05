"""Termal properties: They will be called in the main function"""

def heat_flow(k: float, delta_t: float, delta_x: float)-> float:
    """Calculate the termal conductivity in the material select. 
    the operations is (q = -k*(delta_T/delta_x))

    Args:
        k (float): Termal conductivity (W/m^2)
        delta_t (float): Temperature difference (K)
        delta_x (float): thickness (m)

    Returns:
        float: This is the expected result
    """
    division = delta_t/delta_x
    if k < 0 or delta_t < 0 or delta_x < 0:
        return "Only numbers greater than zero"
    return k*division

def linear_thermal_expansion(delta_l: float, delta_t: float, l_o: float)-> float:
    """Calculate the linear thermal expansion in the material select. 
    the operations is (alpha = delta_l/(l_o*delta_t))

    Args:
        delta_l (float): length difference (m)
        dalta_t (float): temperature difference (K)
        l_o (float): initial length (m)

    Returns:
        float: This is the expected result
    """
    multi = l_o * delta_t
    if delta_l < 0 or delta_t < 0 or l_o < 0:
        return "Only numbers greater than zero"
    if l_o == 0 or delta_t == 0:
        return "Is not divisible by zero"

    return delta_l/multi

def heat_capacity(q: float, delta_t: float)-> float:
    """Calculate the heat capacity in the material select. 
    the operations is (C = q/delta_t)

    Args:
        q (float): absorbed heat (J)
        delta_t (float): temperature difference (K)

    Returns:
        float: This is the expected result
    """
    if q < 0 or delta_t < 0:
        return "Only numbers greater than zero"
    if delta_t == 0:
        return "Is not divisible by zero"
    return q/delta_t
