"""optical properties: They will be called in the main function"""
import math

def refractive_index(v: float)-> float:
    """Calculate the electrical conductivity in the material select. 
    the operations is (n = c/v)

    Args:
        v (float): speed of light in material (m/s)

    Returns:
        float: This is the expected result
    """
    c = 300000000
    if v < 0:
        return "Only numbers greater than zero"
    if v == 0:
        return "Is not divisible by zero"
    return c / v

def transmittance_absorbance(i: float, i_o: float)-> dict:
    """Calculate the transmittance and absorbance in the material select. 
    the operations is (t = i/i_o) and (a = -log(t))

    Args:
        i (float): transmitted intensity
        i_o (float): incident intensity

    Returns:
        dict: This is the expected result
    """
    if i < 0 or i_o < 0:
        return "Only numbers greater than zero"
    if i_o == 0:
        return "Is not divisible by zero"

    # transmittance calculation
    t = i/i_o

    # absorbance calculation
    a = -math.log(t)

    return {
        "Transmittance": t,
        "Absorbance": a
    }
