"""densitometric properties: They will be called in the main function"""

def density(m: float, v: float)->float:
    """Calculate the density in the material select. 
    the operations is (d = m/v)

    Args:
        m (float): mass (Kg)
        v (float): volume (m^3)

    Returns:
        float: This is the expected result
    """
    if m < 0 or v < 0:
        return "Only numbers greater than zero"
    if v == 0:
        return "Is not divisible by zero"
    return m/v

def porosity(v_p: float, v_t: float)-> float:
    """Calculate the porosity in the material select. 
    the operations is (p = v_p/v_t)

    Args:
        v_p (float): pore volume (m^3)
        v_t (float): total volume (m^3)

    Returns:
        float: This is the expected result
    """
    if v_p < 0 or v_t < 0:
        return "Only numbers greater than zero"
    if v_t == 0:
        return "Is not divisible by zero"
    return v_p/v_t
