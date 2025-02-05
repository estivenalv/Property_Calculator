"""calling functions in other modules create by me.
"""
from properties import mec_prop
from properties import ter_prop
from properties import ele_prop
from properties import opt_prop
from properties import mag_prop
from properties import den_prop

def solution(gen_prop: list) -> list | None:
    """Take the list and confirm if exist values, if not, don't
    create nothing
    
    Args:
        gen_prop (list): list create for properties

    Returns:
        list | None: list with values groups in other list
    """
    accumulate = []

    for prop in gen_prop:
        if gen_prop[0] in gen_prop:
            accumulate.append(prop)
        else:
            accumulate.append(None)

    return accumulate


def property_calculator()-> float:
    """ Will have the capacity of interact with many options to propierties of
    materials and resolve basics operations 

    Returns:
        float: The general solution will have numbers with decimals
    """
    mech_prop = []
    term_prop = []
    elec_prop = []
    opti_prop = []
    magn_prop = []
    dens_prop = []

    while True:
        print("--- CALCULATOR ---\n")
        print("1. Mechanical properties")
        print("2. Termal properties")
        print("3. Electrical properties")
        print("4. Optical properties")
        print("5. Magnetic properties")
        print("6. Densitometric properties")
        print("7. Exit")

        option = input("What do you want to calculate?\n")

        if option == "1": # Mechanical properties
            while True:
                print("-> Mechanical properties <-")
                print("1. Young's module")
                print("2. Shear stress")
                print("3. Tensile strength")
                print("4. Hardness")
                print("5. Exit")

                option = input("What property?\n")
                match option:
                    case "1": # Young's module
                        sigma = float(input("value the stress\n"))
                        epsilon = float(input("value the deformation\n"))
                        operation = round(mec_prop.young_module(sigma,epsilon),4)
                        mech_prop.append(f"Young's module : {operation}")
                    case "2": # Shear stress
                        beta = float(input("value the shear modulus\n"))
                        gamma = float(input("value the angular deformation\n"))
                        operation = round(mec_prop.shear_stress(beta,gamma),4)
                        mech_prop.append(f"Shear stress : {operation}")
                    case "3": # Tensile strength
                        f_max = float(input("value the maximum supported force\n"))
                        a_o = float(input("value the initial area of cross section\n"))
                        operation = round(mec_prop.tensile_strength(f_max,a_o),4)
                        mech_prop.append(f"Tensile strength : {operation}")
                    case "4": # Hardness
                        f = float(input("value the maximum supported force\n"))
                        d_indent = float(input("value the initial area of cross section\n"))
                        d_print = float(input("value the initial area of cross section\n"))
                        operation = round(mec_prop.hardness(f, d_indent, d_print),4)
                        mech_prop.append(f"Hardness : {operation}")
                    case "5":
                        print("-> You left the mechanical properties <-")
                        break
                    case _ :
                        print("This option is not valid")
        elif option == "2": # Termal properties
            while True:
                print("-> Termal properties <-")
                print("1. Heat flow")
                print("2. Linear thermal expansion")
                print("3. Heat capacity")
                print("4. Exit")

                option = input("What property?\n")
                match option:
                    case "1":
                        k = float(input("value the termal conductivity\n"))
                        delta_t = float(input("value the temperature difference\n"))
                        delta_x = float(input("value the thickness\n"))
                        operation = round(ter_prop.heat_flow(k,delta_t,delta_x),4)
                        term_prop.append(f"Heat flow : {operation}")
                    case "2":
                        delta_l = float(input("value the length difference\n"))
                        delta_t = float(input("value the temperature difference\n"))
                        l_o = float(input("value the initial length\n"))
                        operation = round(ter_prop.linear_thermal_expansion(delta_l,delta_t,l_o))
                        term_prop.append(f"Linear thermal expansion : {operation}")
                    case "3":
                        k = float(input("value the termal conductivity\n"))
                        delta_t = float(input("value the temperature difference\n"))
                        operation = round(ter_prop.heat_capacity(k,delta_t),4)
                        term_prop.append(f"Heat Capacity : {operation}")
                    case "4":
                        print("-> You left the termal properties <-")
                        break
                    case _ :
                        print("This option is not valid")
        elif option == "3": # Electrical properties
            while True:
                print("-> Electrical properties <-")
                print("1. Electrical conductivity")
                print("2. Ohm's law")
                print("3. Exit")

                option = input("What property?\n")
                match option:
                    case "1": # Electrical conductivity
                        rho = float(input("value the electrical resistivity\n"))
                        operation = round(ele_prop.electrical_conductivity(rho),4)
                        elec_prop.append(f"Electrical conductivity : {operation}")
                    case "2": # Ohm's law
                        i = float(input("value the current\n"))
                        r = float(input("value the resistance\n"))
                        operation = round(ele_prop.voltage(i,r),4)
                        elec_prop.append(f"Ohm's law : {operation}")
                    case "3":
                        print("-> You left the electrical properties <-")
                        break
                    case _ :
                        print("This option is not valid")
        elif option == "4": # Optical properties
            while True:
                print("-> Optical properties <-")
                print("1. Refractive index")
                print("2. Transmittance and absorbance")
                print("3. Exit")

                option = input("What property?\n")
                match option:
                    case "1": # Refractive index
                        v = float(input("value the speed of light in material\n"))
                        operation = round(opt_prop.refractive_index(v),4)
                        opti_prop.append(f"Refractive index : {operation}")
                    case "2": # Transmittance and absorbance
                        i = float(input("value the transmitted intensity \n"))
                        i_o = float(input("value the incident intensity\n"))
                        operation = opt_prop.transmittance_absorbance(i,i_o)
                        opti_prop.append(operation)
                    case "3":
                        print("-> You left the optical properties <-")
                        break
                    case _ :
                        print("This option is not valid")
        elif option == "5": # Magnetic properties
            while True:
                print("-> Magnetic properties <-")
                print("1. Magnetization")
                print("2. Magnetic induction")
                print("3. Exit")

                option = input("What property?\n")
                match option:
                    case "1": # Magnetization
                        x = float(input("value the magnetization \n"))
                        h = float(input("value the magnetic field\n"))
                        operation = round(mag_prop.magnetization(x,h),4)
                        magn_prop.append(f"Magnetization: {operation}")
                    case "2": # Magnetic induction
                        miu = float(input("value the magnetic permeability \n"))
                        h = float(input("value the magnetic field\n"))
                        operation = round(mag_prop.magnetic_induction(miu,h),4)
                        magn_prop.append(f"Magnetic induction: {operation}")
                    case "3":
                        print("-> You left the optical properties <-")
                        break
                    case _ :
                        print("This option is not valid")
        elif option == "6": # Densitometric properties
            while True:
                print("-> Densitometric properties <-")
                print("1. Density")
                print("2. Porosity")
                print("3. Exit")

                option = input("What property?\n")
                match option:
                    case "1": # Density
                        m = float(input("value the mass\n"))
                        v = float(input("value the volume\n"))
                        operation = round(den_prop.density(m,v),4)
                        dens_prop.append(f"Density: {operation}")
                    case "2": # Porosity
                        v_p = float(input("value the pore volume\n"))
                        v_t = float(input("value the total volume\n"))
                        operation = round(den_prop.porosity(v_p,v_t),4)
                        dens_prop.append(f"porosity: {operation}")
                    case "3":
                        print("-> You left the optical properties <-")
                        break
                    case _ :
                        print("This option is not valid")
        elif option == "7": # Exit
            print("-> You left the calculator <-")
            break
        else:
            print("This option is not valid")

    mechanical_property = solution(mech_prop)
    print(f" mechanical properties {mechanical_property}")

    termal_property = solution(term_prop)
    print(f" termal properties {termal_property}")

    electrical_property = solution(elec_prop)
    print(f" mechanical properties {electrical_property}")

    optical_property = solution(opti_prop)
    print(f" mechanical properties {optical_property}")

    magnetical_property = solution(magn_prop)
    print(f" mechanical properties {magnetical_property}")

    densitometric_property = solution(dens_prop)
    print(f" mechanical properties {densitometric_property}")

if __name__ == '__main__':
    property_calculator()
