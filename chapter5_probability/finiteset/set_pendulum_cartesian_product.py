"""
Applying a formula to multiple sets of variables
"""

from sympy import FiniteSet, pi

def time_period(length, g):

    g = 9.8
    T = 2*pi*(length/g)**0.5

    return T

if __name__ == '__main__':

    L = FiniteSet(15, 18, 21, 22.5, 25)
    g_values = FiniteSet(9.8, 9.78, 9.83)

    print('{0:^15}{1:^15}{2:^15}' .format('Length(cm)', 'Gravity(m/s^2)', 'Time Period(s)')) # Specifies how the printing is done

    for elem in L*g_values: # Calculate the Cartesian product (all possible combinations of the two sets)
        l = elem[0]
        g = elem[1]
        t = time_period(l/100, g)
        print('{0:^15}{1:^15}{2:^15.3f}' .format(float(l), float(g), float(t))) # Specifies the printing
