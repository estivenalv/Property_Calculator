"""electrical properties: They will be called in the main function"""

def electrical_conductivity(rho: float) -> float:
    """Calculate the electrical conductivity in the material select. 
    the operations is (sigma = 1 / rho)

    Args:
        rho (float): electrical resistivity

    Returns:
        float: This is the expected result
    """
    if rho < 0:
        return "Only numbers greater than zero"
    if rho == 0:
        return "Is not divisible by zero"
    return 1/rho

def voltage(i: float, r: float)-> float:
    """Calculate the voltage in the material select. 
    the operations is (v = i*r)

    Args:
        i (float): current
        r (float): resistance

    Returns:
        float: This is the expected result
    """
    if i < 0 or r < 0:
        return "Only numbers greater than zero"
    return i*r
