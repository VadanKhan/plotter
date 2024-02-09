# -*- coding: utf-8 -*-
"""
@author: vadan
"""
# %% IMPORT STATEMENTS
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
import sys

# %% DECLARING CONSTANTS
kB = const.Boltzmann
elem = const.elementary_charge

# %% FUNCTION DEFINITIONS


def create_plot(graph_title, x_title, y_title, x_min, x_max, function_input,
                resolution, extra_input1, extra_input2, colour_input):
    """
    Will plot a range of x values into a function. If the function requires
    more than just the x value input, it will try putting in extra_input1
    afterwards, and if not extra_input2 second. If neither works code will
    exit.

    function inputs should be in order:
        func(variable, extra_input1, extra_input2)

    Returns
    -------
    0

    """

    fig = plt.figure()

    axes = fig.add_subplot(111)

    axes.set_title(
        graph_title + ' ($\epsilon =$ {0:1.3g}eV)'.format(extra_input1/elem))
    axes.set_xlabel(x_title)
    axes.set_ylabel(y_title)

    x_values = np.linspace(x_min, x_max, resolution)

    # define random color
    col = (np.random.random(), np.random.random(), np.random.random())

    try:
        axes.plot(x_values, function_input(x_values), color=colour_input,
                  label='Trend Prediction')
    except Exception:
        try:
            axes.plot(x_values, function_input(x_values, extra_input1),
                      color=colour_input, label='Trend Prediction')
        except Exception:
            try:
                axes.plot(x_values, function_input(x_values, extra_input1,
                                                   extra_input2), color=colour_input, label='Trend Prediction')
            except Exception:
                return 1
    plt.legend()
    plt.savefig(graph_title + '.png', dpi=777)
    plt.show()
    return 0


def func(T, e):
    '''
    equation from entropy analysis
    '''
    mult = 2*kB*(e/(kB*T))**2
    num = 2 + np.cosh(e/(kB*T))
    den = (1 + 2*np.cosh(e/(kB*T)))**2
    return mult * num/den

# %% MAIN


def main():
    """
    Main function. Will run all main_code, and if a 1 is returned, it will
    notify of a reading file error.
    """
    return_code = main_code()
    if return_code == 1:
        print("Error Graphing")
        sys.exit()
        return 1
    return 0


def main_code():
    """
    Contains all executed code. Should return 1 in the instance of a reading
    error.

    """
    # %% plot all functions
    # print(np.cosh(0.00001*elem/(kB*0.01)))
    create_plot('$C_V$ against T',
                'Temperature (K)', '$<C_V>$', 0.01, 10000, func, 777,
                0.01*elem, False, 'red')
    return 0


# %% MAIN EXECUTION
if __name__ == "__main__":
    main()
