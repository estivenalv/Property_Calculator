"""magnetic properties: They will be called in the main function"""

def magnetization(x: float, h: float)->float:
    """Calculate the magnetization in the material select. 
    the operations is (M = x*h)

    Args:
        x (float): magnetic susceptibility
        h (float): magnetic field (A/m)

    Returns:
        float: This is the expected result
    """
    if x < 0 or h < 0:
        return "Only numbers greater than zero"
    return x*h

def magnetic_induction(miu: float, h: float)-> float:
    """Calculate the magnetic induction in the material select. 
    the operations is (B = miu*h)

    Args:
        miu (float): magnetic permeability (H/m)
        h (float): magnetic field (A/m)

    Returns:
        float: This is the expected result
    """
    if miu < 0 or h < 0:
        return "Only numbers greater than zero"
    return miu*h
