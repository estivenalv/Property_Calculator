"""Mechanical properties: They will be called in the main function"""
import math

def young_module(sigma: float, epsilon: float)-> float:
    """ Calculate the young's module in the material select. 
    the operations is (E = sigma/epsilon)

    Args:
        sigma (float): stress (Pa or N/m^2)
        epsilon (float): deformation (adimensional)

    Returns:
        float: This is the expected result
        """
    if sigma < 0 or epsilon < 0:
        return "Only numbers greater than zero"
    if epsilon == 0:
        return "Is not divisible by zero"
    return sigma/epsilon

def shear_stress(beta: float, gamma: float)-> float:
    """ Calculate the shear stress in the material select. 
    the operations is (T = beta * gamma)

    Args:
        beta (float): Shear modulus (Pa or N/m^2)
        gamma (float): Sngular deformation (rad)

    Returns:
        float: This is the expected result
    """
    if beta < 0 or gamma < 0:
        return "Only numbers greater than zero"
    return beta*gamma

def tensile_strength(f_max: float, a_o: float)-> float:
    """ Calculate the tensile strength in the material select. 
    the operations is (UTS = F_max/a_o)

    Args:
        f_max (float): Maximun supported force (N)
        a_o (float): Initial area of cross section (m^2)

    Returns:
        float: This is the expected result
    """
    if f_max < 0 or a_o < 0:
        return "Only numbers greater than zero"
    if a_o == 0:
        return "Is not divisible by zero"
    return f_max/a_o

def hardness(f: float, d_indent: float,d_print: float)-> float:
    """Calculate the hardness in the material select. 
    the operations is (HB = (2*f)/pi*d_ident(d_ident - sqrt(d_ident^2 - d_print^2)))

    Args:
        f (float): Applied force (N)
        d_indent (float): Indenter diameter (mm)
        d_print (float): Print diameter (mm)

    Returns:
        float: This is the expected result
    """
    numerator = 2 * f
    denominator = math.pi * d_indent * (d_indent-math.sqrt(d_indent**2 - d_print**2))
    if denominator < 0:
        return "Only numbers greater than zero"
    if denominator == 0:
        return "Is not divisible by zero"
    return numerator/denominator
